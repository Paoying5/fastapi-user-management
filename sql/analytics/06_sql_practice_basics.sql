-- ==========================================
-- 01. DATABASE EXPLORATION
-- ==========================================

-- Check current database

SELECT
    current_database();


-- Check total users

SELECT
    COUNT(*) AS total_users
FROM users;


-- Check total posts

SELECT
    COUNT(*) AS total_posts
FROM posts;

-- Bài mới: Xem email của 5 User
SELECT email
FROM users
LIMIT 5;

--- Lấy 5 User, sắp xếp theo ID tăng dần.
SELECT
    id,
    name,
    email
FROM users
ORDER BY id ASC
LIMIT 5;


-- Tìm 10 tài khoản User đang bị vô hiệu hóa.
SELECT
    id,
    name,
    email,
    is_active
FROM users
WHERE is_active = FALSE
ORDER BY id ASC
LIMIT 10;

-- Tìm 10 tài khoản Admin.
SELECT
    id,
    name,
    email,
    role
FROM users
WHERE role = 'admin'
ORDER BY id ASC
LIMIT 10;

--- Tìm những tài khoản vừa có quyền Admin vừa đang hoạt động.

SELECT
    id,
    name,
    email,
    role,
    is_active
FROM users
WHERE role = 'admin'
AND is_active = TRUE
ORDER BY id ASC
LIMIT 10;

--- Thống kê hệ thống có bao nhiêu User theo từng Role.

SELECT
    role,
    COUNT(*) AS total_users
FROM users
GROUP BY role
ORDER BY total_users DESC;


SELECT
    status,
    COUNT(*) AS total_posts
FROM posts
GROUP BY status
ORDER BY total_posts DESC;
