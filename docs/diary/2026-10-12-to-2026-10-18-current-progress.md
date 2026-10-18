# Development Diary — 2026-10-12 → 2026-10-18

**Weekly report:** W25

## Main goal

The main objective this week was to finish the FastAPI backend at a reasonable portfolio / learning-project boundary and stop adding backend features.

After reaching that checkpoint, the project began transitioning toward SQL and Data Analysis using the same PostgreSQL database.

---

## 1. Database lifecycle V2

The User entity was extended with:

```text
is_active
created_at
updated_at
last_login_at
```

The Post entity was extended with:

```text
status
created_at
updated_at
```

Valid post statuses:

```text
draft
published
archived
```

The lifecycle migration was applied through Alembic:

```text
c42a7f91d8e3
```

The migration was verified against PostgreSQL instead of assuming that updating the ORM model automatically updated the database.

---

## 2. Schema-drift debugging

A major issue this week was schema drift.

At one stage:

```text
SQLAlchemy model
    had new lifecycle fields
```

while:

```text
PostgreSQL
    still had an older schema
```

This caused runtime failures when the application queried columns that the database did not yet have.

After the migration was created and applied, the PostgreSQL schema and application model were synchronized.

A second mismatch appeared around Post status handling.

`PostService` correctly passed:

```python
status=post_data.status
```

but the running SQLAlchemy `Post` model did not yet expose the field correctly.

The observed error was:

```text
TypeError:
'status' is an invalid keyword argument for Post
```

This showed that the failure occurred at ORM object construction before SQL was sent to PostgreSQL.

---

## 3. Authentication lifecycle

Authentication was extended to support account lifecycle behavior.

After a successful login:

```text
last_login_at = current UTC time
```

Inactive accounts:

```text
is_active = false
```

cannot receive a new JWT.

Existing tokens are also rejected after the account is deactivated because `get_current_user()` checks the current database state.

The JWT subject remains:

```text
sub = str(user.id)
```

instead of reverting to the earlier email-based subject.

---

## 4. API and schema lifecycle

Pydantic response schemas now expose lifecycle data.

User responses include:

```text
is_active
created_at
updated_at
last_login_at
```

Post responses include:

```text
status
created_at
updated_at
```

Post input validation uses the allowed lifecycle states:

```text
draft
published
archived
```

Invalid values are rejected at the API boundary before they reach PostgreSQL.

PostgreSQL still retains a CHECK constraint as database-level defense in depth.

---

## 5. Automated verification

Lifecycle coverage was added for:

- user lifecycle response fields;
- `last_login_at`;
- inactive-user login rejection;
- rejection of an already-issued token after deactivation;
- default Post status;
- Post status update;
- invalid Post status;
- PostgreSQL Post status constraint.

Verified regression results:

```text
Integration: 11 passed
API:         50 passed
E2E:          9 passed
Full suite:  79 passed
```

Final full-suite result:

```text
79 passed
```

This became the stopping point for FastAPI feature development.

---

## 6. FastAPI feature freeze

I intentionally decided not to continue expanding the backend with unrelated infrastructure such as:

```text
Redis
Celery
Kafka
Microservices
Kubernetes
```

The backend already provides enough material to explain and demonstrate:

- FastAPI;
- PostgreSQL;
- SQLAlchemy;
- Alembic;
- JWT authentication;
- role-based authorization;
- Repository / Service architecture;
- validation;
- pagination;
- eager loading / query efficiency;
- API, unit, integration, and E2E testing;
- schema-drift debugging.

The goal now is depth and analysis rather than adding more backend technologies.

---

## 7. Transition to Data Analysis

The original development/test data was inspected with SQL.

Initial database state used for exploration:

```text
184 users
113 posts
```

The data was not suitable for meaningful analytical practice because it was dominated by test records:

```text
all users had the same role
all users were active
all posts were published
every posting user had exactly one post
```

The SQL calculations were valid, but the dataset lacked behavioral variation.

This produced an important lesson:

> A technically correct query does not automatically produce a meaningful business insight.

---

## 8. Reproducible analytics dataset

A dedicated synthetic dataset was created for analysis practice.

Verified analytics data:

```text
600 analytics users
2,250 analytics posts
```

User distribution:

```text
570 user
30 admin

540 active
60 inactive
```

Post status distribution:

```text
1,575 published
450 draft
225 archived
```

User posting segments:

```text
No posts       120
1 post         150
2–5 posts      210
6–10 posts      90
11–20 posts     30
```

---

## 9. SQL exploration

Exploratory SQL was written and executed for:

- total users and posts;
- posting users vs non-posting users;
- posting rate;
- average posts per user;
- average posts per posting user;
- Post status distribution;
- User segmentation;
- role distribution;
- active/inactive distribution;
- top content creators;
- monthly user registrations;
- monthly post activity;
- active vs inactive engagement.

Verified synthetic-dataset KPIs:

```text
Posting rate:                  80.00%
Average posts / user:           3.75
Average posts / posting user:   4.69

Published: 70%
Draft:     20%
Archived:  10%
```

---

## 10. Main learning outcome

The project has now changed direction:

```text
Backend engineering
        ↓
Database understanding
        ↓
SQL analysis
        ↓
Data quality
        ↓
Business interpretation
```

The central Data Analyst lesson from this week is:

> Query correctness and business validity are different questions.

An analyst must understand where the data came from, how it was generated, what it represents, and what limitations exist before interpreting a metric.

---

## 11. Current direction

```text
FastAPI
  ✅ feature development stopped
        ↓
PostgreSQL
        ↓
SQL analytics
        ↓
CTE / Window Functions
        ↓
Pandas / NumPy
        ↓
EDA
        ↓
Matplotlib
        ↓
Dashboard
```

## Next step

Continue with:

- KPI analysis;
- CTEs;
- Window Functions;
- `LAG`;
- `RANK`;
- `NTILE`;
- Pandas EDA;
- visualization;
- business-insight writing.
