-- =========================================================
-- DATA ANALYST PHASE 2
-- BUSINESS KPI ANALYSIS
-- =========================================================


-- =========================================================
-- KPI 1
-- OVERALL PLATFORM ENGAGEMENT
-- =========================================================

WITH user_post_counts AS (
    SELECT
        u.id,
        COUNT(p.id) AS post_count

    FROM v_analytics_users u

    LEFT JOIN v_analytics_posts p
        ON p.user_id = u.id

    GROUP BY u.id
)

SELECT
    COUNT(*) AS total_users,

    COUNT(*) FILTER (
        WHERE post_count > 0
    ) AS posting_users,

    ROUND(
        100.0
        * COUNT(*) FILTER (
            WHERE post_count > 0
        )
        / COUNT(*),
        2
    ) AS posting_rate_percent,

    ROUND(
        AVG(post_count),
        2
    ) AS avg_posts_per_user,

    MAX(post_count) AS max_posts_per_user

FROM user_post_counts;


-- =========================================================
-- KPI 2
-- ACTIVE VS INACTIVE USER ENGAGEMENT
-- =========================================================

SELECT
    u.is_active,

    COUNT(DISTINCT u.id)
        AS total_users,

    COUNT(p.id)
        AS total_posts,

    COUNT(DISTINCT p.user_id)
        AS posting_users,

    ROUND(
        100.0
        * COUNT(DISTINCT p.user_id)
        / COUNT(DISTINCT u.id),
        2
    ) AS posting_rate_percent,

    ROUND(
        COUNT(p.id)::numeric
        / NULLIF(
            COUNT(DISTINCT u.id),
            0
        ),
        2
    ) AS avg_posts_per_user

FROM v_analytics_users u

LEFT JOIN v_analytics_posts p
    ON p.user_id = u.id

GROUP BY u.is_active

ORDER BY u.is_active DESC;


-- =========================================================
-- KPI 3
-- MONTHLY USER ACQUISITION + MOM GROWTH
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
),

with_previous AS (
    SELECT
        month,
        new_users,

        LAG(new_users) OVER (
            ORDER BY month
        ) AS previous_month_users

    FROM monthly_users
)

SELECT
    month,
    new_users,
    previous_month_users,

    ROUND(
        100.0
        * (
            new_users
            - previous_month_users
        )
        / NULLIF(
            previous_month_users,
            0
        ),
        2
    ) AS mom_growth_percent

FROM with_previous

ORDER BY month;


-- =========================================================
-- KPI 4
-- MONTHLY POST ACTIVITY + MOM GROWTH
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

with_previous AS (
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

FROM with_previous

ORDER BY month;


-- =========================================================
-- KPI 5
-- MONTHLY POST STATUS MIX
-- =========================================================

SELECT
    DATE_TRUNC(
        'month',
        created_at
    )::date AS month,

    COUNT(*) AS total_posts,

    COUNT(*) FILTER (
        WHERE status = 'published'
    ) AS published_posts,

    COUNT(*) FILTER (
        WHERE status = 'draft'
    ) AS draft_posts,

    COUNT(*) FILTER (
        WHERE status = 'archived'
    ) AS archived_posts,

    ROUND(
        100.0
        * COUNT(*) FILTER (
            WHERE status = 'published'
        )
        / COUNT(*),
        2
    ) AS published_rate_percent

FROM v_analytics_posts

GROUP BY month

ORDER BY month;


-- =========================================================
-- KPI 6
-- CONTENT CREATOR RANKING
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

    RANK() OVER (
        ORDER BY total_posts DESC
    ) AS creator_rank

FROM creator_stats

ORDER BY
    creator_rank,
    id

LIMIT 20;


-- =========================================================
-- KPI 7
-- TOP 10% CREATOR CONTENT CONTRIBUTION
-- =========================================================

WITH creator_stats AS (
    SELECT
        u.id,
        COUNT(p.id) AS total_posts

    FROM v_analytics_users u

    LEFT JOIN v_analytics_posts p
        ON p.user_id = u.id

    GROUP BY u.id
),

ranked_creators AS (
    SELECT
        id,
        total_posts,

        NTILE(10) OVER (
            ORDER BY total_posts DESC
        ) AS creator_decile

    FROM creator_stats
)

SELECT
    SUM(total_posts) FILTER (
        WHERE creator_decile = 1
    ) AS top_10_percent_posts,

    SUM(total_posts)
        AS all_posts,

    ROUND(
        100.0
        * SUM(total_posts) FILTER (
            WHERE creator_decile = 1
        )
        / NULLIF(
            SUM(total_posts),
            0
        ),
        2
    ) AS top_10_percent_content_share

FROM ranked_creators;


-- =========================================================
-- KPI 8
-- MONTHLY ACTIVE CREATORS
-- Active creator = user created >= 1 post in month
-- =========================================================

SELECT
    DATE_TRUNC(
        'month',
        created_at
    )::date AS month,

    COUNT(
        DISTINCT user_id
    ) AS active_creators,

    COUNT(*) AS total_posts,

    ROUND(
        COUNT(*)::numeric
        / NULLIF(
            COUNT(DISTINCT user_id),
            0
        ),
        2
    ) AS posts_per_active_creator

FROM v_analytics_posts

GROUP BY month

ORDER BY month;