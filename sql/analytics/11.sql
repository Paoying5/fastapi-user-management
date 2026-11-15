---Hiển thị bài viết cùng thông tin tác giả
SELECT
    posts.id AS post_id,
    posts.title AS post_title,
    users.id AS author_id,
    users.name AS author_name,
    users.email AS author_email
FROM posts
INNER JOIN users
    ON posts.user_id = users.id
ORDER BY post_id ASC
LIMIT 30;

--Đếm số bài viết của từng người dùng
SELECT
    users.id AS user_id,
    users.name,
    COUNT(posts.id) AS total_posts
FROM users
LEFT JOIN posts
    ON users.id = posts.user_id
GROUP BY users.id, users.name
ORDER BY total_posts DESC, user_id ASC
LIMIT 30;

---Tìm người dùng chưa có bài viết
SELECT
    users.id,
    users.name,
    users.email
FROM users
LEFT JOIN posts
    ON users.id = posts.user_id
WHERE posts.id IS NULL
ORDER BY users.id ASC
LIMIT 30;

--- Người dùng có ít nhất 3 bài viết đã xuất bản
SELECT
    users.id AS user_id,
    users.name,
    COUNT(posts.id) AS published_posts
FROM users
INNER JOIN posts
    ON users.id = posts.user_id
WHERE posts.status = 'published'
GROUP BY users.id, users.name
HAVING COUNT(posts.id) >= 3
ORDER BY published_posts DESC, user_id ASC;

--- Đếm bài viết theo vai trò và trạng thái
SELECT
    users.role,
    posts.status,
    COUNT(posts.id) AS total_posts
FROM users
INNER JOIN posts
    ON users.id = posts.user_id
GROUP BY users.role, posts.status
ORDER BY users.role ASC, total_posts DESC;

--- Tính trung bình số bài viết theo vai trò
SELECT
    role,
    COUNT(*) AS total_users,
    ROUND(AVG(user_posts), 2) AS average_posts_per_user
FROM (
    SELECT
        users.id,
        users.role,
        COUNT(posts.id) AS user_posts
    FROM users
    LEFT JOIN posts
        ON users.id = posts.user_id
    GROUP BY users.id, users.role
) AS user_statistics
GROUP BY role
ORDER BY average_posts_per_user DESC;


SELECT
    users.id,
    users.role,
    COUNT(posts.id) AS user_posts
FROM users
LEFT JOIN posts
    ON users.id = posts.user_id
GROUP BY users.id, users.role


SELECT
    role,
    COUNT(*) AS total_users,
    ROUND(AVG(user_posts), 2) AS average_posts_per_user
FROM (...) AS user_statistics
GROUP BY role;


--- Người dùng có số bài viết cao hơn trung bình
WITH user_post_counts AS (
    SELECT
        users.id AS user_id,
        users.name,
        COUNT(posts.id) AS total_posts
    FROM users
    LEFT JOIN posts
        ON users.id = posts.user_id
    GROUP BY users.id, users.name
),
average_posts AS (
    SELECT AVG(total_posts) AS avg_posts
    FROM user_post_counts
)
SELECT
    user_post_counts.user_id,
    user_post_counts.name,
    user_post_counts.total_posts
FROM user_post_counts
CROSS JOIN average_posts
WHERE user_post_counts.total_posts > average_posts.avg_posts
ORDER BY total_posts DESC, user_id ASC;


--- Tìm bài viết mới nhất của từng người dùng
WITH ranked_posts AS (
    SELECT
        user_id,
        id AS post_id,
        title,
        created_at,
        ROW_NUMBER() OVER (
            PARTITION BY user_id
            ORDER BY created_at DESC, id DESC
        ) AS row_num
    FROM posts
)
SELECT
    user_id,
    post_id,
    title,
    created_at
FROM ranked_posts
WHERE row_num = 1
ORDER BY user_id ASC;

---- Xếp hạng người dùng theo số bài viết
WITH user_post_counts AS (
    SELECT
        users.id AS user_id,
        users.name,
        COUNT(posts.id) AS total_posts
    FROM users
    LEFT JOIN posts
        ON users.id = posts.user_id
    GROUP BY users.id, users.name
)
SELECT
    user_id,
    name,
    total_posts,
    DENSE_RANK() OVER (
        ORDER BY total_posts DESC
    ) AS creator_rank
FROM user_post_counts
ORDER BY creator_rank ASC, user_id ASC
LIMIT 30;

--- Thống kê số bài viết theo tháng

SELECT
    DATE_TRUNC('month', created_at) AS month,
    COUNT(*) AS total_posts
FROM posts
GROUP BY DATE_TRUNC('month', created_at)
ORDER BY month ASC;

---Tính tổng bài viết tích lũy theo tháng
WITH monthly_posts AS (
    SELECT
        DATE_TRUNC('month', created_at) AS month,
        COUNT(*) AS monthly_posts
    FROM posts
    GROUP BY DATE_TRUNC('month', created_at)
)
SELECT
    month,
    monthly_posts,
    SUM(monthly_posts) OVER (
        ORDER BY month ASC
    ) AS cumulative_posts
FROM monthly_posts
ORDER BY month ASC;

---Tính tỷ lệ phần trăm bài viết theo trạng thái
WITH status_counts AS (
    SELECT
        status,
        COUNT(*) AS total_posts
    FROM posts
    GROUP BY status
)
SELECT
    status,
    total_posts,
    ROUND(
        total_posts * 100.0 / SUM(total_posts) OVER (),
        2
    ) AS percentage
FROM status_counts
ORDER BY total_posts DESC;

--- 