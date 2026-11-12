-- SOLUTIONS - MODULE 02
-- Try the challenges before reading these solutions.

-- CHALLENGE 09 - COUNT USERS BY ROLE
SELECT
    role,
    COUNT(*) AS total_users
FROM users
GROUP BY role
ORDER BY total_users DESC, role ASC;

-- CHALLENGE 10 - COUNT POSTS BY STATUS
SELECT
    status,
    COUNT(*) AS total_posts
FROM posts
GROUP BY status
ORDER BY total_posts DESC, status ASC;

-- CHALLENGE 11 - TOTAL POSTS PER USER
SELECT
    u.id AS user_id,
    u.name,
    COUNT(p.id) AS total_posts
FROM users u
LEFT JOIN posts p
    ON p.user_id = u.id
GROUP BY u.id, u.name
ORDER BY total_posts DESC, u.id ASC
LIMIT 10;

-- CHALLENGE 12 - USERS WITH MORE THAN 5 POSTS
SELECT
    u.id AS user_id,
    u.name,
    COUNT(p.id) AS total_posts
FROM users u
INNER JOIN posts p
    ON p.user_id = u.id
GROUP BY u.id, u.name
HAVING COUNT(p.id) > 5
ORDER BY total_posts DESC, u.id ASC;