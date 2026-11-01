# Documentation Audit — FastAPI User Management

**Audit date:** 2026-11-01  
**Primary evidence:** latest uploaded `project_context.md`  
**Audit type:** source-to-diary and exporter-consistency review

---

## 1. Executive conclusion

The diary is behind the source snapshot in the Python Analytics layer and the Analytics API. The root README documents a later KPI/dashboard milestone, but the current export script excludes the file types required to verify those components.

The key findings are:

1. The original diary index is dated 2026-10-18, while the current source export includes Analytics modules and an admin-protected User Analytics endpoint.
2. The 2026-09-28 Analytics API plan was only partially delivered: the current endpoint returns total Users and Users by Role; age statistics and Post statistics by Role are not part of the endpoint.
3. Post Analytics has an empty-data defect and a misleading average metric name.
4. `get_users_dataframe()` loads the complete User ORM entity, including the password column, although the DataFrame omits it.
5. The root README documents KPI 7 and a Next.js dashboard, but the underlying SQL/JSON/JavaScript/TypeScript files are excluded by `export_project.py`.
6. The current export count of 139 is the count of allowed files, not necessarily the full repository.
7. The historical `79 passed` result remains valid only as a recorded 2026-10-18 result. The current source contains 83 test-function definitions, but no fresh pytest collection or full test run was completed.
8. The root README's Uvicorn command is inconsistent with the actual application module.

This package preserves the original diary records, updates the diary index, adds a source-based retrospective and current summary, and appends a cautious migration note to the existing documentation-gap record.

---

## 2. Scope and evidence labels

The latest `project_context.md` reports 139 included files and contains 45 Markdown files under `docs/diary/`.

The audit reviewed:

- all 45 diary Markdown files;
- root `README.md`;
- `export_project.py`;
- `docs/mentor/DOCKER_AND_ANALYTICS_NOTES.md`;
- `docs/mentor/development-notes.md`;
- Alembic migrations;
- ORM models;
- Analytics modules and router;
- API, unit, integration, and E2E test source;
- practice scripts.

Evidence labels:

| Label | Meaning |
|---|---|
| Source-confirmed | Directly visible in source code included in the export |
| Test-source-confirmed | A test is present and asserts the behavior; it was not necessarily executed |
| Historical result | A prior diary records a result from that date |
| README-documented | Root README describes the feature/value, but underlying implementation was not included for direct review |
| Unverified | The supplied export does not provide enough evidence to establish implementation or runtime behavior |

This audit did not modify application source code, connect to PostgreSQL, run Alembic migrations, verify the live Vercel deployment, or run the full pytest suite.

---

## 3. Diary timeline review

The current export contains 45 `docs/diary/*.md` files. The latest original progress record is W25, ending 2026-10-18.

| Period | Diary status |
|---|---|
| 2026-07-28 to 2026-08-09 | Daily records and project summary |
| 2026-08-10 to 2026-08-28 | Retrospective gap |
| 2026-08-29 to 2026-09-13 | Daily progress records |
| 2026-09-14 to 2026-09-23 | No reliable daily records in this export |
| 2026-09-24 to 2026-09-28 | Daily records and future plan |
| 2026-09-29 to 2026-10-04 | Daily records and weekly summary |
| 2026-10-05 to 2026-10-11 | Retrospective documentation gap |
| 2026-10-12 to 2026-10-18 | W25 diary and project summary |
| 2026-10-19 to 2026-11-01 | No original daily diary; covered by a labelled source retrospective |

No daily records were fabricated for missing periods.

---

## 4. Source-to-diary comparison

### 4.1 Alembic migrations

The source migration chain is:

```text
e7d9b8aad922
      ↓
b31f9c2a6d10
      ↓
c42a7f91d8e3
```

`b31f9c2a6d10` declares `Create Date: 2026-10-07` and enforces allowed User roles, nullability, a server default, and a CHECK constraint.

`c42a7f91d8e3` declares `Create Date: 2026-10-14` and adds User/Post lifecycle fields and the Post status CHECK constraint.

W25 records that the lifecycle migration was applied and verified against PostgreSQL. The role migration's declared creation date does not prove its exact execution date; the addendum to the 2026-10-05 to 2026-10-11 gap makes this evidence boundary explicit.

### 4.2 Backend architecture and behavior

The current source includes:

- Router → Service → Repository separation;
- SQLAlchemy User/Post models;
- Pydantic request and response schemas;
- password hashing and JWT authentication;
- admin authorization;
- active-account checks;
- Post ownership checks;
- pagination and search;
- response metadata headers;
- custom application exceptions.

Most of these backend milestones are already represented in the historical diary. The synchronization therefore avoids rewriting the entire backend history.

### 4.3 Query efficiency and database integration tests

`tests/unit/test_query_efficiency.py` expects:

- User list: two SELECT statements — Users plus related Posts via `selectinload`;
- Post list: one SELECT statement — Posts with owner via `joinedload`.

Integration tests cover Alembic head, expected tables, role constraints, lifecycle columns, duplicate email, invalid roles, null roles, foreign keys, case-insensitive `ILIKE`, and invalid Post status.

These are test-source assertions, not proof of a fresh test execution during this audit.

### 4.4 Python Analytics

| File | Source-confirmed behavior | Diary gap / limitation |
|---|---|---|
| `analytics/user_analysis.py` | User DataFrame, total count, count by role, empty-frame handling | Whole User ORM entity is loaded; lifecycle fields omitted |
| `analytics/post_analysis.py` | Post DataFrame, counts per user, statistics, merge, top users, posts by role | Empty-frame failure; average excludes zero-post users; lifecycle fields omitted |
| `analytics/charts.py` | Users by role, age histogram helper, top-user chart | Age is not a field on current User model; no direct chart tests |

### 4.5 Analytics API

Source-confirmed endpoint:

```text
GET /analytics/users/summary
```

It requires `get_admin_user` and returns total User count and User counts by Role.

The API test source checks:

- unauthenticated request → 401;
- normal authenticated User → 403;
- Admin → 200.

The 2026-09-28 plan included age median/standard deviation and average Post counts by Role. The current endpoint does not implement the full plan. The `posts_by_role()` helper exists but is not integrated into the endpoint. The User model has no `age` column.

### 4.6 Analytics helper defects reproduced during review

The following calls fail on an empty DataFrame because the expected `user_id` column does not exist:

```text
posts_per_user(pd.DataFrame())
calculate_post_statistics(pd.DataFrame())
merge_users_posts(users_df, pd.DataFrame())
```

Each raises:

```text
KeyError: 'user_id'
```

The source of the problem is that `get_posts_dataframe()` creates `pd.DataFrame(data)` without an explicit column list. When there are no Post rows, the resulting DataFrame has no columns.

The average calculation also excludes users with zero Posts. The W25 diary distinguishes 3.75 Posts per all Users from 4.6875 Posts per posting User; the function currently returns the latter while naming the field `average_posts_per_user`.

### 4.7 Current test-source inventory

Static AST inspection found 83 `test_` function definitions:

| Area | Definitions |
|---|---:|
| API | 54 |
| Integration | 11 |
| E2E | 9 |
| Unit | 9 |
| **Total** | **83** |

The W25 diary records 79 passed on 2026-10-18. The 83 static definitions do not prove 83 tests are collected or passing. The four-definition difference should not be assigned to a date without Git history.

During this audit:

- `python -m compileall -q app analytics tests practice alembic` completed successfully;
- `pytest --collect-only -q` stopped because `python-jose` (`jose`) was not installed in the audit environment;
- no full suite or PostgreSQL integration run was completed.

### 4.8 SQL KPI and dashboard

The root README documents KPI 7:

| Metric | README-documented value |
|---|---:|
| Total users | 600 |
| Total posts | 2,250 |
| Posts attributed to top 10% creator group | 870 |
| Top-creator post share | 38.67% |
| Stated verification date | 2026-10-25 |

The percentage arithmetic is correct:

```text
870 / 2,250 × 100 = 38.67%
```

The root README identifies `sql/analytics/03_kpi_analysis.sql` as the source and describes JSON snapshots and a Next.js data pipeline. The actual SQL, JSON, JavaScript, TypeScript, and TSX files were not included in this export. The KPI and dashboard are therefore README-documented, not independently source-verified here.

The README states that the dashboard uses snapshots and does not query PostgreSQL live. This architecture should remain explicit in documentation unless the implementation changes.

---

## 5. Root cause: exporter omits key source types

`export_project.py` currently allows:

```python
ALLOWED_EXTENSIONS = {
    ".py",
    ".md",
    ".txt",
    ".ini",
    ".yml",
    ".yaml",
    ".sh",
    ".dockerfile",
}
```

This excludes:

```text
.sql
.json
.js
.mjs
.ts
.tsx
.css
.scss
.html
```

Consequences:

- SQL analytics files are absent from the exported file inventory/content;
- JSON KPI and monthly snapshots are omitted;
- `package.json` and TypeScript configuration are omitted;
- Next.js page/component source is omitted;
- JavaScript/TypeScript sync scripts are omitted.

Therefore, the `139` figure is the count of files accepted by the exporter, not necessarily the total number of repository files. It is incorrect to conclude from this export alone that the SQL or dashboard files do not exist in the repository.

### Recommended exporter change

Extend the allowlist with the required file types:

```python
ALLOWED_EXTENSIONS = {
    ".py", ".md", ".txt", ".ini",
    ".yml", ".yaml", ".sh", ".dockerfile",
    ".sql", ".json",
    ".js", ".mjs", ".ts", ".tsx",
    ".css", ".scss", ".html", ".toml",
}
```

Add generated/build/dependency directories to `EXCLUDED_DIRS`, including:

```text
.next
.vercel
out
dist
build
coverage
```

Exclude large lock/generated files where appropriate, while retaining `package.json` and the KPI/monthly snapshot JSON files.

The next export should include at least:

```text
sql/analytics/*.sql
mentor-web/package.json
mentor-web/scripts/*.mjs
mentor-web/src/**/*.tsx
mentor-web/src/data/analytics-kpi.snapshot.json
mentor-web/src/data/monthly-posts.snapshot.json
```

---

## 6. Documentation consistency findings

| File | Finding | Recommended correction |
|---|---|---|
| `docs/diary/README.md` | Stale at 2026-10-18; says KPI analysis/dashboard are next | Updated to 2026-11-01 with evidence labels |
| `2026-10-18-project-summary.md` | Correct historical snapshot, but not current | Preserved; new current summary added |
| `2026-10-05-to-2026-10-11-retrospective-gap.md` | Does not mention role-constraint migration source | Added source-based note without inventing execution date |
| Root `README.md` | Uses `uvicorn main:app --reload` | Correct to `uvicorn app.main:app --reload` |
| `mentor-web/README.md` | Generic create-next-app template | Update from actual dashboard source and package scripts |
| `docs/mentor/DOCKER_AND_ANALYTICS_NOTES.md` | Mentions `gender` and `birth_year` as possible analysis fields | Mark as future/external-data examples; current User model does not contain them |

---

## 7. Prioritized engineering follow-up

| Priority | Task | Why it matters |
|---|---|---|
| P0 | Extend `export_project.py` allowlist | Makes the next source audit complete |
| P0 | Re-export SQL, snapshots, and dashboard source | Verifies README's KPI/dashboard claims |
| P1 | Fix empty-Post DataFrame handling | Prevents `KeyError` on zero Posts |
| P1 | Select only required User columns | Avoids loading password and unused fields into analytics |
| P1 | Correct average metric naming/denominator | Prevents incorrect business interpretation |
| P1 | Add tests for Post Analytics and chart helpers | Current tests cover the API route, not helper edge cases |
| P1 | Re-run pytest and record real results | Separates historical 79 passed from current source state |
| P2 | Decide whether `posts_by_role()` belongs in the API | Aligns endpoint scope with the 2026-09-28 plan |
| P2 | Define a legitimate age data source before age metrics | The User model has no age field |
| P2 | Correct the root README Uvicorn command | Makes setup instructions executable |
| P2 | Replace generic dashboard README | Aligns documentation with actual frontend implementation |

---

## 8. Final assessment

The diary is behind the source snapshot in the Python Analytics layer and the Analytics API. The root README describes a further SQL/KPI/dashboard milestone, but the exporter currently filters out the source types required to verify it.

The most important correction is to fix the exporter before the next synchronization. Otherwise, future audits will continue to operate on an incomplete source snapshot.

This update preserves the historical diary, records only source-supported retrospective findings, and keeps README-only claims separate from verified implementation. No application source code was changed.
