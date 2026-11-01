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