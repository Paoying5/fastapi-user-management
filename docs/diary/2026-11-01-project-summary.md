# FastAPI User Management — Current Project Summary

**Review date:** 2026-11-01  
**Evidence baseline:** latest supplied `project_context.md` export  
**Status:** source/documentation review; no fresh full test run or PostgreSQL migration run

---

## 1. Project direction

The project has evolved from a FastAPI user-management backend into a learning and portfolio project connecting:

```text
Backend Engineering
        +
PostgreSQL / Database Design
        +
SQL Analytics
        +
Python / Pandas / NumPy
        +
Visualization and Dashboard
```

FastAPI feature development was recorded as frozen at the 2026-10-18 milestone. The next priority should be analytical correctness, testability, and evidence-backed documentation rather than adding unrelated backend infrastructure.

---

## 2. Backend architecture

```text
Client
  ↓
FastAPI Router
  ↓
Service
  ↓
Repository
  ↓
SQLAlchemy ORM
  ↓
PostgreSQL
```

The source contains separate modules for configuration, database sessions, User/Post models, Pydantic schemas, repositories, services, routers, authentication dependencies, pagination, response helpers, and exception handling.

Main API areas:

| Area | Source-backed behavior |
|---|---|
| Authentication | Login, current-user access, JWT |
| Users | Create, list, retrieve, replace, patch, delete |
| Posts | Create, list, retrieve, current-user posts, replace, patch, delete |
| Analytics | Admin-protected User summary endpoint |
| Health | Health endpoint and database status |

User listing supports name/email search and pagination. Post listing supports title search and pagination. Post update/delete operations include ownership checks in the service layer.

---

## 3. Authentication and authorization

The source uses `pwdlib` password hashing and JWT access tokens.

The current token subject is the string representation of `user.id`. The current-user dependency checks the database state and rejects inactive accounts, including requests made with a token issued before deactivation.

Role values are constrained to:

```text
user
admin
```

Administrative endpoints use the admin dependency.

---

## 4. Database schema and migrations

The source migration chain is:

```text
e7d9b8aad922
      ↓
b31f9c2a6d10
      ↓
c42a7f91d8e3
```

### User fields

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

Allowed roles:

```text
user
admin
```

### Post fields

```text
id
title
content
user_id
status
created_at
updated_at
```

Allowed statuses:

```text
draft
published
archived
```

The model and migration source define role and Post-status CHECK constraints. Integration test source checks migration head, expected tables, lifecycle columns, and constraints. This audit did not connect to the user's PostgreSQL database to confirm its current revision.

---

## 5. Testing

The 2026-10-18 diary records:

```text
79 passed
```

That is a historical result, not a current test result.

The current exported test source contains 83 `test_` function definitions by static AST inspection:

| Area | Definitions |
|---|---:|
| API | 54 |
| Integration | 11 |
| E2E | 9 |
| Unit | 9 |
| Total | 83 |

This count is not equivalent to pytest collection or passing tests. `pytest --collect-only -q` could not run in the audit environment because `python-jose` (`jose`) was not installed. Python `compileall` completed successfully.

The current source contains API, unit, PostgreSQL integration, Alembic migration, and Playwright/Swagger E2E test modules.

---

## 6. Python Analytics

The source contains:

```text
analytics/
├── user_analysis.py
├── post_analysis.py
└── charts.py
```

### User Analytics

- User DataFrame extraction;
- total User count;
- User counts grouped by Role;
- empty DataFrame handling in `users_by_role()`;
- null Role grouping as `unknown`.

### Post Analytics

- Post DataFrame extraction;
- Post counts per User;
- Post statistics;
- User/Post left merge;
- top Users by Post count;
- Post counts by Role.

### Visualization

- Users by Role bar chart;
- age distribution histogram helper;
- top Users by Post count chart.

### Current Analytics API

```text
GET /analytics/users/summary
```

The endpoint is admin-protected and returns:

- total users;
- users by role.

The API test source covers 401, 403, and 200 access scenarios.

### Important code-review findings

1. `get_users_dataframe()` uses `select(User)`, which loads the entire User ORM entity, including `password`, even though the output DataFrame omits it.
2. `get_posts_dataframe()` returns a DataFrame with no columns when there are no Posts.
3. `posts_per_user()`, `calculate_post_statistics()`, and `merge_users_posts()` fail on that empty Post DataFrame with `KeyError: 'user_id'`.
4. `calculate_post_statistics()` averages only across users with at least one Post. Its `average_posts_per_user` key is misleading.
5. Post DataFrame output omits lifecycle fields (`status`, `created_at`, `updated_at`).
6. The age chart requires an `age` column, but the current User model has no age field.
7. The Analytics helper/chart modules have no dedicated test module in the current export.

---

## 7. Synthetic analytics dataset

The W25 diary and root README document:

```text
600 synthetic users
2,250 synthetic posts
```

The W25 diary records:

```text
Posting rate:                  80.00%
Average posts / user:           3.75
Average posts / posting user:   4.69

Published: 70%
Draft:     20%
Archived:  10%
```

These values describe a synthetic practice dataset, not production-user behavior. The underlying seed/query files are not included in the current export, so they were not independently re-executed during this review.

---

## 8. KPI 7 and Dashboard — README-documented state

The root README documents KPI 7:

| Metric | README value |
|---|---:|
| Total users | 600 |
| Total posts | 2,250 |
| Posts attributed to top 10% creator group | 870 |
| Top-creator post share | 38.67% |
| Stated verification date | 2026-10-25 |

The arithmetic is correct:

```text
870 / 2,250 × 100 = 38.67%
```

However, the SQL query and JSON snapshot were not included in the export. The values remain README-documented, not independently source-verified.

The root README also describes a Next.js dashboard, JSON snapshots, a synchronization script, and Vercel deployment. The actual frontend source and package manifest were not included in the export, so the dashboard was not re-tested.

The README says the dashboard is snapshot-based, not a live PostgreSQL dashboard.

---

## 9. Documentation/export limitations

The project-context exporter currently allows only:

```text
.py, .md, .txt, .ini, .yml, .yaml, .sh, .dockerfile
```

It excludes SQL, JSON, JavaScript, TypeScript, and TSX files. Therefore, the exported count of 139 files is not necessarily the total repository file count.

This is the main reason the SQL/KPI/dashboard implementation cannot yet be checked line by line.

The root README also uses `uvicorn main:app --reload`, while the actual application module is `app/main.py` and the Dockerfile uses `uvicorn app.main:app`. The README command should be corrected.

---

## 10. Recommended next steps

1. Extend `export_project.py` to include `.sql`, `.json`, `.js`, `.mjs`, `.ts`, `.tsx`, and relevant frontend assets, while excluding generated/dependency directories.
2. Export the SQL analytics queries and KPI/monthly JSON snapshots.
3. Export `mentor-web/package.json`, scripts, and `src/` implementation.
4. Fix empty-Post DataFrame behavior and add tests.
5. Select only required User columns in `get_users_dataframe()`.
6. Clarify the average-post denominator and return both population-level metrics if needed.
7. Add direct tests for Post Analytics and chart helpers.
8. Re-run pytest and record the actual collected/pass/fail/skip counts.
9. Correct the root README Uvicorn command and update the dashboard README from the actual implementation.
