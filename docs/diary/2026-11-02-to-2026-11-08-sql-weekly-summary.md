# W28 Weekly Report — SQL PostgreSQL Restart

**Period:** 2026-11-02 → 2026-11-08  
**Project:** FastAPI User Management  
**Main focus:** Resume SQL practice on the project's PostgreSQL database  
**Record type:** Weekly retrospective based on the learner's report, supplied Terminal output, and the latest project snapshot

## 1. Summary

This week was not seven full days of SQL practice. The learner reported taking a break from coding for approximately one week and resumed on Sunday, 2026-11-08.

The confirmed work this week was mainly environment recovery, PostgreSQL schema inspection, and introductory queries. The learner is still at the SQL fundamentals stage and needs guided practice to become more independent.

## 2. What was actually completed or verified

- Rebuilt and started the Docker Compose environment with `docker compose up --build -d`.
- Checked running services using `docker compose ps`; the API reported `healthy` and PostgreSQL was running.
- Connected to `fastapi_db` through `psql`.
- Inspected the real schemas of `users` and `posts`, including keys and CHECK constraints.
- Confirmed the current database name as `fastapi_db`.
- Executed row-count queries and observed 784 Users and 2,363 Posts in the current local database.
- Executed simple `SELECT ... LIMIT` queries to retrieve a small number of User names and email values.
- Reviewed the current contents of `06_sql_practice_basics.sql` and `07_sql_fundamentals_practice.sql`.

## 3. Database results observed on 2026-11-08

| Query | Observed result |
|---|---:|
| `SELECT current_database()` | `fastapi_db` |
| `SELECT COUNT(*) FROM users` | 784 |
| `SELECT COUNT(*) FROM posts` | 2,363 |
| `SELECT name FROM users LIMIT 3` | 3 rows |
| `SELECT email FROM users LIMIT 5` | 5 rows |

These are results from the local Docker database at the time of the supplied Terminal output. They should not be confused with the separate synthetic analytics dataset documented as 600 Users and 2,250 Posts in the KPI materials.

## 4. Main difficulties

- After the break, the learner struggled to translate a task description and hints into a complete SQL query.
- The learner recognized an over-reliance on copied code and wants to rebuild the habit of reasoning before writing.
- `docker compose status` was attempted, but the installed CLI uses `docker compose ps` to list services.
- An incorrect SQL filename was used initially; the directory listing helped identify the actual file names.
- Explanatory text was placed on the same line as `psql` backslash commands, causing `psql` to interpret it as extra arguments.

## 5. What was learned

- A SQL task can be broken down into: source table → selected columns → filter conditions → sort order → row limit.
- `SELECT` chooses columns, `FROM` chooses the table, `COUNT(*)` counts rows, and `LIMIT` caps the returned rows.
- `ORDER BY` is needed when a task requires a deterministic order such as the first or latest records.
- PostgreSQL `psql` meta-commands such as `\d` and `\dt` are different from SQL statements.
- A query appearing in a source file is not the same as a query being executed, checked, and understood.

## 6. Current level and remaining gaps

The learner can connect to the database, inspect schemas, and run simple selection/counting queries with support.

The learner is not yet able to reliably write a complete query independently from a plain-language exercise. `WHERE`, `ORDER BY`, and `GROUP BY` appear in the current practice source, but the available runtime evidence does not confirm that every such query has been independently executed and understood.

`JOIN`, `HAVING`, CTE, and Window Functions remain future practice topics for this learning cycle.

## 7. Plan for the next week

1. Rebuild `SELECT`, `FROM`, `ORDER BY`, and `LIMIT` through short exercises.
2. Practice `WHERE`, `AND`, `OR`, `IN`, `LIKE`, and `IS NULL`.
3. Practice `COUNT`, `GROUP BY`, and `HAVING`.
4. Learn `INNER JOIN` and `LEFT JOIN` using the `users` and `posts` relationship.
5. Write a small set of queries without copying complete solutions.
6. Record the query, output, error (if any), and explanation in the SQL practice file.

## 8. Mentor-facing note

The backend project already provides a real PostgreSQL schema and data source for SQL practice. The immediate priority is not to add more advanced queries, but to strengthen the learner's ability to reason from a business question and write a correct query independently.

This report intentionally distinguishes confirmed runtime results from SQL statements that are only present in the source files.
