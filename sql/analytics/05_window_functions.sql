-- =========================================================
-- DATA ANALYST PHASE 4
-- WINDOW FUNCTIONS
-- =========================================================
--
-- Topics:
--   ROW_NUMBER
--   RANK
--   DENSE_RANK
--   LAG
--   LEAD
--   Running Total
--   Moving Average
--   NTILE
--
-- Source:
--   v_analytics_users
--   v_analytics_posts
-- =========================================================


-- =========================================================
-- 1. ROW_NUMBER vs RANK vs DENSE_RANK
--
-- Business question:
-- Who are the top content creators?
-- What happens when multiple users have the same post count?
-- =========================================================

WITH creator_stats AS (
    SELECT
        u.id,
        u.name,
        COUNT(p.id) AS total_posts

    FROM v_analytics_users u

    LEFT JOIN v_analytics_posts p
        ON p.user_id = u.id

    GROUP BY
        u.id,
        u.name
)

SELECT
    id,
    name,
    total_posts,

    ROW_NUMBER() OVER (
        ORDER BY total_posts DESC
    ) AS row_number_rank,

    RANK() OVER (
        ORDER BY total_posts DESC
    ) AS rank_value,

    DENSE_RANK() OVER (
        ORDER BY total_posts DESC
    ) AS dense_rank_value

FROM creator_stats

ORDER BY
    total_posts DESC,
    id

LIMIT 40;


-- =========================================================
-- 2. LAG
--
-- Business question:
-- How did monthly post activity change compared
-- with the previous month?
-- =========================================================

WITH monthly_posts AS (
    SELECT
        DATE_TRUNC(
            'month',
            created_at
        )::date AS month,

        COUNT(*) AS total_posts

    FROM v_analytics_posts

    GROUP BY month
),

monthly_comparison AS (
    SELECT
        month,
        total_posts,

        LAG(total_posts) OVER (
            ORDER BY month
        ) AS previous_month_posts

    FROM monthly_posts
)

SELECT
    month,
    total_posts,
    previous_month_posts,

    total_posts
        - previous_month_posts
        AS absolute_change,

    ROUND(
        100.0
        * (
            total_posts
            - previous_month_posts
        )
        / NULLIF(
            previous_month_posts,
            0
        ),
        2
    ) AS mom_growth_percent

FROM monthly_comparison

ORDER BY month;


-- =========================================================
-- 3. LEAD
--
-- Business question:
-- What is the next month's user-acquisition value?
--
-- LEAD looks forward instead of backward.
-- =========================================================

WITH monthly_users AS (
    SELECT
        DATE_TRUNC(
            'month',
            created_at
        )::date AS month,

        COUNT(*) AS new_users

    FROM v_analytics_users

    GROUP BY month
)

SELECT
    month,
    new_users,

    LEAD(new_users) OVER (
        ORDER BY month
    ) AS next_month_users,

    LEAD(new_users) OVER (
        ORDER BY month
    ) - new_users
        AS change_to_next_month

FROM monthly_users

ORDER BY month;


-- =========================================================
-- 4. RUNNING TOTAL
--
-- Business question:
-- How many posts had accumulated by each month?
-- =========================================================

WITH monthly_posts AS (
    SELECT
        DATE_TRUNC(
            'month',
            created_at
        )::date AS month,

        COUNT(*) AS monthly_posts

    FROM v_analytics_posts

    GROUP BY month
)

SELECT
    month,
    monthly_posts,

    SUM(monthly_posts) OVER (
        ORDER BY month
        ROWS BETWEEN
            UNBOUNDED PRECEDING
            AND CURRENT ROW
    ) AS cumulative_posts

FROM monthly_posts

ORDER BY month;


-- =========================================================
-- 5. 3-MONTH MOVING AVERAGE
--
-- Business question:
-- What does the short-term post trend look like
-- after smoothing monthly volatility?
-- =========================================================

WITH monthly_posts AS (
    SELECT
        DATE_TRUNC(
            'month',
            created_at
        )::date AS month,

        COUNT(*) AS monthly_posts

    FROM v_analytics_posts

    GROUP BY month
)

SELECT
    month,
    monthly_posts,

    ROUND(
        AVG(monthly_posts) OVER (
            ORDER BY month
            ROWS BETWEEN
                2 PRECEDING
                AND CURRENT ROW
        ),
        2
    ) AS moving_avg_3_months

FROM monthly_posts

ORDER BY month;


-- =========================================================
-- 6. NTILE
--
-- Business question:
-- Divide creators into 10 equal-size groups
-- based on number of posts.
--
-- Decile 1 = highest activity.
-- Decile 10 = lowest activity.
-- =========================================================

WITH creator_stats AS (
    SELECT
        u.id,
        u.name,
        COUNT(p.id) AS total_posts

    FROM v_analytics_users u

    LEFT JOIN v_analytics_posts p
        ON p.user_id = u.id

    GROUP BY
        u.id,
        u.name
),

creator_deciles AS (
    SELECT
        id,
        name,
        total_posts,

        NTILE(10) OVER (
            ORDER BY total_posts DESC
        ) AS activity_decile

    FROM creator_stats
)

SELECT
    activity_decile,

    COUNT(*) AS total_users,

    MIN(total_posts) AS min_posts,

    MAX(total_posts) AS max_posts,

    ROUND(
        AVG(total_posts),
        2
    ) AS avg_posts,

    SUM(total_posts) AS total_posts

FROM creator_deciles

GROUP BY activity_decile

ORDER BY activity_decile;


-- =========================================================
-- 7. PARETO / CUMULATIVE CONTENT CONTRIBUTION
--
-- Business question:
-- How quickly does content accumulate
-- as we move from highest to lowest creators?
-- =========================================================

WITH creator_stats AS (
    SELECT
        u.id,
        u.name,
        COUNT(p.id) AS total_posts

    FROM v_analytics_users u

    LEFT JOIN v_analytics_posts p
        ON p.user_id = u.id

    GROUP BY
        u.id,
        u.name
),

ranked_creators AS (
    SELECT
        id,
        name,
        total_posts,

        ROW_NUMBER() OVER (
            ORDER BY
                total_posts DESC,
                id
        ) AS creator_position,

        SUM(total_posts) OVER (
            ORDER BY
                total_posts DESC,
                id

            ROWS BETWEEN
                UNBOUNDED PRECEDING
                AND CURRENT ROW
        ) AS cumulative_posts,

        SUM(total_posts) OVER ()
            AS all_posts

    FROM creator_stats
)

SELECT
    creator_position,
    id,
    name,
    total_posts,
    cumulative_posts,

    ROUND(
        100.0
        * cumulative_posts
        / NULLIF(
            all_posts,
            0
        ),
        2
    ) AS cumulative_content_percent

FROM ranked_creators

WHERE creator_position <= 30

ORDER BY creator_position;


-- =========================================================
-- 8. FIRST POST RANK PER USER
--
-- Business question:
-- In what order did each user's posts occur?
--
-- This introduces PARTITION BY.
-- =========================================================

SELECT
    user_id,
    id AS post_id,
    status,
    created_at,

    ROW_NUMBER() OVER (
        PARTITION BY user_id
        ORDER BY created_at
    ) AS post_number_for_user

FROM v_analytics_posts

ORDER BY
    user_id,
    post_number_for_user

LIMIT 100;