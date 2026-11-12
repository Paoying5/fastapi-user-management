
-- Bài 1: Lấy tên của 3 User
SELECT name
FROM users
LIMIT 3;

-- Bài 2: Lấy email của 3 User
SELECT email
FROM users
LIMIT 3;

-- Bài 3: Lấy ID, tên và email của 5 User
SELECT
    id,
    name,
    email
FROM users
ORDER BY id ASC
LIMIT 5;


-- 1. Kiểm tra database
SELECT current_database();

-- 2. Tổng số users
SELECT COUNT(*) AS total_users
FROM users;

-- 3. Tổng số posts
SELECT COUNT(*) AS total_posts
FROM posts;

-- 4. Số analytics users
SELECT COUNT(*) AS analytics_users
FROM users
WHERE email LIKE
    'analytics\_user\_%@example.com'
    ESCAPE '\';

-- 5. Số analytics posts
SELECT COUNT(*) AS analytics_posts
FROM posts p
JOIN users u
    ON u.id = p.user_id
WHERE u.email LIKE
    'analytics\_user\_%@example.com'
    ESCAPE '\';


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
        100.0 *
        COUNT(*) FILTER (
            WHERE post_count > 0
        ) / COUNT(*),
        2
    ) AS posting_rate_percent,

    ROUND(
        AVG(post_count),
        2
    ) AS avg_posts_per_user

FROM user_post_counts;