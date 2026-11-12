-- SOLUTIONS - MODULE 01
-- Try the challenges before reading these solutions.

-- CHALLENGE 01 - FIND ACTIVE USERS
SELECT id, name, email
FROM users
WHERE is_active IS TRUE
ORDER BY id ASC
LIMIT 10;

-- CHALLENGE 02 - FIND INACTIVE USERS
SELECT id, name, email, is_active
FROM users
WHERE is_active IS FALSE
ORDER BY id ASC
LIMIT 10;

-- CHALLENGE 03 - FIND ADMIN ACCOUNTS
SELECT id, name, email, role
FROM users
WHERE role = 'admin'
ORDER BY id ASC
LIMIT 10;

-- CHALLENGE 04 - FIND ACTIVE ADMIN ACCOUNTS
SELECT id, name, email, role, is_active
FROM users
WHERE role = 'admin'
  AND is_active IS TRUE
ORDER BY id ASC
LIMIT 10;

-- CHALLENGE 05 - USERS WITHOUT FULL NAME
SELECT id, name, email, full_name
FROM users
WHERE full_name IS NULL
ORDER BY id ASC
LIMIT 20;

-- CHALLENGE 06 - LATEST POSTS
SELECT id, title, user_id, status, created_at
FROM posts
ORDER BY created_at DESC, id DESC
LIMIT 10;

-- CHALLENGE 07 - PUBLISHED POSTS
SELECT id, title, user_id, status
FROM posts
WHERE status = 'published'
ORDER BY id ASC
LIMIT 10;

-- CHALLENGE 08 - SEARCH USERS BY NAME
SELECT id, name, email
FROM users
WHERE name ILIKE '%admin%'
ORDER BY name ASC, id ASC
LIMIT 20;