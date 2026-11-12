# Development Diary — SQL Practice Resumption

**Date:** 2026-11-08  
**Weekly report:** W28 (2026-11-02 → 2026-11-08)  
**Record type:** Daily entry based on commands and results supplied in the conversation

## 1. Goal

Resume SQL practice after a break and verify that the FastAPI User Management PostgreSQL environment is available.

The focus for this session was basic database inspection and simple data retrieval. This was a restart session, not evidence of SQL mastery.

## 2. Environment verification

The learner ran:

```bash
docker compose up --build -d
docker compose ps
```

The supplied output showed:

- `fastapi-postgres` running;
- `fastapi-api` running and reporting `healthy`;
- PostgreSQL published on host port `5433` and container port `5432`;
- API published on host port `8000`.

The learner also tried `docker compose status`. Docker Compose did not recognize that command. The working command used afterward was:

```bash
docker compose ps
```

## 3. PostgreSQL connection

The learner connected to the database using:

```bash
docker compose exec postgres psql -U admin -d fastapi_db
```

For running a SQL file from the project directory, the following command was used successfully:

```bash
docker compose exec -T postgres psql \
  -U admin \
  -d fastapi_db \
  -v ON_ERROR_STOP=1 \
  < sql/analytics/06_sql_practice_basics.sql
```

`-v ON_ERROR_STOP=1` makes `psql` stop when a SQL error occurs, which is useful when validating a practice script.

## 4. Schema inspection

The learner inspected the `users` and `posts` tables using `\d users` and `\d posts`.

### Users

The supplied schema output showed these columns:

```text
id
name
email
role
password
full_name
is_active
created_at
updated_at
last_login_at
```

The table also has:

- primary key on `id`;
- unique index on `email`;
- CHECK constraint allowing `user` and `admin`;
- a relationship referenced by `posts.user_id`.

### Posts

The supplied schema output showed:

```text
id
title
content
user_id
status
created_at
updated_at
```

The table also has:

- primary key on `id`;
- foreign key `user_id` referencing `users(id)`;
- CHECK constraint allowing `draft`, `published`, and `archived`.

This schema inspection is useful because SQL exercises should use real column names rather than guessed names.

## 5. Queries with runtime output confirmed

### 5.1 Check the current database

```sql
SELECT current_database();
```

Observed result:

```text
fastapi_db
```

### 5.2 Count Users

```sql
SELECT COUNT(*) AS total_users
FROM users;
```

Observed result:

```text
784
```

### 5.3 Count Posts

```sql
SELECT COUNT(*) AS total_posts
FROM posts;
```

Observed result:

```text
2363
```

### 5.4 Retrieve a small number of names

The learner ran a query equivalent to:

```sql
SELECT name
FROM users
LIMIT 3;
```

The output contained three rows:

```text
Admin Test
admin
Swagger E2E User
```

### 5.5 Retrieve a small number of email values

The learner ran:

```sql
SELECT email
FROM users
LIMIT 5;
```

The output contained five rows. The displayed values included:

```text
admin-test@example.com
admin@example.com
swagger-e2e@example.com
swagger-login-9385dc64@example.com
swagger-login-efc77fce@example.com
```

**Important:** These two `LIMIT` queries did not include `ORDER BY`. The displayed row order is the observed output from that execution; SQL does not guarantee a stable order without an explicit sort.

## 6. Existing practice files reviewed

The latest project snapshot contains:

### `06_sql_practice_basics.sql`

The file currently includes examples for database inspection, row counts, `SELECT`, `WHERE`, `ORDER BY`, and `GROUP BY`.

Runtime output was supplied for the database check, counts, and simple name/email retrieval. The available evidence does not confirm that every later statement in the current file was executed.

### `07_sql_fundamentals_practice.sql`

The file contains three introductory exercises:

1. select the names of three Users;
2. select the emails of three Users;
3. select ID, name, and email for five Users ordered by ID.

The source file is present in the snapshot. A separate execution result for all three exercises was not supplied.

### Files not treated as completed this week

The project also contains SQL analytics files for exploration, KPI analysis, business questions, and window functions. Their presence in the repository does not mean those topics were studied or independently completed during this session.

## 7. Problems encountered and lessons

### Docker Compose command

`docker compose status` was not a valid command in the installed Docker Compose CLI. `docker compose ps` was used to inspect running services.

### Incorrect SQL file path

An attempted command referenced a file named `04_sql_fundamentals_practice.sql`, which did not exist in `sql/analytics/`. Listing the directory showed the actual filenames. The correct practice files were `06_sql_practice_basics.sql` and `07_sql_fundamentals_practice.sql`.

### `psql` meta-commands and comments

The learner placed explanatory text after backslash commands such as `\conninfo` and `\dt`. `psql` interpreted the trailing text as extra arguments and returned errors.

Lesson: `\conninfo`, `\dt`, and `\d users` are `psql` meta-commands, not ordinary SQL statements. Put explanatory comments on a separate line.

### Difficulty writing SQL independently

The learner reported that even when a task contains hints, they often cannot turn the hint into a complete SQL statement without asking for generated code.

This is recorded as the main learning gap. The next practice should require the learner to identify the table, columns, filters, sorting, and row limit before writing SQL.

## 8. Current learning assessment

| Topic | Status based on available evidence |
|---|---|
| Connect to PostgreSQL through Docker | Practiced |
| Inspect table schemas | Practiced |
| `SELECT` and `FROM` | Practiced with simple queries |
| `COUNT(*)` | Practiced |
| `LIMIT` | Practiced |
| `ORDER BY` | Present in practice source; independent execution not yet confirmed |
| `WHERE` | Present in practice source; independent execution not yet confirmed |
| `GROUP BY` | Present in practice source; independent execution not yet confirmed |
| `JOIN`, `HAVING`, CTE, Window Functions | Not demonstrated in this session |
| Write a complete query independently from a prompt | Still needs substantial practice |

Overall level: restarting the fundamentals. The learner is not yet confident writing SQL independently.

## 9. Next practice steps

1. Write a `SELECT` query from a plain-language prompt without copying a complete example.
2. Add `ORDER BY` and explain why it is needed when the task says “first” or “latest”.
3. Add `WHERE` to filter active/inactive Users.
4. Combine two conditions with `AND` and `OR`.
5. Group Users by role and Posts by status.
6. Only after these are understood, proceed to `HAVING` and `JOIN`.

The next session should save the learner's own query, the actual result, and a short explanation of each clause.
