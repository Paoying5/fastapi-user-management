# FastAPI User Management — Development Diary

**Last updated:** 2026-10-18

This directory records the learning and development journey of the FastAPI User Management project.

The diary is treated as a historical engineering record:

- older entries describe the project state at that time;
- old entries are not rewritten simply because the architecture changed later;
- retrospective entries are clearly marked when the original daily log is unavailable;
- missing periods are recorded as gaps instead of being reconstructed as fake daily history.

---

## Current project status

FastAPI feature development has reached the planned stopping point.

Latest verified regression:

```text
79 passed
```

Current backend flow:

```text
HTTP Request
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

Current direction:

```text
FastAPI Backend
      ✅ DONE
       ↓
PostgreSQL / SQL
       ↓
Data Analysis
       ↓
Pandas / NumPy
       ↓
Visualization
       ↓
Dashboard
```

---

## Current mentor-facing files

Start here for the latest state:

1. [Current Project Summary — 18/10/2026](./2026-10-18-project-summary.md)
2. [W25 Development Diary — 12/10 → 18/10](./2026-10-12-to-2026-10-18-current-progress.md)
3. [Documentation Gap — 05/10 → 11/10](./2026-10-05-to-2026-10-11-retrospective-gap.md)
4. [Weekly Project Summary — 29/09 → 04/10](./2026-10-04-project-summary.md)

---

## Timeline

### 28/07 → 09/08 — Backend foundation

Topics included:

- FastAPI CRUD;
- SQLAlchemy;
- PostgreSQL;
- JWT authentication;
- Docker;
- Alembic;
- Repository Pattern;
- Service Layer;
- Models / Schemas;
- testing;
- schema debugging.

Historical overview:

[Project Summary — 09/08](./2026-08-09-project-summary.md)

---

### 10/08 → 28/08 — Retrospective gap

The original day-by-day record is not reliable enough to reconstruct exact activity.

Use the single consolidated retrospective instead:

[Retrospective Learning Record — 10/08 → 28/08](./2026-08-10-to-2026-08-28-retrospective-gap.md)

---

### 29/08 → 13/09 — Runtime verification and E2E

Focus included:

- authentication verification;
- request-flow review;
- Alembic baseline stabilization;
- API tests;
- Playwright / Swagger E2E;
- debugging Swagger Authorize → Post interaction.

---

### 14/09 → 23/09 — Documentation gap

There are no reliable daily diary files for this period in the current project context.

The gap is intentionally left visible rather than reconstructed from assumptions.

---

### 24/09 → 28/09 — Architecture cleanup and pagination

Focus included:

- removing overlap between old CRUD and Repository/Service architecture;
- handing schema management to Alembic;
- Docker environment cleanup;
- server-side pagination and search;
- planning stronger automated test coverage.

---

### 29/09 → 04/10 — Testing stability and first Data Analysis practice

Focus included:

- authentication/password verification;
- Docker Firefox sandbox debugging;
- API + E2E regression and coverage;
- NumPy basics;
- Pandas filtering, sorting, grouping, `value_counts`, and missing-value checks.

See:

[Weekly Project Summary — 29/09 → 04/10](./2026-10-04-project-summary.md)

---

### 05/10 → 11/10 — Report not submitted

This period is not backfilled as a fake Week 24 report.

See:

[Retrospective Documentation Gap — 05/10 → 11/10](./2026-10-05-to-2026-10-11-retrospective-gap.md)

---

### 12/10 → 18/10 — W25

Major verified milestones:

- User/Post lifecycle fields;
- Alembic lifecycle migration;
- inactive-user authentication behavior;
- `last_login_at`;
- Post status lifecycle;
- full regression reaching `79 passed`;
- FastAPI feature freeze;
- analytics-ready synthetic dataset;
- SQL exploration.

See:

[W25 Development Diary — 12/10 → 18/10](./2026-10-12-to-2026-10-18-current-progress.md)

and:

[Current Project Summary — 18/10](./2026-10-18-project-summary.md)

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

The purpose of the diary is not to make the project appear perfect.

Debugging, failed assumptions, documentation gaps, and architectural corrections are part of the learning record.

---

## Data Analysis direction

A dedicated reproducible synthetic dataset is now used for analysis practice:

```text
600 analytics users
2,250 analytics posts
```

Current SQL topics include:

- `SELECT`;
- `WHERE`;
- `ORDER BY`;
- aggregate functions;
- `GROUP BY`;
- `LEFT JOIN`;
- `CASE WHEN`;
- `FILTER`;
- `DATE_TRUNC`;
- percentages and ratios;
- user segmentation;
- exploratory KPI analysis.

Next:

```text
CTE
↓
Window Functions
↓
LAG / LEAD
↓
RANK / NTILE
↓
Pandas EDA
↓
Visualization
↓
Dashboard
```
