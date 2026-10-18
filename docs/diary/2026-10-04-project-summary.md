# FastAPI User Management — Weekly Project Summary

**Period:** 2026-09-29 → 2026-10-04

## 1. Main focus

This period focused on stabilizing the FastAPI learning environment and beginning the transition from backend development toward data analysis.

The work covered four connected areas:

- authentication and password security;
- Docker / Playwright E2E stability;
- regression testing and coverage;
- introductory NumPy and Pandas practice using project data.

---

## 2. Authentication and security review

The authentication flow was reviewed around:

```text
password
   ↓
Argon2 hashing / verification
   ↓
JWT access token
```

The project uses `pwdlib` with Argon2 for password hashing and `python-jose` for JWT creation.

The password flow was verified directly inside the container:

- correct password → accepted;
- incorrect password → rejected;
- stored password → hashed instead of plain text.

UTC-aware datetime handling was also reviewed for token-related time values.

---

## 3. Docker and Playwright Firefox

A Playwright/Firefox issue appeared inside Docker:

```text
Sandbox: CanCreateUserNamespace() clone() failure: EPERM
```

The root cause was related to the container security profile rather than missing Python packages.

For the local development / E2E environment, the API service was tested with:

```yaml
security_opt:
  - seccomp:unconfined
```

This allowed Firefox to launch successfully in the controlled development environment.

> This setting reduces container isolation and is not treated as a production default.

---

## 4. Regression testing

After stabilizing Firefox, the API and E2E tests were run again.

Verified result at this milestone:

```text
31 passed
```

including:

```text
22 API tests
9 E2E tests
```

Coverage was approximately:

```text
79%
```

The key lesson was that coverage is useful for locating untested code, but a high coverage percentage does not prove that the application is bug-free.

---

## 5. PostgreSQL and Alembic

The database remained managed through PostgreSQL and Alembic.

At this milestone:

```text
Alembic head:
e7d9b8aad922
```

The project no longer depended on `Base.metadata.create_all()` in application startup as the main schema-management mechanism.

The intended flow remained:

```text
SQLAlchemy Model
      ↓
Alembic Migration
      ↓
PostgreSQL Schema
```

---

## 6. Beginning the Data Analysis track

After the backend/testing environment became more stable, a separate practice area was used for:

- NumPy;
- Pandas;
- Matplotlib preparation.

Project user data was loaded from PostgreSQL into a Pandas DataFrame.

The password field was intentionally excluded from analytical output.

Early Pandas practice included:

```text
column selection
filtering
sorting
groupby
value_counts
missing-value checks
```

---

## 7. Data-analysis lessons

Several important lessons appeared early:

### Identifier is not a business metric

Using `id` to practice NumPy functions is technically possible, but statistics such as mean or standard deviation on an identifier normally have no business meaning.

### Inspect schema before assuming columns

An early attempt referenced a non-existent `username` attribute.

The fix was to verify the actual `User` model and use the real fields instead.

### Clean text before grouping

Name initials showed separate values such as:

```text
A
S
a
```

Normalizing case before counting produced a more meaningful grouping.

### SQL and Pandas have strong conceptual parallels

```text
SQL WHERE       ↔ Pandas boolean filtering
SQL ORDER BY    ↔ sort_values()
SQL GROUP BY    ↔ groupby()
SQL COUNT       ↔ size() / count()
```

This connection made the transition from backend database work to data analysis easier to understand.

---

## 8. Status at the end of the period

```text
FastAPI backend              ✅ working
PostgreSQL                   ✅ working
Alembic                      ✅ working
API automated tests          ✅
Playwright Firefox E2E       ✅
Coverage review              ✅
NumPy basics                 ✅ started
Pandas basics                ✅ started
Matplotlib                   ⏭ next
```

---

## 9. Next direction

The next phase should avoid adding unrelated backend complexity.

Priority:

```text
Backend stability
      ↓
Database correctness
      ↓
SQL / Pandas analysis
      ↓
Visualization
      ↓
Meaningful analytical questions
```

The aim is to reuse the same project as both a backend engineering exercise and a practical source of data for the next learning phase.
