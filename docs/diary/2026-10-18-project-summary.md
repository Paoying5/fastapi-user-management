# FastAPI User Management — Current Project Summary

**Updated:** 2026-10-18

## Project direction

The project started as a FastAPI backend learning project.

It has now reached a stable backend milestone and is transitioning toward a combined:

```text
Backend
+
Database
+
Data Analysis
```

learning project.

---

## Backend architecture

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

Responsibilities are intentionally separated:

- **Router:** HTTP boundary.
- **Service:** business rules and orchestration.
- **Repository:** database access.
- **Schema:** API validation and contract.
- **Model:** ORM/database representation.
- **Alembic:** schema evolution.

---

## Authentication

Current authentication flow:

```text
Password
  ↓
Argon2 verification
  ↓
JWT
  ↓
user.id stored in sub
  ↓
get_current_user()
  ↓
active-user validation
```

User roles:

```text
user
admin
```

Inactive users cannot obtain a new token, and previously issued tokens are rejected after deactivation because protected requests re-check the current database state.

---

## Database lifecycle

User lifecycle fields include:

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

Post fields include:

```text
id
title
content
user_id
status
created_at
updated_at
```

Post statuses:

```text
draft
published
archived
```

---

## Database migration

Schema changes are controlled by Alembic.

Latest lifecycle migration at this milestone:

```text
c42a7f91d8e3
```

The project now treats these as three states that must be verified separately:

```text
SQLAlchemy Model
Alembic Migration
PostgreSQL Schema
```

One being correct does not automatically prove the other two are correct.

---

## Testing

Latest verified full regression:

```text
79 passed
```

Testing includes:

- API tests;
- Unit tests;
- PostgreSQL integration tests;
- migration/schema behavior tests;
- Playwright / Swagger E2E tests.

Testing is used as regression protection and as a debugging tool rather than simply as a way to obtain green output.

---

## Important debugging lesson

One of the most useful lessons from the project was schema drift.

The project encountered both directions of mismatch:

```text
ORM newer
Database older
```

and:

```text
Database/runtime state newer
ORM/runtime code inconsistent
```

The debugging workflow became:

```text
Failed test / HTTP error
        ↓
Traceback
        ↓
Application layer
        ↓
SQLAlchemy
        ↓
Alembic state
        ↓
PostgreSQL schema
```

instead of changing code based on guesses.

---

## Data Analysis track

A dedicated reproducible analytics dataset is now available:

```text
600 analytics users
2,250 analytics posts
```

The dataset intentionally contains variation suitable for SQL practice.

Current synthetic distributions include:

```text
Roles:
570 user
30 admin

Account state:
540 active
60 inactive

Post status:
1,575 published
450 draft
225 archived
```

---

## SQL Analytics

Exploratory analysis currently includes:

- `GROUP BY`;
- `LEFT JOIN`;
- aggregate functions;
- ratios and percentages;
- `CASE WHEN`;
- `FILTER`;
- `DATE_TRUNC`;
- user segmentation;
- monthly activity;
- engagement comparisons.

Current synthetic KPIs include:

```text
Posting rate:                  80.00%
Average posts / user:           3.75
Average posts / posting user:   4.69
Published posts:               70%
Draft posts:                   20%
Archived posts:                10%
```

These metrics describe **synthetic data** and must not be presented as real user behavior.

---

## Current status

```text
FastAPI Feature Development   ✅ DONE
PostgreSQL / Alembic          ✅ STABLE
Automated Regression          ✅ 79 PASS
Analytics Seed Dataset        ✅ DONE
SQL Exploration               ✅ STARTED
KPI Analysis                  ⏭ NEXT
Window Functions              ⏭
Pandas EDA                    ⏭
Visualization                 ⏭
Dashboard                     ⏭
```

---

## Main learning outcome

The project is no longer only about writing endpoints.

The learning path now connects:

```text
Application
    ↓
Database
    ↓
Testing
    ↓
Data
    ↓
Analysis
    ↓
Insight
```

The next priority is to use SQL and Python to answer analytical questions instead of expanding the backend with additional infrastructure features.
