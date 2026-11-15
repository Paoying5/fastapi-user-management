--- tìm người dùng mới đăng ký trong 30 ngày
select id, name, email, created_at
from users
where is_active = TRUE
    and created_at >= NOW() - INTERVAL '30 DAY'
order by created_at desc,id desc
limit 20;
----Tìm người chưa từng đăng nhập
SELECT id, name, email, last_login_at
FROM users
WHERE last_login_at IS NULL
ORDER BY id ASC
LIMIT 30;
---- Tìm email có đuôi @example.com
SELECT id, name, email
FROM users
WHERE email ILIKE '%@example.com'
ORDER BY email ASC
LIMIT 30;
-------Tìm theo tên HOẶC email
SELECT id, name, email
FROM users
WHERE name ILIKE '%admin%'
   OR email ILIKE '%admin%'
ORDER BY id ASC
LIMIT 30;
-------Tìm bài viết Draft hoặc Archived
SELECT id, title, user_id, status, created_at
FROM posts
WHERE status IN ('draft', 'archived')
ORDER BY created_at DESC
LIMIT 30;
---------- Tìm bài viết đã xuất bản trong 7 ngày
SELECT id, title, user_id, created_at
FROM posts
WHERE status = 'published'
  AND created_at >= NOW() - INTERVAL '7 days'
ORDER BY created_at DESC
LIMIT 30;
--Người dùng không hoạt động HOẶC chưa đăng nhập
SELECT id, name, email, is_active, last_login_at
FROM users
WHERE is_active = FALSE
   OR last_login_at IS NULL
ORDER BY id ASC
LIMIT 30;
---- Tìm bài viết có tiêu đề chứa analytics
SELECT id, title, user_id, status
FROM posts
WHERE title ILIKE '%analytics%'
ORDER BY title ASC, id ASC
LIMIT 30;