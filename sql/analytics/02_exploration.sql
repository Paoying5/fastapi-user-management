-- =========================================================
-- DATA ANALYST PHASE 1
-- EXPLORATORY SQL ANALYSIS
-- =========================================================


-- =========================================================
-- 1. ANALYTICS USERS VIEW
-- =========================================================

CREATE OR REPLACE VIEW v_analytics_users AS
SELECT *
FROM users
WHERE email LIKE
    'analytics\_user\_%@example.com'
    ESCAPE '\';


-- =========================================================
-- 2. ANALYTICS POSTS VIEW
-- =========================================================

CREATE OR REPLACE VIEW v_analytics_posts AS
SELECT
    p.*
FROM posts p
JOIN v_analytics_users u
    ON u.id = p.user_id;


-- =========================================================
-- 3. BASIC DATASET SIZE
-- =========================================================

SELECT
    COUNT(*) AS total_users
FROM v_analytics_users;


SELECT
    COUNT(*) AS total_posts
FROM v_analytics_posts;


-- =========================================================
-- 4. CORE ENGAGEMENT KPIs
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

    COUNT(*) FILTER (
        WHERE post_count = 0
    ) AS non_posting_users,

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

    ROUND(
        AVG(post_count) FILTER (
            WHERE post_count > 0
        ),
        2
    ) AS avg_posts_per_posting_user

FROM user_post_counts;


-- =========================================================
-- 5. POST STATUS DISTRIBUTION
-- =========================================================

SELECT
    status,
    COUNT(*) AS total_posts,

    ROUND(
        100.0 * COUNT(*)
        / SUM(COUNT(*)) OVER (),
        2
    ) AS percentage

FROM v_analytics_posts

GROUP BY status

ORDER BY total_posts DESC;


-- =========================================================
-- 6. USER SEGMENTATION
-- =========================================================

WITH user_posts AS (
    SELECT
        u.id,
        COUNT(p.id) AS post_count

    FROM v_analytics_users u

    LEFT JOIN v_analytics_posts p
        ON p.user_id = u.id

    GROUP BY u.id
),

segments AS (
    SELECT
        id,
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

    FROM user_posts
)

SELECT
    user_segment,
    COUNT(*) AS total_users,

    ROUND(
        100.0 * COUNT(*)
        / SUM(COUNT(*)) OVER (),
        2
    ) AS percentage

FROM segments

GROUP BY user_segment

ORDER BY total_users DESC;


-- =========================================================
-- 7. ROLE DISTRIBUTION
-- =========================================================

SELECT
    role,
    COUNT(*) AS total_users,

    ROUND(
        100.0 * COUNT(*)
        / SUM(COUNT(*)) OVER (),
        2
    ) AS percentage

FROM v_analytics_users

GROUP BY role

ORDER BY total_users DESC;


-- =========================================================
-- 8. ACTIVE / INACTIVE DISTRIBUTION
-- =========================================================

SELECT
    is_active,
    COUNT(*) AS total_users,

    ROUND(
        100.0 * COUNT(*)
        / SUM(COUNT(*)) OVER (),
        2
    ) AS percentage

FROM v_analytics_users

GROUP BY is_active

ORDER BY is_active DESC;


-- =========================================================
-- 9. TOP 10 CONTENT CREATORS
-- =========================================================

SELECT
    u.id,
    u.name,
    u.role,
    u.is_active,
    COUNT(p.id) AS total_posts

FROM v_analytics_users u

LEFT JOIN v_analytics_posts p
    ON p.user_id = u.id

GROUP BY
    u.id,
    u.name,
    u.role,
    u.is_active

ORDER BY
    total_posts DESC,
    u.id

LIMIT 10;


-- =========================================================
-- 10. MONTHLY USER REGISTRATIONS
-- =========================================================

SELECT
    DATE_TRUNC(
        'month',
        created_at
    )::date AS month,

    COUNT(*) AS new_users

FROM v_analytics_users

GROUP BY month

ORDER BY month;


-- =========================================================
-- 11. MONTHLY POST ACTIVITY
-- =========================================================

SELECT
    DATE_TRUNC(
        'month',
        created_at
    )::date AS month,

    COUNT(*) AS total_posts

FROM v_analytics_posts

GROUP BY month

ORDER BY month;


-- =========================================================
-- 12. ACTIVE VS INACTIVE ENGAGEMENT
-- =========================================================

SELECT
    u.is_active,

    COUNT(DISTINCT u.id)
        AS total_users,

    COUNT(p.id)
        AS total_posts,

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