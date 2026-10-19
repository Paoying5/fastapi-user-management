-- =========================================================
-- DATA ANALYST PHASE 3
-- BUSINESS QUESTIONS WITH SQL
-- =========================================================
--
-- Dataset:
--   v_analytics_users
--   v_analytics_posts
--
-- Goal:
--   Stop thinking only about SQL syntax.
--   Start answering business questions with data.
-- =========================================================


-- =========================================================
-- QUESTION 1
-- Which user role contributes more content?
-- =========================================================

SELECT
    u.role,

    COUNT(DISTINCT u.id) AS total_users,

    COUNT(p.id) AS total_posts,

    COUNT(DISTINCT p.user_id) AS posting_users,

    ROUND(
        COUNT(p.id)::numeric
        / NULLIF(
            COUNT(DISTINCT u.id),
            0
        ),
        2
    ) AS avg_posts_per_user,

    ROUND(
        100.0
        * COUNT(p.id)
        / NULLIF(
            SUM(COUNT(p.id)) OVER (),
            0
        ),
        2
    ) AS content_share_percent

FROM v_analytics_users u

LEFT JOIN v_analytics_posts p
    ON p.user_id = u.id

GROUP BY u.role

ORDER BY total_posts DESC;


-- =========================================================
-- QUESTION 2
-- How different is engagement between user segments?
-- =========================================================

WITH user_post_counts AS (
    SELECT
        u.id,
        u.role,
        u.is_active,
        COUNT(p.id) AS post_count

    FROM v_analytics_users u

    LEFT JOIN v_analytics_posts p
        ON p.user_id = u.id

    GROUP BY
        u.id,
        u.role,
        u.is_active
),

segmented_users AS (
    SELECT
        id,
        role,
        is_active,
        post_count,

        CASE
            WHEN post_count = 0
                THEN 'No posts'

            WHEN post_count = 1
                THEN '1 post'

            WHEN post_count BETWEEN 2 AND 5
                THEN '2-5 posts'

            WHEN post_count BETWEEN 6 AND 10
                THEN '6-10 posts'

            ELSE '11-20 posts'
        END AS user_segment

    FROM user_post_counts
)

SELECT
    user_segment,

    COUNT(*) AS total_users,

    ROUND(
        AVG(post_count),
        2
    ) AS avg_posts,

    MIN(post_count) AS min_posts,

    MAX(post_count) AS max_posts

FROM segmented_users

GROUP BY user_segment

ORDER BY avg_posts DESC;


-- =========================================================
-- QUESTION 3
-- What percentage of users in each role actually post?
-- =========================================================

WITH role_activity AS (
    SELECT
        u.role,
        u.id,

        CASE
            WHEN COUNT(p.id) > 0
                THEN 1
            ELSE 0
        END AS has_posted

    FROM v_analytics_users u

    LEFT JOIN v_analytics_posts p
        ON p.user_id = u.id

    GROUP BY
        u.role,
        u.id
)

SELECT
    role,

    COUNT(*) AS total_users,

    SUM(has_posted) AS posting_users,

    COUNT(*) - SUM(has_posted)
        AS non_posting_users,

    ROUND(
        100.0
        * SUM(has_posted)
        / COUNT(*),
        2
    ) AS posting_rate_percent

FROM role_activity

GROUP BY role

ORDER BY posting_rate_percent DESC;


-- =========================================================
-- QUESTION 4
-- Which registration cohorts are most engaged?
--
-- Cohort = month user registered.
-- Engagement = users who created at least one post.
-- =========================================================

WITH user_activity AS (
    SELECT
        u.id,

        DATE_TRUNC(
            'month',
            u.created_at
        )::date AS registration_month,

        COUNT(p.id) AS post_count

    FROM v_analytics_users u

    LEFT JOIN v_analytics_posts p
        ON p.user_id = u.id

    GROUP BY
        u.id,
        registration_month
)

SELECT
    registration_month,

    COUNT(*) AS registered_users,

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
    ) AS avg_posts_per_user

FROM user_activity

GROUP BY registration_month

ORDER BY registration_month;


-- =========================================================
-- QUESTION 5
-- Which users create a lot of content
-- but publish a relatively small percentage?
--
-- Business idea:
-- High creation + low publish rate may indicate
-- unfinished content or workflow friction.
-- =========================================================

WITH creator_status AS (
    SELECT
        u.id,
        u.name,

        COUNT(p.id) AS total_posts,

        COUNT(p.id) FILTER (
            WHERE p.status = 'published'
        ) AS published_posts,

        COUNT(p.id) FILTER (
            WHERE p.status = 'draft'
        ) AS draft_posts,

        COUNT(p.id) FILTER (
            WHERE p.status = 'archived'
        ) AS archived_posts

    FROM v_analytics_users u

    LEFT JOIN v_analytics_posts p
        ON p.user_id = u.id

    GROUP BY
        u.id,
        u.name
),

creator_rates AS (
    SELECT
        *,

        ROUND(
            100.0
            * published_posts
            / NULLIF(
                total_posts,
                0
            ),
            2
        ) AS published_rate_percent

    FROM creator_status
)

SELECT
    id,
    name,
    total_posts,
    published_posts,
    draft_posts,
    archived_posts,
    published_rate_percent

FROM creator_rates

WHERE total_posts >= 6

ORDER BY
    published_rate_percent ASC,
    total_posts DESC

LIMIT 15;


-- =========================================================
-- QUESTION 6
-- How much content comes from highly engaged users?
--
-- Highly engaged:
--   >= 6 posts
--
-- Moderate:
--   2-5 posts
--
-- Low:
--   1 post
--
-- Inactive creator:
--   0 posts
-- =========================================================

WITH user_post_counts AS (
    SELECT
        u.id,
        COUNT(p.id) AS post_count

    FROM v_analytics_users u

    LEFT JOIN v_analytics_posts p
        ON p.user_id = u.id

    GROUP BY u.id
),

engagement_groups AS (
    SELECT
        id,
        post_count,

        CASE
            WHEN post_count = 0
                THEN 'Inactive creator'

            WHEN post_count = 1
                THEN 'Low engagement'

            WHEN post_count BETWEEN 2 AND 5
                THEN 'Moderate engagement'

            ELSE 'High engagement'
        END AS engagement_group

    FROM user_post_counts
)

SELECT
    engagement_group,

    COUNT(*) AS total_users,

    SUM(post_count) AS total_posts,

    ROUND(
        100.0
        * SUM(post_count)
        / NULLIF(
            SUM(SUM(post_count)) OVER (),
            0
        ),
        2
    ) AS content_share_percent

FROM engagement_groups

GROUP BY engagement_group

ORDER BY total_posts DESC;