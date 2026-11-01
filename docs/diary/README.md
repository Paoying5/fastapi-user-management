# FastAPI User Management — Development Diary

**Last updated:** 2026-11-01  
**Evidence baseline:** `project_context.md` export reviewed on 2026-11-01

This directory records the learning and development history of the FastAPI User Management project.

The diary is a historical engineering record:

- original entries describe what was recorded at the time;
- historical entries are not silently rewritten to match later architecture;
- retrospective notes are explicitly labelled;
- missing daily records remain visible as documentation gaps;
- source-code evidence is separated from test-source evidence, runtime verification, and README-only claims.

---

## Current project status — 2026-11-01

### Backend and database

The source export contains a FastAPI application using PostgreSQL, SQLAlchemy, Alembic, JWT authentication, and a Router → Service → Repository structure.

The migration chain represented in source is:

```text
e7d9b8aad922
      ↓
b31f9c2a6d10
      ↓
c42a7f91d8e3
```

The current models and migrations include:

- User roles `user` and `admin`, with a database CHECK constraint;
- User lifecycle fields `is_active`, `created_at`, `updated_at`, `last_login_at`;
- Post lifecycle fields `status`, `created_at`, `updated_at`;
- allowed Post statuses `draft`, `published`, `archived`;
- pagination, search, authentication, authorization, and Post ownership checks.

FastAPI feature development was recorded as frozen at the 2026-10-18 milestone. This audit does not reopen backend scope.

### Testing

The 2026-10-18 diary records a full regression result of **79 passed**. This is a historical result, not a fresh test run.

A static scan of the current exported test source finds **83 test-function definitions**:

| Test area | Definitions |
|---|---:|
| API | 54 |
| Integration | 11 |
| E2E | 9 |
| Unit | 9 |
| **Total** | **83** |

A static function count is not a pytest collection result and does not mean 83 tests pass. The audit environment could not collect tests because `python-jose` (`jose`) was not installed. Python syntax compilation completed successfully.

### Python Analytics

The source export contains:

- `analytics/user_analysis.py`
- `analytics/post_analysis.py`
- `analytics/charts.py`

The current Analytics API is:

```text
GET /analytics/users/summary
```

It is admin-protected and returns total users and users grouped by role. The API tests cover unauthenticated access (401), a normal user (403), and an admin (200).

The Post Analytics helpers and chart helpers exist in source, but they are not exposed as separate API endpoints and have no dedicated analytics-helper test module in the export.

Important limitations found during review:

- the User DataFrame query loads the complete User ORM entity, including `password`, although the DataFrame output omits that field;
- the Post DataFrame omits lifecycle fields and returns a zero-column DataFrame when there are no Posts;
- Post helper functions fail on that empty DataFrame because `user_id` is missing;
- `calculate_post_statistics()` averages only across users with at least one Post, not across every User;
- the age chart requires an `age` column, which the current User model does not define.

See [Documentation Audit — 2026-11-01](./2026-11-01-documentation-audit.md).

### SQL analytics and Dashboard

The root README documents SQL analytics, KPI 7, a Next.js dashboard, JSON snapshots, a synchronization script, and a Vercel URL.

Those are **README-documented claims**, not independently verified source components in this export. The reason is the current `export_project.py` allowlist: it excludes `.sql`, `.json`, `.js`, `.mjs`, `.ts`, and `.tsx` files, among others.

The README documents a KPI snapshot with 600 users, 2,250 posts, 870 posts attributed to the top 10% creator group, and a 38.67% share, with a stated verification date of 2026-10-25. The arithmetic `870 / 2250 × 100 = 38.67%` is correct, but the SQL query and JSON snapshot were not included for independent validation.

The README also says the dashboard is snapshot-based and does not query PostgreSQL live. The full Next.js source and package manifest were not included in this export, so dashboard implementation and deployment were not re-tested.

---

## Current mentor-facing files

Start with these files for the current state:

1. [Current Project Summary — 2026-11-01](./2026-11-01-project-summary.md)
2. [Retrospective Source Review — 2026-10-19 to 2026-11-01](./2026-10-19-to-2026-11-01-retrospective.md)
3. [Documentation Audit — 2026-11-01](./2026-11-01-documentation-audit.md)
4. [W25 Development Diary — 2026-10-12 to 2026-10-18](./2026-10-12-to-2026-10-18-current-progress.md)
5. [Current Project Summary — 2026-10-18](./2026-10-18-project-summary.md)

---

## Timeline

### 2026-07-28 → 2026-08-09 — Backend foundation

Topics included FastAPI CRUD, SQLAlchemy, PostgreSQL, JWT authentication, Docker, Alembic, Repository Pattern, Service Layer, Models/Schemas, testing, and schema debugging.

[Project Summary — 2026-08-09](./2026-08-09-project-summary.md)

### 2026-08-10 → 2026-08-28 — Retrospective gap

The original day-by-day record is not reliable enough to reconstruct exact activity.

[Retrospective Learning Record — 2026-08-10 to 2026-08-28](./2026-08-10-to-2026-08-28-retrospective-gap.md)

### 2026-08-29 → 2026-09-13 — Runtime verification and E2E

Focus included authentication verification, request-flow review, Alembic baseline stabilization, API tests, Playwright/Swagger E2E, and debugging Swagger Authorize → Post interaction.

### 2026-09-14 → 2026-09-23 — Documentation gap

There are no reliable daily diary files for this period in the supplied project context. The gap remains visible.

### 2026-09-24 → 2026-09-28 — Architecture cleanup, pagination, and Analytics API planning

Focus included removing overlap between old CRUD and Repository/Service architecture, Alembic-based schema management, Docker cleanup, server-side pagination and search, test coverage planning, and the proposed admin-only User Analytics endpoint.

The 2026-09-28 plan proposed age statistics and Post statistics by role. The current endpoint implements a narrower User summary; see the retrospective and audit.

[Future Plan — 2026-09-28](./2026-09-28-future-plan.md)

### 2026-09-29 → 2026-10-04 — Testing stability and first Data Analysis practice

Focus included authentication/password verification, Docker Firefox sandbox debugging, API + E2E regression, NumPy basics, and Pandas filtering, sorting, grouping, `value_counts`, and missing-value checks.

[Weekly Project Summary — 2026-10-04](./2026-10-04-project-summary.md)

### 2026-10-05 → 2026-10-11 — Daily documentation gap

The daily record remains a gap. A source-based note records the role-constraint migration definition and declared date without inventing a day-by-day activity history.

[Retrospective Documentation Gap — 2026-10-05 to 2026-10-11](./2026-10-05-to-2026-10-11-retrospective-gap.md)

### 2026-10-12 → 2026-10-18 — W25: lifecycle and analytics dataset

Major recorded milestones:

- User/Post lifecycle fields;
- Alembic lifecycle migration;
- inactive-user authentication behavior;
- `last_login_at`;
- Post status lifecycle;
- full regression recorded as `79 passed`;
- FastAPI feature freeze;
- synthetic analytics dataset with 600 users and 2,250 posts;
- SQL exploration.

[W25 Development Diary](./2026-10-12-to-2026-10-18-current-progress.md)

### 2026-10-19 → 2026-11-01 — Retrospective source synchronization

The current source export shows Python Analytics modules, an admin-protected User Analytics endpoint, and additional test definitions. The root README documents KPI 7 and a dashboard pipeline, but the underlying SQL/JSON/Next.js source files are excluded by the current export allowlist.

This is a consolidated source review, not a day-by-day reconstruction.

[Retrospective Source Review — 2026-10-19 to 2026-11-01](./2026-10-19-to-2026-11-01-retrospective.md)

---

## Data Analysis direction

The current learning path connects:

```text
PostgreSQL schema and data
        ↓
SQL query design and validation
        ↓
Python data extraction
        ↓
Pandas / NumPy
        ↓
EDA and data-quality checks
        ↓
Matplotlib visualization
        ↓
KPI interpretation
        ↓
Dashboard presentation
```

Next practical priorities:

1. Export the actual SQL analytics files and JSON snapshots so KPI calculations can be reviewed.
2. Clarify the population used by every average and percentage.
3. Fix empty-Post DataFrame handling and add direct tests for analytics helpers.
4. Re-run pytest in the project environment and record the current result.
5. Export the full Next.js source and verify its data synchronization/build pipeline.
6. Continue CTEs and Window Functions only when the SQL source and learning record support that status.

---

## Documentation rule

Each meaningful diary entry should answer:

```text
What was the goal?
      ↓
What was actually done?
      ↓
What failed?
      ↓
What was the root cause?
      ↓
How was it verified?
      ↓
What was learned?
      ↓
What comes next?
```

The purpose of the diary is not to make the project appear perfect. Debugging, failed assumptions, documentation gaps, and architectural corrections are part of the engineering record.
