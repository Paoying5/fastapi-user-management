BEGIN;

-- Reproducible random values.
SELECT setseed(0.42);

-- =========================================================
-- CLEAN PREVIOUS ANALYTICS SEED ONLY
-- Không đụng vào test/dev data hiện tại.
-- =========================================================

DELETE FROM posts
WHERE user_id IN (
    SELECT id
    FROM users
    WHERE email LIKE 'analytics\_user\_%@example.com' ESCAPE '\'
);

DELETE FROM users
WHERE email LIKE 'analytics\_user\_%@example.com' ESCAPE '\';


-- =========================================================
-- SEED 600 ANALYTICS USERS
-- =========================================================

WITH password_source AS (
    SELECT password
    FROM users
    ORDER BY id
    LIMIT 1
),

generated_users AS (
    SELECT
        seq,

        NOW()
        - (
            random()
            * 300
            * 24
            * 60
            * 60
        ) * INTERVAL '1 second'
        AS created_at

    FROM generate_series(
        1,
        600
    ) AS seq
)

INSERT INTO users (
    name,
    email,
    role,
    password,
    full_name,
    is_active,
    created_at,
    updated_at,
    last_login_at
)

SELECT
    'Analytics User ' || seq,

    'analytics_user_'
        || LPAD(seq::text, 4, '0')
        || '@example.com',

    CASE
        WHEN seq % 20 = 0
            THEN 'admin'
        ELSE 'user'
    END,

    password_source.password,

    'Analytics User ' || seq,

    CASE
        WHEN seq % 10 = 0
            THEN false
        ELSE true
    END,

    created_at,

    LEAST(
        NOW(),

        created_at
        + (
            random()
            * EXTRACT(
                EPOCH FROM (
                    NOW() - created_at
                )
            )
        ) * INTERVAL '1 second'
    ),

    CASE
        WHEN seq % 7 = 0
            THEN NULL

        ELSE LEAST(
            NOW(),

            created_at
            + (
                random()
                * EXTRACT(
                    EPOCH FROM (
                        NOW() - created_at
                    )
                )
            ) * INTERVAL '1 second'
        )
    END

FROM generated_users
CROSS JOIN password_source;


-- =========================================================
-- CREATE USER BEHAVIOR SEGMENTS
--
-- mỗi nhóm 20 users:
-- 4 users  -> 0 posts
-- 5 users  -> 1 post
-- 7 users  -> 2–5 posts
-- 3 users  -> 6–10 posts
-- 1 user   -> 11–20 posts
-- =========================================================

WITH ranked_users AS (
    SELECT
        id,
        created_at,

        ROW_NUMBER() OVER (
            ORDER BY id
        ) AS rn

    FROM users

    WHERE email LIKE
        'analytics\_user\_%@example.com' ESCAPE '\'
),

user_post_counts AS (
    SELECT
        id,
        created_at,

        CASE
            WHEN rn % 20 IN (
                0, 1, 2, 3
            )
                THEN 0

            WHEN rn % 20 IN (
                4, 5, 6, 7, 8
            )
                THEN 1

            WHEN rn % 20 IN (
                9, 10, 11,
                12, 13, 14, 15
            )
                THEN 2 + (rn % 4)

            WHEN rn % 20 IN (
                16, 17, 18
            )
                THEN 6 + (rn % 5)

            ELSE
                11 + (rn % 10)
        END AS post_count

    FROM ranked_users
),

expanded_posts AS (
    SELECT
        u.id AS user_id,
        u.created_at AS user_created_at,
        gs.post_no

    FROM user_post_counts u

    JOIN LATERAL generate_series(
        1,
        u.post_count
    ) AS gs(post_no)
        ON true
),

prepared_posts AS (
    SELECT
        user_id,
        post_no,

        ROW_NUMBER() OVER (
            ORDER BY
                user_id,
                post_no
        ) AS post_seq,

        user_created_at
        + (
            random()
            * EXTRACT(
                EPOCH FROM (
                    NOW() - user_created_at
                )
            )
        ) * INTERVAL '1 second'
        AS post_created_at

    FROM expanded_posts
)

INSERT INTO posts (
    title,
    content,
    user_id,
    status,
    created_at,
    updated_at
)

SELECT
    'Analytics Post '
        || user_id
        || '-'
        || post_no,

    'Synthetic analytics content for user '
        || user_id
        || ', post '
        || post_no
        || '.',

    user_id,

    CASE
        WHEN post_seq % 10 = 0
            THEN 'archived'

        WHEN post_seq % 10 IN (
            1, 2
        )
            THEN 'draft'

        ELSE 'published'
    END,

    post_created_at,

    LEAST(
        NOW(),

        post_created_at
        + (
            random()
            * EXTRACT(
                EPOCH FROM (
                    NOW() - post_created_at
                )
            )
        ) * INTERVAL '1 second'
    )

FROM prepared_posts;


COMMIT;