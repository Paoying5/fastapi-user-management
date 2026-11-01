# PROJECT CONTEXT

**Project root:** `/home/truongp/Documents/fastapi-user-management`  
**Total included files:** 139

## Project Structure

- `.dockerignore`
- `.gitignore`
- `Dockerfile`
- `LICENSE`
- `README.md`
- `alembic.ini`
- `alembic/env.py`
- `alembic/versions/b31f9c2a6d10_enforce_user_role_constraints.py`
- `alembic/versions/c42a7f91d8e3_add_lifecycle_fields.py`
- `alembic/versions/e7d9b8aad922_initial_schema.py`
- `analytics/__init__.py`
- `analytics/charts.py`
- `analytics/post_analysis.py`
- `analytics/user_analysis.py`
- `app/__init__.py`
- `app/constants.py`
- `app/core/config.py`
- `app/core/exceptions.py`
- `app/core/logging.py`
- `app/core/security.py`
- `app/database.py`
- `app/dependencies.py`
- `app/main.py`
- `app/models/__init__.py`
- `app/models/post.py`
- `app/models/user.py`
- `app/repositories/__init__.py`
- `app/repositories/post_repository.py`
- `app/repositories/user_repository.py`
- `app/routers/__init__.py`
- `app/routers/analytics.py`
- `app/routers/auth.py`
- `app/routers/health.py`
- `app/routers/post.py`
- `app/routers/user.py`
- `app/schemas/__init__.py`
- `app/schemas/auth.py`
- `app/schemas/common.py`
- `app/schemas/post.py`
- `app/schemas/user.py`
- `app/services/__init__.py`
- `app/services/auth_service.py`
- `app/services/post_service.py`
- `app/services/user_service.py`
- `app/utils/helpers.py`
- `app/utils/pagination.py`
- `app/utils/response.py`
- `app/utils/validators.py`
- `docker-compose.yml`
- `docs/diary/2026-07-28-current-progress.md`
- `docs/diary/2026-07-29-current-progress.md`
- `docs/diary/2026-07-30-current-progress.md`
- `docs/diary/2026-07-31-current-progress.md`
- `docs/diary/2026-08-01-current-progress.md`
- `docs/diary/2026-08-02-current-progress.md`
- `docs/diary/2026-08-03-current-progress.md`
- `docs/diary/2026-08-04-current-progress.md`
- `docs/diary/2026-08-05-current-progress.md`
- `docs/diary/2026-08-06-current-progress.md`
- `docs/diary/2026-08-07-current-progress.md`
- `docs/diary/2026-08-08-current-progress.md`
- `docs/diary/2026-08-09-project-summary.md`
- `docs/diary/2026-08-10-to-2026-08-28-retrospective-gap.md`
- `docs/diary/2026-08-29-current-progress.md`
- `docs/diary/2026-08-30-current-progress.md`
- `docs/diary/2026-08-31-current-progress.md`
- `docs/diary/2026-09-01-current-progress.md`
- `docs/diary/2026-09-02-current-progress.md`
- `docs/diary/2026-09-03-current-progress.md`
- `docs/diary/2026-09-04-current-progress.md`
- `docs/diary/2026-09-05-current-progress.md`
- `docs/diary/2026-09-06-current-progress.md`
- `docs/diary/2026-09-07-current-progress.md`
- `docs/diary/2026-09-08-current-progress.md`
- `docs/diary/2026-09-09-current-progress.md`
- `docs/diary/2026-09-10-current-progress.md`
- `docs/diary/2026-09-11-current-progress.md`
- `docs/diary/2026-09-12-current-progress.md`
- `docs/diary/2026-09-13-current-progress.md`
- `docs/diary/2026-09-24-current-progress.md`
- `docs/diary/2026-09-25-current-progress.md`
- `docs/diary/2026-09-26-current-progress.md`
- `docs/diary/2026-09-27-current-progress.md`
- `docs/diary/2026-09-28-future-plan.md`
- `docs/diary/2026-09-29-current-progress.md`
- `docs/diary/2026-09-30-current-progress.md`
- `docs/diary/2026-10-01-current-progress.md`
- `docs/diary/2026-10-02-current-progress.md`
- `docs/diary/2026-10-03-current-progress.md`
- `docs/diary/2026-10-04-project-summary.md`
- `docs/diary/2026-10-05-to-2026-10-11-retrospective-gap.md`
- `docs/diary/2026-10-12-to-2026-10-18-current-progress.md`
- `docs/diary/2026-10-18-project-summary.md`
- `docs/diary/README.md`
- `docs/mentor/DOCKER_AND_ANALYTICS_NOTES.md`
- `docs/mentor/development-notes.md`
- `export_project.py`
- `htmlcov/.gitignore`
- `mentor-web/.gitignore`
- `mentor-web/AGENTS.md`
- `mentor-web/README.md`
- `practice/pandas_lesson2.py`
- `practice/pandas_numpy_lesson1.py`
- `pytest.ini`
- `requirements-dev.txt`
- `requirements.txt`
- `scripts/menu.sh`
- `test_connection.py`
- `tests/__init__.py`
- `tests/api/test_analytics.py`
- `tests/api/test_auth.py`
- `tests/api/test_create_user.py`
- `tests/api/test_health.py`
- `tests/api/test_lifecycle.py`
- `tests/api/test_openapi_contract.py`
- `tests/api/test_pagination.py`
- `tests/api/test_posts.py`
- `tests/api/test_user_filters.py`
- `tests/api/test_users.py`
- `tests/api/test_validation.py`
- `tests/conftest.py`
- `tests/e2e/__init__.py`
- `tests/e2e/test_swagger_auth.py`
- `tests/e2e/test_swagger_authorize.py`
- `tests/e2e/test_swagger_home.py`
- `tests/e2e/test_swagger_posts.py`
- `tests/e2e/test_swagger_users.py`
- `tests/e2e/utils.py`
- `tests/integration/__init__.py`
- `tests/integration/conftest.py`
- `tests/integration/test_migrations.py`
- `tests/integration/test_postgres_behavior.py`
- `tests/swagger/test_auth_swagger.py`
- `tests/swagger/test_posts_swagger.py`
- `tests/swagger/test_users_swagger.py`
- `tests/swagger/utils.py`
- `tests/unit/test_query_efficiency.py`
- `tests/unit/test_service_exceptions.py`
- `tests/unit/test_user_integrity.py`

## File Contents


---

## `.dockerignore`

```gitignore
# ==========================
# Python
# ==========================
__pycache__/
*.py[cod]
*.pyo
*.pyd
*.so

# Virtual Environment
.venv/
venv/
env/

# ==========================
# Git
# ==========================
.git/
.gitignore

# ==========================
# IDE
# ==========================
.vscode/
.idea/

# ==========================
# Pytest
# ==========================
.pytest_cache/
.coverage
htmlcov/

# ==========================
# Logs
# ==========================
*.log
logs/

# ==========================
# Environment
# ==========================
.env

# ==========================
# Build
# ==========================
dist/
build/
*.egg-info/

# ==========================
# Notebook
# ==========================
.ipynb_checkpoints/

# ==========================
# Docker
# ==========================
docker-compose.override.yml

# ==========================
# OS
# ==========================
.DS_Store
Thumbs.db

# ==========================
# Alembic cache
# ==========================
alembic/__pycache__/

# ==========================
# Misc
# ==========================
.cache/
```


---

## `.gitignore`

```gitignore
# Python
__pycache__/
*.py[cod]
*.pyo

# Environment
.env
.venv/
venv/

# IDE
.vscode/
.idea/

# Notebook
.ipynb_checkpoints/

# Database
*.db

# Python cache
.pytest_cache/
.mypy_cache/

# OS
.DS_Store

# Docker
*.log
.coverage
htmlcov/
```


---

## `Dockerfile`

```dockerfile
FROM python:3.12-slim

WORKDIR /app

ENV PLAYWRIGHT_BROWSERS_PATH=/ms-playwright

COPY requirements.txt requirements-dev.txt ./

RUN pip install --no-cache-dir -r requirements-dev.txt

RUN playwright install --with-deps firefox

COPY . .

HEALTHCHECK \
    --interval=30s \
    --timeout=5s \
    --start-period=20s \
    --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
```


---

## `LICENSE`

```text
MIT License

Copyright (c) 2026 Truong Pham

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```


---

## `README.md`

```markdown
 <h1 align="center">FastAPI User Management & Analytics Dashboard</h1>

<p align="center">
  A backend development project built with FastAPI and PostgreSQL, featuring SQL analytics and an online dashboard built with Next.js.
</p>

<p align="center">
  <a href="https://fastapi-user-management-dashboard-three.vercel.app">
    <img src="https://img.shields.io/badge/Live%20Dashboard-Vercel-black?style=for-the-badge&logo=vercel" alt="Live Dashboard on Vercel">
  </a>
  <a href="https://github.com/Paoying5/fastapi-user-management">
    <img src="https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github" alt="GitHub Repository">
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/Database-PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL">
  <img src="https://img.shields.io/badge/Frontend-Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white" alt="Next.js">
  <img src="https://img.shields.io/badge/Styling-Tailwind%20CSS-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white" alt="Tailwind CSS">
  <img src="https://img.shields.io/badge/Deployment-Vercel-000000?style=flat-square&logo=vercel&logoColor=white" alt="Vercel">
</p>

---

## 📌 Table of Contents

<details open>
  <summary><strong>Click to expand</strong></summary>

- [📖 Overview](#-overview)
- [✨ Features](#-features)
- [🛠️ Tech Stack](#️-tech-stack)
- [🏗️ Architecture](#️-architecture)
- [📁 Project Structure](#-project-structure)
- [🚀 Getting Started](#-getting-started)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Set Up PostgreSQL](#2-set-up-postgresql)
  - [3. Run the FastAPI Backend](#3-run-the-fastapi-backend)
  - [4. Run the Dashboard Locally](#4-run-the-dashboard-locally)
- [📊 Analytics and Data Pipeline](#-analytics-and-data-pipeline)
- [🌐 Deployment](#-deployment)
- [🔒 Security Notes](#-security-notes)
- [🎯 Project Goals](#-project-goals)
- [👤 Author](#-author)

</details>

---

## 📖 Overview

**FastAPI User Management & Analytics Dashboard** is a project focused on backend development, database management, SQL analytics, and data visualization.

The project combines a FastAPI backend with PostgreSQL and a Next.js dashboard. The backend and SQL analytics support data processing and analysis, while the dashboard presents project progress and analytics metrics through a web interface.

The dashboard is deployed on Vercel and can be accessed online:

<p align="center">
  <a href="https://fastapi-user-management-dashboard-three.vercel.app">
    <strong>🚀 Open the Live Dashboard</strong>
  </a>
</p>

The project currently has two distinct parts:

- **Backend:** FastAPI and PostgreSQL, used for backend development and database operations.
- **Dashboard:** Next.js, used to present project progress and analytics information.

> **Important:** The dashboard is deployed online, but its analytics are generated from project files and JSON snapshots. It is not currently a live dashboard directly querying the FastAPI backend or PostgreSQL database. The displayed figures represent the available snapshot data, not guaranteed real-time database values.

---

## ✨ Features

### 🔹 Backend Development

- Build REST API functionality using FastAPI.
- Work with PostgreSQL for relational data storage.
- Run the database locally with Docker Compose.
- Access interactive API documentation through Swagger UI when the backend is running.
- Organize SQL analytics queries for data exploration and reporting.

### 🔹 SQL Analytics

- Analyze user and post data using SQL.
- Calculate overall data metrics.
- Evaluate the contribution of top creators to total post volume.
- Store verified KPI values in a dedicated JSON snapshot.
- Validate snapshot values against the analytics totals during dashboard data generation.

### 🔹 Analytics Dashboard

- Present project progress and summary statistics.
- Display user and post metrics.
- Visualize analytics data with charts.
- Generate progress data from project diaries, SQL analytics files, and JSON snapshots.
- Calculate the top-creator post share from verified KPI snapshot values.
- Build the dashboard automatically through the Next.js build process.

### 🔹 Online Deployment

- Deploy the Next.js dashboard to Vercel.
- Access the dashboard through a public URL.
- Maintain the backend and dashboard as separate components.
- Build and validate the dashboard locally before deployment.

---

## 🛠️ Tech Stack

| Category | Technology |
|---|---|
| Backend | Python, FastAPI |
| Database | PostgreSQL |
| Database Environment | Docker Compose |
| Query Language | SQL |
| Frontend Framework | Next.js |
| UI Library | React |
| Styling | Tailwind CSS v4 |
| Charts | Recharts |
| Data Pipeline | Node.js scripts and JSON snapshots |
| Frontend Deployment | Vercel |
| Version Control | Git and GitHub |

---

## 🏗️ Architecture

The project separates backend services, analytics resources, and dashboard presentation.

```text
                         ┌──────────────────────────┐
                         │        GitHub Repo       │
                         │  Source Code & SQL Files │
                         └────────────┬─────────────┘
                                      │
                 ┌────────────────────┴────────────────────┐
                 │                                         │
                 ▼                                         ▼
       ┌───────────────────┐                    ┌────────────────────┐
       │   FastAPI Backend │                    │   Analytics Files  │
       │                   │                    │                    │
       │   REST API        │                    │   SQL Queries      │
       │   Python          │                    │   Project Diaries  │
       └─────────┬─────────┘                    │   JSON Snapshots   │
                 │                              └─────────┬──────────┘
                 ▼                                        │
       ┌───────────────────┐                              ▼
       │    PostgreSQL     │                    ┌────────────────────┐
       │                   │                    │  Data Sync Script  │
       │    Database       │                    │ sync-progress.mjs  │
       └───────────────────┘                    └─────────┬──────────┘
                                                          │
                                                          ▼
                                                ┌────────────────────┐
                                                │    Next.js Build   │
                                                │                    │
                                                │ Generated Progress │
                                                │ Analytics Dashboard│
                                                └─────────┬──────────┘
                                                          │
                                                          ▼
                                                ┌────────────────────┐
                                                │       Vercel       │
                                                │   Online Dashboard │
                                                └────────────────────┘
```

### How the data flow works

1. The backend uses PostgreSQL for database operations.
2. SQL files contain queries used for analytics.
3. Project diaries and JSON snapshots provide the source data for the dashboard's progress and KPI summaries.
4. The `sync-progress.mjs` script reads and validates the available sources.
5. The script generates `progress.generated.json` for the dashboard.
6. The Next.js build process generates the production dashboard.
7. Vercel hosts the deployed frontend.

The current data pipeline generates dashboard data from project files. It does not automatically execute SQL against the production database or establish a live connection between Vercel and PostgreSQL.

---

## 📁 Project Structure

The repository contains the backend, database configuration, analytics resources, and the dashboard application.

```text
fastapi-user-management/
│
├── docs/
│   └── diary/
│       └── ...                         # Project progress and development notes
│
├── sql/
│   └── analytics/
│       ├── 03_kpi_analysis.sql         # KPI analysis queries
│       └── ...                         # Other analytics SQL files
│
├── mentor-web/
│   ├── scripts/
│   │   └── sync-progress.mjs           # Generates and validates dashboard data
│   │
│   ├── src/
│   │   ├── app/
│   │   │   └── page.tsx                # Dashboard page
│   │   │
│   │   └── data/
│   │       ├── analytics-kpi.snapshot.json
│   │       ├── monthly-posts.snapshot.json
│   │       └── progress.generated.json # Generated file; not committed
│   │
│   ├── package.json
│   └── ...
│
├── docker-compose.yml                  # Local service configuration
├── README.md
└── ...                                 # Existing backend source and configuration
```

**Notes:**

- `mentor-web/` contains the Next.js dashboard.
- `sql/analytics/` contains the SQL analytics queries.
- `docs/diary/` contains project development notes used by the progress pipeline.
- `analytics-kpi.snapshot.json` stores verified analytics values used by the dashboard.
- `progress.generated.json` is generated by the sync script and is intentionally excluded from Git.
- Sensitive configuration files, such as `.env`, should remain local and must not be committed.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Paoying5/fastapi-user-management.git
cd fastapi-user-management
```

### 2. Set Up PostgreSQL

The project uses Docker Compose to run PostgreSQL locally.

Start the PostgreSQL service:

```bash
docker compose up -d postgres
```

Check the running services:

```bash
docker compose ps
```

Connect to the database:

```bash
docker compose exec postgres psql -U admin -d fastapi_db
```

To exit the PostgreSQL command-line interface:

```sql
\q
```

The database container is configured to expose PostgreSQL on host port `5433`, mapped to container port `5432`.

Use the connection settings defined by your local Docker Compose and environment configuration when connecting from a local application.

### 3. Run the FastAPI Backend

Create a Python virtual environment from the repository root:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Activate it on macOS or Linux:

```bash
source .venv/bin/activate
```

Install the backend dependencies using the dependency file provided by the project:

```bash
pip install -r requirements.txt
```

Start the FastAPI application using the entry point configured in the backend. For example, if the FastAPI instance is named `app` in the root-level `main.py` file:

```bash
uvicorn main:app --reload
```

Once the backend is running, open the interactive API documentation:

- **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

> If your FastAPI entry point or dependency file is located elsewhere, use the path and command defined by the existing backend structure.

### 4. Run the Dashboard Locally

Open a new terminal and move to the dashboard directory:

```bash
cd mentor-web
```

Install the frontend dependencies:

```bash
npm install
```

Run the data synchronization script:

```bash
npm run sync-progress
```

Start the development server:

```bash
npm run dev
```

Open the dashboard in your browser:

[http://localhost:3000](http://localhost:3000)

#### Validate the Dashboard

Run the linter:

```bash
npm run lint
```

Build the production version:

```bash
npm run build
```

The build process runs the configured prebuild step, which synchronizes the dashboard data before compiling the Next.js application.

You can also check for whitespace errors in Git changes from the repository root:

```bash
git diff --check
```

---

## 📊 Analytics and Data Pipeline

The dashboard uses a data synchronization process to combine project progress information and verified analytics values.

### Data Sources

| Source | Purpose |
|---|---|
| `docs/diary/` | Project progress and development records |
| `sql/analytics/` | SQL analytics queries |
| `monthly-posts.snapshot.json` | Monthly post data used by the dashboard |
| `analytics-kpi.snapshot.json` | Verified KPI values used for analytics calculations |
| `sync-progress.mjs` | Reads, validates, and generates dashboard data |
| `progress.generated.json` | Generated dashboard progress data |

### KPI Snapshot

The file `mentor-web/src/data/analytics-kpi.snapshot.json` stores the verified values used for the top-creator KPI.

Current snapshot:

| Metric | Value |
|---|---:|
| Total users | 600 |
| Total posts | 2,250 |
| Posts attributed to the top 10% creator group | 870 |
| Post share of the top 10% creator group | 38.67% |

The KPI snapshot identifies its source as:

```text
sql/analytics/03_kpi_analysis.sql - KPI 7
```

The snapshot's verification date is `2026-10-25`.

### How the KPI Is Calculated

The dashboard calculates the top-creator post share from the snapshot values:

\[
\text{Top Creator Share}
=
\frac{\text{Top 10\% Posts}}{\text{All Posts}}
\times 100
\]

Using the current snapshot:

\[
\frac{870}{2250}\times 100 = 38.67\%
\]

The calculation is performed by the synchronization script rather than relying on a separately hardcoded percentage.

### Data Validation

The `sync-progress.mjs` script validates the KPI snapshot before generating dashboard data.

The validation process checks that:

- Required KPI fields are available.
- The snapshot's user total matches the extracted analytics user total.
- The snapshot's post total matches the extracted analytics post total.
- The top-creator share is calculated from the validated post counts.

If a required value or consistency check fails, the synchronization process should report the problem rather than silently generating a misleading KPI.

### Regenerate the Dashboard Data

From the `mentor-web/` directory, run:

```bash
npm run sync-progress
```

Then validate and build the dashboard:

```bash
npm run lint
npm run build
```

**Important:** The generated file `progress.generated.json` should not be edited manually. Update the relevant source data or snapshot, then run the synchronization script again.

The snapshot values should be refreshed and reverified whenever the underlying analytics data changes. The dashboard does not automatically retrieve updated PostgreSQL records simply because the site is deployed on Vercel.

---

## 🌐 Deployment

### Dashboard Deployment — Vercel

The Next.js dashboard is deployed online on Vercel.

<p align="center">
  <a href="https://fastapi-user-management-dashboard-three.vercel.app">
    <img src="https://img.shields.io/badge/Visit%20Dashboard-paoying--data.vercel.app-black?style=for-the-badge&logo=vercel" alt="Visit the online dashboard">
  </a>
</p>

**Live URL:** [https://fastapi-user-management-dashboard-three.vercel.app](https://fastapi-user-management-dashboard-three.vercel.app)

The dashboard source code is located in the `mentor-web/` directory.

For a Vercel project connected to this repository, use the following configuration:

| Setting | Value |
|---|---|
| Framework Preset | Next.js |
| Root Directory | `mentor-web` |
| Install Command | `npm install` |
| Build Command | `npm run build` |

The build process uses the configured prebuild script to synchronize the progress data before creating the production build.

After deployment, open the live URL to verify that the dashboard loads and displays its available analytics data correctly.

### Backend Deployment

The online dashboard and FastAPI backend are separate components.

The dashboard's Vercel URL is **not** a public FastAPI API URL. A public backend endpoint should only be documented here after the FastAPI service has been deployed and its URL verified.

For local backend development, use the setup instructions in the [Getting Started](#-getting-started) section.

---

## 🔒 Security Notes

Follow these practices when developing or deploying the project:

- Do not commit `.env` files, passwords, database URLs, API keys, or other secrets.
- Keep local database credentials separate from frontend configuration.
- Do not expose PostgreSQL credentials to browser-side code.
- Do not place private database credentials in `NEXT_PUBLIC_*` environment variables.
- Do not assume that a static analytics snapshot represents real-time database data.
- Validate and refresh snapshots before publishing updated analytics.
- Use environment variables and the deployment platform's secret-management features for sensitive configuration.

The frontend should consume only data that is appropriate for public display.

---

## 🎯 Project Goals

This project supports practical learning and development in several areas:

- **Backend development:** Building and running a FastAPI application.
- **Database management:** Working with PostgreSQL and Docker Compose.
- **SQL analytics:** Writing and validating queries for user and post metrics.
- **Data processing:** Transforming source files and snapshots into dashboard-ready data.
- **Frontend development:** Building a Next.js dashboard with React, Tailwind CSS, and Recharts.
- **Data visualization:** Presenting metrics and project progress in a web interface.
- **Deployment:** Publishing the dashboard to Vercel.
- **Code quality:** Validating data, running lint checks, and testing production builds.

The project can be extended in the future to connect the dashboard to a deployed backend API, enabling analytics to be retrieved dynamically rather than from static snapshots.

---

## 👤 Author

**Paoying5**

- GitHub: [@Paoying5](https://github.com/Paoying5)
- Repository: [fastapi-user-management](https://github.com/Paoying5/fastapi-user-management)
- Live Dashboard: [fastapi-user-management-dashboard-three.vercel.app](https://fastapi-user-management-dashboard-three.vercel.app)

---

<p align="center">
  <strong>Built with FastAPI, PostgreSQL, Next.js, and a focus on practical backend and analytics development.</strong>
</p>
```


---

## `alembic.ini`

```ini
# A generic, single database configuration.

[alembic]
# path to migration scripts.
# this is typically a path given in POSIX (e.g. forward slashes)
# format, relative to the token %(here)s which refers to the location of this
# ini file
script_location = %(here)s/alembic

# template used to generate migration file names; The default value is %%(rev)s_%%(slug)s
# Uncomment the line below if you want the files to be prepended with date and time
# see https://alembic.sqlalchemy.org/en/latest/tutorial.html#editing-the-ini-file
# for all available tokens
# file_template = %%(year)d_%%(month).2d_%%(day).2d_%%(hour).2d%%(minute).2d-%%(rev)s_%%(slug)s
# Or organize into date-based subdirectories (requires recursive_version_locations = true)
# file_template = %%(year)d/%%(month).2d/%%(day).2d_%%(hour).2d%%(minute).2d_%%(second).2d_%%(rev)s_%%(slug)s

# sys.path path, will be prepended to sys.path if present.
# defaults to the current working directory.  for multiple paths, the path separator
# is defined by "path_separator" below.
prepend_sys_path = .


# timezone to use when rendering the date within the migration file
# as well as the filename.
# If specified, requires the tzdata library which can be installed by adding
# `alembic[tz]` to the pip requirements.
# string value is passed to ZoneInfo()
# leave blank for localtime
# timezone =

# max length of characters to apply to the "slug" field
# truncate_slug_length = 40

# set to 'true' to run the environment during
# the 'revision' command, regardless of autogenerate
# revision_environment = false

# set to 'true' to allow .pyc and .pyo files without
# a source .py file to be detected as revisions in the
# versions/ directory
# sourceless = false

# version location specification; This defaults
# to <script_location>/versions.  When using multiple version
# directories, initial revisions must be specified with --version-path.
# The path separator used here should be the separator specified by "path_separator"
# below.
# version_locations = %(here)s/bar:%(here)s/bat:%(here)s/alembic/versions

# path_separator; This indicates what character is used to split lists of file
# paths, including version_locations and prepend_sys_path within configparser
# files such as alembic.ini.
# The default rendered in new alembic.ini files is "os", which uses os.pathsep
# to provide os-dependent path splitting.
#
# Note that in order to support legacy alembic.ini files, this default does NOT
# take place if path_separator is not present in alembic.ini.  If this
# option is omitted entirely, fallback logic is as follows:
#
# 1. Parsing of the version_locations option falls back to using the legacy
#    "version_path_separator" key, which if absent then falls back to the legacy
#    behavior of splitting on spaces and/or commas.
# 2. Parsing of the prepend_sys_path option falls back to the legacy
#    behavior of splitting on spaces, commas, or colons.
#
# Valid values for path_separator are:
#
# path_separator = :
# path_separator = ;
# path_separator = space
# path_separator = newline
#
# Use os.pathsep. Default configuration used for new projects.
path_separator = os

# set to 'true' to search source files recursively
# in each "version_locations" directory
# new in Alembic version 1.10
# recursive_version_locations = false

# the output encoding used when revision files
# are written from script.py.mako
# output_encoding = utf-8

# database URL.  This is consumed by the user-maintained env.py script only.
# other means of configuring database URLs may be customized within the env.py
# file.
sqlalchemy.url = 


[post_write_hooks]
# post_write_hooks defines scripts or Python functions that are run
# on newly generated revision scripts.  See the documentation for further
# detail and examples

# format using "black" - use the console_scripts runner, against the "black" entrypoint
# hooks = black
# black.type = console_scripts
# black.entrypoint = black
# black.options = -l 79 REVISION_SCRIPT_FILENAME

# lint with attempts to fix using "ruff" - use the module runner, against the "ruff" module
# hooks = ruff
# ruff.type = module
# ruff.module = ruff
# ruff.options = check --fix REVISION_SCRIPT_FILENAME

# Alternatively, use the exec runner to execute a binary found on your PATH
# hooks = ruff
# ruff.type = exec
# ruff.executable = ruff
# ruff.options = check --fix REVISION_SCRIPT_FILENAME

# Logging configuration.  This is also consumed by the user-maintained
# env.py script only.
[loggers]
keys = root,sqlalchemy,alembic

[handlers]
keys = console

[formatters]
keys = generic

[logger_root]
level = WARNING
handlers = console
qualname =

[logger_sqlalchemy]
level = WARNING
handlers =
qualname = sqlalchemy.engine

[logger_alembic]
level = INFO
handlers =
qualname = alembic

[handler_console]
class = StreamHandler
args = (sys.stderr,)
level = NOTSET
formatter = generic

[formatter_generic]
format = %(levelname)-5.5s [%(name)s] %(message)s
datefmt = %H:%M:%S
```


---

## `alembic/env.py`

```python
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

from dotenv import load_dotenv
import os

from app.database import Base
from app.models.user import User
from app.models.post import Post


# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

load_dotenv()

database_url = os.getenv("DATABASE_URL")

config.set_main_option(
    "sqlalchemy.url",
    database_url
)


# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
```


---

## `alembic/versions/b31f9c2a6d10_enforce_user_role_constraints.py`

```python
"""enforce user role constraints

Revision ID: b31f9c2a6d10
Revises: e7d9b8aad922
Create Date: 2026-10-07
"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op


revision: str = "b31f9c2a6d10"
down_revision: Union[str, Sequence[str], None] = "e7d9b8aad922"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    connection = op.get_bind()

    invalid_role_count = connection.execute(
        sa.text(
            """
            SELECT COUNT(*)
            FROM users
            WHERE role IS NOT NULL
              AND role NOT IN ('user', 'admin')
            """
        )
    ).scalar_one()

    if invalid_role_count > 0:
        raise RuntimeError(
            "Migration stopped because users table contains "
            "roles other than 'user' or 'admin'. "
            "Fix invalid role data before running this migration."
        )

    connection.execute(
        sa.text(
            """
            UPDATE users
            SET role = 'user'
            WHERE role IS NULL
            """
        )
    )

    op.alter_column(
        "users",
        "role",
        existing_type=sa.String(length=50),
        nullable=False,
        server_default="user",
    )

    op.create_check_constraint(
        "ck_users_role_allowed",
        "users",
        "role IN ('user', 'admin')",
    )


def downgrade() -> None:
    op.drop_constraint(
        "ck_users_role_allowed",
        "users",
        type_="check",
    )

    op.alter_column(
        "users",
        "role",
        existing_type=sa.String(length=50),
        nullable=True,
        server_default=None,
    )
```


---

## `alembic/versions/c42a7f91d8e3_add_lifecycle_fields.py`

```python
"""add lifecycle fields

Revision ID: c42a7f91d8e3
Revises: b31f9c2a6d10
Create Date: 2026-10-14
"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op


revision: str = "c42a7f91d8e3"

down_revision: Union[
    str,
    Sequence[str],
    None,
] = "b31f9c2a6d10"

branch_labels: Union[
    str,
    Sequence[str],
    None,
] = None

depends_on: Union[
    str,
    Sequence[str],
    None,
] = None


def upgrade() -> None:
    op.add_column(
        "users",
        sa.Column(
            "is_active",
            sa.Boolean(),
            nullable=False,
            server_default=sa.true(),
        ),
    )

    op.add_column(
        "users",
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text(
                "CURRENT_TIMESTAMP"
            ),
        ),
    )

    op.add_column(
        "users",
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text(
                "CURRENT_TIMESTAMP"
            ),
        ),
    )

    op.add_column(
        "users",
        sa.Column(
            "last_login_at",
            sa.DateTime(timezone=True),
            nullable=True,
        ),
    )

    op.add_column(
        "posts",
        sa.Column(
            "status",
            sa.String(length=20),
            nullable=False,
            server_default=sa.text(
                "'published'"
            ),
        ),
    )

    op.add_column(
        "posts",
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text(
                "CURRENT_TIMESTAMP"
            ),
        ),
    )

    op.add_column(
        "posts",
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text(
                "CURRENT_TIMESTAMP"
            ),
        ),
    )

    op.create_check_constraint(
        "ck_posts_status_allowed",
        "posts",
        (
            "status IN "
            "('draft', 'published', 'archived')"
        ),
    )


def downgrade() -> None:
    op.drop_constraint(
        "ck_posts_status_allowed",
        "posts",
        type_="check",
    )

    op.drop_column(
        "posts",
        "updated_at",
    )

    op.drop_column(
        "posts",
        "created_at",
    )

    op.drop_column(
        "posts",
        "status",
    )

    op.drop_column(
        "users",
        "last_login_at",
    )

    op.drop_column(
        "users",
        "updated_at",
    )

    op.drop_column(
        "users",
        "created_at",
    )

    op.drop_column(
        "users",
        "is_active",
    )
```


---

## `alembic/versions/e7d9b8aad922_initial_schema.py`

```python
"""initial schema

Revision ID: e7d9b8aad922
Revises: 
Create Date: 2026-08-29 00:21:19.332855

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e7d9b8aad922'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('role', sa.String(length=50), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('full_name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_posts_id'), 'posts', ['id'], unique=False)
    op.create_index(op.f('ix_posts_user_id'), 'posts', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_posts_user_id'), table_name='posts')
    op.drop_index(op.f('ix_posts_id'), table_name='posts')
    op.drop_table('posts')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
```


---

## `analytics/__init__.py`

```python

```


---

## `analytics/charts.py`

```python
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.figure import Figure

from analytics.post_analysis import top_users_by_posts


def plot_users_by_role(
    df: pd.DataFrame,
) -> Figure:
    """
    Create a bar chart showing the number of users for each role.
    """
    if "role" not in df.columns:
        raise ValueError(
            "DataFrame must contain a 'role' column"
        )

    counts = (
        df["role"]
        .fillna("unknown")
        .value_counts()
    )

    fig, ax = plt.subplots()

    ax.bar(
        counts.index,
        counts.values,
    )

    ax.set_title("Number of Users by Role")
    ax.set_xlabel("Role")
    ax.set_ylabel("Number of Users")

    fig.tight_layout()

    return fig


def plot_age_distribution(
    df: pd.DataFrame,
) -> Figure:
    """
    Create an age histogram from a DataFrame that already contains
    an 'age' column.

    The current User database model does not provide age data,
    so this helper is not used by the FastAPI analytics endpoint.
    """
    if "age" not in df.columns:
        raise ValueError(
            "DataFrame must contain an 'age' column"
        )

    ages = df["age"].dropna()

    fig, ax = plt.subplots()

    ax.hist(
        ages,
        bins=10,
    )

    ax.set_title("User Age Distribution")
    ax.set_xlabel("Age")
    ax.set_ylabel("Number of Users")

    fig.tight_layout()

    return fig


def plot_top_users_by_posts(
    users_df: pd.DataFrame,
    posts_df: pd.DataFrame,
    limit: int = 10,
) -> Figure:
    """
    Create a bar chart of users with the highest number of posts.
    """
    if limit < 1:
        raise ValueError(
            "limit must be greater than or equal to 1"
        )

    top_users = top_users_by_posts(
        users_df=users_df,
        posts_df=posts_df,
        limit=limit,
    )

    fig, ax = plt.subplots()

    ax.bar(
        top_users["name"],
        top_users["post_count"],
    )

    ax.set_title(
        "Top Users by Number of Posts"
    )
    ax.set_xlabel("User")
    ax.set_ylabel("Number of Posts")

    ax.tick_params(
        axis="x",
        labelrotation=45,
    )

    fig.tight_layout()

    return fig
```


---

## `analytics/post_analysis.py`

```python
import pandas as pd
import numpy as np
from sqlalchemy import select

from app.models.post import Post


def get_posts_dataframe(session):
    posts = session.scalars(
        select(Post)
    ).all()

    data = []

    for post in posts:
        data.append(
            {
                "id": post.id,
                "title": post.title,
                "content": post.content,
                "user_id": post.user_id,
            }
        )

    return pd.DataFrame(data)

# Đếm số Post của từng User
def posts_per_user(df: pd.DataFrame):
    return (
        df["user_id"]
        .value_counts()
        .rename_axis("user_id")
        .reset_index(name="post_count")
    )
# tính thống kê Post

def calculate_post_statistics(df: pd.DataFrame):
    counts = (
        df["user_id"]
        .value_counts()
        .to_numpy()
    )

    if len(counts) == 0:
        return {
            "total_posts": 0,
            "average_posts_per_user": 0,
            "max_posts_by_one_user": 0,
            "min_posts_by_one_user": 0,
            "std": 0,
        }

    return {
        "total_posts": int(len(df)),
        "average_posts_per_user": float(
            np.mean(counts)
        ),
        "max_posts_by_one_user": int(
            np.max(counts)
        ),
        "min_posts_by_one_user": int(
            np.min(counts)
        ),
        "std": float(
            np.std(counts)
        ),
    }


def merge_users_posts(
    users_df: pd.DataFrame,
    posts_df: pd.DataFrame,
):
    post_counts = (
        posts_df["user_id"]
        .value_counts()
        .rename_axis("id")
        .reset_index(name="post_count")
    )

    result = users_df.merge(
        post_counts,
        on="id",
        how="left",
    )

    result["post_count"] = (
        result["post_count"]
        .fillna(0)
        .astype(int)
    )

    return result


def top_users_by_posts(
    users_df: pd.DataFrame,
    posts_df: pd.DataFrame,
    limit: int = 10,
):
    merged = merge_users_posts(
        users_df,
        posts_df,
    )

    return (
        merged
        .sort_values(
            "post_count",
            ascending=False,
        )
        .head(limit)
    )


def posts_by_role(
    users_df: pd.DataFrame,
    posts_df: pd.DataFrame,
):
    merged = merge_users_posts(
        users_df,
        posts_df,
    )

    return (
        merged
        .groupby("role")["post_count"]
        .sum()
        .reset_index()
    )
```


---

## `analytics/user_analysis.py`

```python
import pandas as pd
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User


def get_users_dataframe(
    session: Session,
) -> pd.DataFrame:
    """
    Load the currently supported User fields into a DataFrame.

    This function intentionally uses only columns that actually exist
    in the current SQLAlchemy User model.
    """
    users = session.scalars(
        select(User)
    ).all()

    data = [
        {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "role": user.role,
            "full_name": user.full_name,
        }
        for user in users
    ]

    return pd.DataFrame(
        data,
        columns=[
            "id",
            "name",
            "email",
            "role",
            "full_name",
        ],
    )


def count_users(
    df: pd.DataFrame,
) -> int:
    return len(df)


def users_by_role(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Count users grouped by role.

    Null roles are grouped as 'unknown' so analytics does not silently
    discard those records.
    """
    if df.empty:
        return pd.DataFrame(
            columns=[
                "role",
                "user_count",
            ]
        )

    role_counts = (
        df["role"]
        .fillna("unknown")
        .value_counts()
        .rename_axis("role")
        .reset_index(name="user_count")
    )

    return role_counts
```


---

## `app/__init__.py`

```python

```


---

## `app/constants.py`

```python
# ADMIN

#USER

#MODERATOR

# không hard-code.
```


---

## `app/core/config.py`

```python
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    DATABASE_URL: str

    SECRET_KEY: str

    ALGORITHM: str = "HS256"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 120


    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

class Config:
        env_file = ".env"


settings = Settings()
```


---

## `app/core/exceptions.py`

```python
class ApplicationError(Exception):
    """Base exception for application/business errors."""

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class ResourceNotFoundError(ApplicationError):
    """Requested resource does not exist."""


class PermissionDeniedError(ApplicationError):
    """Authenticated user is not allowed to perform the action."""


class ConflictError(ApplicationError):
    """Operation conflicts with the current resource state."""
```


---

## `app/core/logging.py`

```python

```


---

## `app/core/security.py`

```python
from datetime import datetime, timedelta, timezone

from jose import jwt
from pwdlib import PasswordHash

from app.core.config import settings


password_hash = PasswordHash.recommended()


def hash_password(password: str) -> str:
    return password_hash.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str,
) -> bool:
    return password_hash.verify(
        plain_password,
        hashed_password,
    )


def create_access_token(data: dict) -> str:
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update(
        {
            "exp": expire,
        }
    )

    encoded_jwt = jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )

    return encoded_jwt
```


---

## `app/database.py`

```python
from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

from app.core.config import settings


engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()


def get_db() -> Generator[Session, None, None]:
    """
    Create one SQLAlchemy Session for one request.

    The session is always closed after the request finishes,
    including when an exception occurs.
    """
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
```


---

## `app/dependencies.py`

```python
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from app.core.config import settings
from app.database import get_db
from app.models import User, user
from app.services.auth_service import AuthService
from app.services.post_service import PostService
from app.services.user_service import UserService


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login",
)


def get_user_service(
    db: Session = Depends(get_db),
) -> UserService:
    return UserService(db)


def get_post_service(
    db: Session = Depends(get_db),
) -> PostService:
    return PostService(db)


def get_auth_service(
    db: Session = Depends(get_db),
) -> AuthService:
    return AuthService(db)


def get_current_user(
    token: str = Depends(oauth2_scheme),
    service: AuthService = Depends(get_auth_service),
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={
            "WWW-Authenticate": "Bearer",
        },
    )

    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM],
        )

        subject = payload.get("sub")

        if not isinstance(subject, str) or not subject:
            raise credentials_exception

    except JWTError as exc:
        raise credentials_exception from exc

    # New token format:
    # sub = string representation of user.id
    if subject.isdigit():
        user = service.get_user_by_id(
            int(subject)
        )

    # Backward compatibility:
    # old tokens used email as the JWT subject.
    else:
        user = service.get_user_by_email(
            subject
        )

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Inactive user",
        )

    return user


def get_admin_user(
    current_user: User = Depends(get_current_user),
) -> User:
    if current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required",
        )

    return current_user
```


---

## `app/main.py`

```python
from fastapi import (
    FastAPI,
    Request,
    status,
)
from fastapi.responses import JSONResponse

from app.core.exceptions import (
    ConflictError,
    PermissionDeniedError,
    ResourceNotFoundError,
)
from app.routers import (
    analytics,
    auth,
    health,
    post,
    user,
)


app = FastAPI(
    title="FastAPI User Management",
    version="0.2.0",
    description=(
        "User and post management API built with "
        "FastAPI, SQLAlchemy, PostgreSQL and JWT."
    ),
)


@app.exception_handler(
    ResourceNotFoundError
)
async def resource_not_found_handler(
    request: Request,
    exc: ResourceNotFoundError,
):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "detail": exc.message,
        },
    )


@app.exception_handler(
    PermissionDeniedError
)
async def permission_denied_handler(
    request: Request,
    exc: PermissionDeniedError,
):
    return JSONResponse(
        status_code=status.HTTP_403_FORBIDDEN,
        content={
            "detail": exc.message,
        },
    )


@app.exception_handler(
    ConflictError
)
async def conflict_handler(
    request: Request,
    exc: ConflictError,
):
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={
            "detail": exc.message,
        },
    )


app.include_router(
    health.router
)

app.include_router(
    auth.router
)

app.include_router(
    user.router
)

app.include_router(
    post.router
)

app.include_router(
    analytics.router
)


@app.get(
    "/",
    tags=["Default"],
)
def root():
    return {
        "message": (
            "FastAPI User Management is running"
        ),
        "docs": "/docs",
        "health": "/health",
    }
```


---

## `app/models/__init__.py`

```python
from app.models.user import User
from app.models.post import Post

__all__ = [
    "User",
    "Post",
]
```


---

## `app/models/post.py`

```python
from sqlalchemy import (
    CheckConstraint,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
    func,
    text,
)
from sqlalchemy.orm import relationship

from app.database import Base


class Post(Base):
    __tablename__ = "posts"

    __table_args__ = (
        CheckConstraint(
            "status IN "
            "('draft', 'published', 'archived')",
            name="ck_posts_status_allowed",
        ),
    )

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    title = Column(
        String(255),
        nullable=False,
    )

    content = Column(
        Text,
        nullable=True,
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
        index=True,
    )

    status = Column(
        String(20),
        nullable=False,
        default="published",
        server_default=text("'published'"),
    )

    created_at = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )

    updated_at = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )

    owner = relationship(
        "User",
        back_populates="posts",
    )
```


---

## `app/models/user.py`

```python
from sqlalchemy import (
    Boolean,
    CheckConstraint,
    Column,
    DateTime,
    Integer,
    String,
    func,
    text,
)
from sqlalchemy.orm import relationship

from app.database import Base


class User(Base):
    __tablename__ = "users"

    __table_args__ = (
        CheckConstraint(
            "role IN ('user', 'admin')",
            name="ck_users_role_allowed",
        ),
    )

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    name = Column(
        String(100),
        nullable=False,
    )

    email = Column(
        String(100),
        unique=True,
        nullable=False,
        index=True,
    )

    role = Column(
        String(50),
        nullable=False,
        default="user",
        server_default=text("'user'"),
    )

    password = Column(
        String(255),
        nullable=False,
    )

    full_name = Column(
        String(100),
        nullable=True,
    )

    is_active = Column(
        Boolean,
        nullable=False,
        default=True,
        server_default=text("true"),
    )

    created_at = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )

    updated_at = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )

    last_login_at = Column(
        DateTime(timezone=True),
        nullable=True,
    )

    posts = relationship(
        "Post",
        back_populates="owner",
        cascade="all, delete-orphan",
    )
```


---

## `app/repositories/__init__.py`

```python

```


---

## `app/repositories/post_repository.py`

```python
from sqlalchemy import (
    desc,
    func,
    select,
)
from sqlalchemy.orm import (
    Session,
    joinedload,
)

from app.models.post import Post


class PostRepository:
    """Persistence operations for Post entities."""

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def get_all(
        self,
        limit: int = 10,
        offset: int = 0,
        search: str = "",
    ) -> list[Post]:
        statement = (
            select(Post)
            .options(
                joinedload(
                    Post.owner
                )
            )
        )

        if search:
            statement = (
                statement.where(
                    Post.title.ilike(
                        f"%{search}%"
                    )
                )
            )

        statement = (
            statement
            .order_by(
                desc(Post.id)
            )
            .offset(offset)
            .limit(limit)
        )

        return list(
            self.db.scalars(
                statement
            ).all()
        )

    def count(
        self,
        search: str = "",
    ) -> int:
        statement = (
            select(
                func.count()
            )
            .select_from(Post)
        )

        if search:
            statement = (
                statement.where(
                    Post.title.ilike(
                        f"%{search}%"
                    )
                )
            )

        result = self.db.scalar(
            statement
        )

        return int(
            result or 0
        )

    def get_by_id(
        self,
        post_id: int,
    ) -> Post | None:
        statement = (
            select(Post)
            .options(
                joinedload(
                    Post.owner
                )
            )
            .where(
                Post.id
                == post_id
            )
        )

        return (
            self.db
            .scalars(statement)
            .first()
        )

    def get_by_user_id(
        self,
        user_id: int,
    ) -> list[Post]:
        statement = (
            select(Post)
            .options(
                joinedload(
                    Post.owner
                )
            )
            .where(
                Post.user_id
                == user_id
            )
            .order_by(
                desc(Post.id)
            )
        )

        return list(
            self.db.scalars(
                statement
            ).all()
        )

    def add(
        self,
        post: Post,
    ) -> Post:
        self.db.add(post)
        self.db.flush()
        self.db.refresh(post)

        return post

    def update(
        self,
        post: Post,
    ) -> Post:
        self.db.flush()
        self.db.refresh(post)

        return post

    def delete(
        self,
        post: Post,
    ) -> None:
        self.db.delete(post)
        self.db.flush()
```


---

## `app/repositories/user_repository.py`

```python
from sqlalchemy import (
    asc,
    func,
    or_,
    select,
)
from sqlalchemy.orm import (
    Session,
    joinedload,
    selectinload,
)

from app.models.user import User


class UserRepository:
    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def get_all(
        self,
        limit: int = 10,
        offset: int = 0,
        search: str = "",
    ) -> list[User]:
        statement = (
            select(User)
            .options(
                selectinload(
                    User.posts
                )
            )
        )

        if search:
            pattern = (
                f"%{search}%"
            )

            statement = (
                statement.where(
                    or_(
                        User.name.ilike(
                            pattern
                        ),
                        User.email.ilike(
                            pattern
                        ),
                    )
                )
            )

        statement = (
            statement
            .order_by(
                asc(User.id)
            )
            .offset(offset)
            .limit(limit)
        )

        return list(
            self.db.scalars(
                statement
            ).all()
        )

    def count(
        self,
        search: str = "",
    ) -> int:
        statement = (
            select(
                func.count()
            )
            .select_from(User)
        )

        if search:
            pattern = (
                f"%{search}%"
            )

            statement = (
                statement.where(
                    or_(
                        User.name.ilike(
                            pattern
                        ),
                        User.email.ilike(
                            pattern
                        ),
                    )
                )
            )

        result = self.db.scalar(
            statement
        )

        return int(
            result or 0
        )

    def get_by_id(
        self,
        user_id: int,
    ) -> User | None:
        statement = (
            select(User)
            .options(
                joinedload(
                    User.posts
                )
            )
            .where(
                User.id
                == user_id
            )
        )

        return (
            self.db
            .scalars(statement)
            .unique()
            .first()
        )

    def get_by_email(
        self,
        email: str,
    ) -> User | None:
        statement = (
            select(User)
            .where(
                User.email
                == email
            )
        )

        return (
            self.db
            .scalars(statement)
            .first()
        )

    def add(
        self,
        user: User,
    ) -> User:
        self.db.add(user)
        self.db.flush()
        self.db.refresh(user)

        return user

    def update(
        self,
        user: User,
    ) -> User:
        self.db.flush()
        self.db.refresh(user)

        return user

    def delete(
        self,
        user: User,
    ) -> None:
        self.db.delete(user)
        self.db.flush()
```


---

## `app/routers/__init__.py`

```python

```


---

## `app/routers/analytics.py`

```python
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from analytics.user_analysis import (
    count_users,
    get_users_dataframe,
    users_by_role,
)
from app.dependencies import (
    get_admin_user,
    get_db,
)
from app.models import User
from app.schemas import APIResponse
from app.utils.response import response


router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"],
)


@router.get(
    "/users/summary",
    response_model=APIResponse,
    summary="Get user analytics summary",
)
def user_summary(
    db: Session = Depends(get_db),
    admin: User = Depends(get_admin_user),
) -> dict:
    """
    Return basic user statistics.

    Access is restricted to admin users.
    """
    users_df = get_users_dataframe(db)

    role_counts = users_by_role(
        users_df
    )

    data = {
        "total_users": count_users(
            users_df
        ),
        "users_by_role": role_counts.to_dict(
            orient="records"
        ),
    }

    return response(
        "User analytics retrieved successfully",
        data,
    )
```


---

## `app/routers/auth.py`

```python
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from app.dependencies import get_auth_service, get_current_user
from app.models import User
from app.schemas import Token, UserResponse
from app.services.auth_service import AuthService


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/login",
    response_model=Token,
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    service: AuthService = Depends(get_auth_service),
) -> Token:

    token = service.login(
        form_data.username,
        form_data.password,
    )

    if token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
            headers={
                "WWW-Authenticate": "Bearer",
            },
        )

    return token


@router.get(
    "/me",
    response_model=UserResponse,
)
def read_me(
    current_user: User = Depends(get_current_user),
) -> User:
    return current_user
```


---

## `app/routers/health.py`

```python
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.dependencies import get_db


router = APIRouter(
    tags=["Health"],
)


@router.get("/health")
def health_check(
    db: Session = Depends(get_db),
):
    try:
        db.execute(
            text("SELECT 1"),
        )

    except SQLAlchemyError as exc:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Database connection failed",
        ) from exc

    return {
        "status": "healthy",
        "api": "running",
        "database": "connected",
    }
```


---

## `app/routers/post.py`

```python
from fastapi import (
    APIRouter,
    Depends,
    Response,
    Query,
    status,
)

from app.dependencies import (
    get_current_user,
    get_post_service,
)
from app.models import User
from app.schemas import (
    MessageResponse,
    PostCreate,
    PostPatch,
    PostResponse,
    PostUpdate,
)
from app.services.post_service import PostService
from app.utils.pagination import (
    PAGINATION_HEADERS_OPENAPI,
    build_pagination_headers,
)


router = APIRouter(
    prefix="/posts",
    tags=["Posts"],
)


@router.post(
    "/",
    response_model=PostResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_post(
    post_data: PostCreate,
    service: PostService = Depends(
        get_post_service
    ),
    current_user: User = Depends(
        get_current_user
    ),
):
    return service.create_post(
        post_data,
        current_user.id,
    )

@router.get(
    "/",
    response_model=list[PostResponse],
    responses={
        200: {
            "description": (
                "Posts retrieved successfully"
            ),
            "headers":
                PAGINATION_HEADERS_OPENAPI,
        },
    },
)
def get_posts(
    http_response: Response,
    limit: int = Query(
        default=10,
        ge=1,
        le=100,
    ),
    offset: int = Query(
        default=0,
        ge=0,
    ),
    search: str = Query(
        default="",
        max_length=100,
    ),
    service: PostService = Depends(
        get_post_service
    ),
):
    posts, total = (
        service.get_posts(
            limit=limit,
            offset=offset,
            search=search,
        )
    )

    http_response.headers.update(
        build_pagination_headers(
            total=total,
            limit=limit,
            offset=offset,
        )
    )

    return posts

@router.get(
    "/me",
    response_model=list[PostResponse],
)
def get_my_posts(
    service: PostService = Depends(
        get_post_service
    ),
    current_user: User = Depends(
        get_current_user
    ),
):
    return service.get_my_posts(
        current_user.id
    )


@router.get(
    "/{post_id}",
    response_model=PostResponse,
)
def get_post(
    post_id: int,
    service: PostService = Depends(
        get_post_service
    ),
):
    return service.get_post(
        post_id
    )


@router.put(
    "/{post_id}",
    response_model=PostResponse,
)
def update_post(
    post_id: int,
    post_data: PostUpdate,
    service: PostService = Depends(
        get_post_service
    ),
    current_user: User = Depends(
        get_current_user
    ),
):
    return service.update_post(
        post_id,
        post_data,
        current_user.id,
    )


@router.patch(
    "/{post_id}",
    response_model=PostResponse,
)
def patch_post(
    post_id: int,
    post_data: PostPatch,
    service: PostService = Depends(
        get_post_service
    ),
    current_user: User = Depends(
        get_current_user
    ),
):
    return service.patch_post(
        post_id,
        post_data,
        current_user.id,
    )


@router.delete(
    "/{post_id}",
    response_model=MessageResponse,
)
def delete_post(
    post_id: int,
    service: PostService = Depends(
        get_post_service
    ),
    current_user: User = Depends(
        get_current_user
    ),
):
    service.delete_post(
        post_id,
        current_user.id,
    )

    return MessageResponse(
        message="Post deleted successfully"
    )
```


---

## `app/routers/user.py`

```python
from fastapi import (
    APIRouter,
    Depends,
    Query,
    Response,
    status,
)

from app.dependencies import (
    get_admin_user,
    get_user_service,
)
from app.models.user import User
from app.schemas import (
    APIResponse,
    UserCreate,
    UserPatch,
    UserResponse,
    UserUpdate,
)
from app.services.user_service import UserService
from app.utils.pagination import (
    PAGINATION_HEADERS_OPENAPI,
    build_pagination_headers,
)
from app.utils.response import response


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get(
    "/",
    response_model=APIResponse[
        list[UserResponse]
    ],
    summary="Get all users",
    responses={
        200: {
            "description": (
                "Users retrieved successfully"
            ),
            "headers":
                PAGINATION_HEADERS_OPENAPI,
        },
    },
)
def get_users(
    http_response: Response,
    limit: int = Query(
        default=10,
        ge=1,
        le=100,
        description=(
            "Số lượng bản ghi tối đa trả về"
        ),
    ),
    offset: int = Query(
        default=0,
        ge=0,
        description=(
            "Số lượng bản ghi bỏ qua"
        ),
    ),
    search: str = Query(
        default="",
        max_length=100,
        description=(
            "Tìm kiếm theo tên hoặc email"
        ),
    ),
    service: UserService = Depends(
        get_user_service
    ),
    _admin: User = Depends(
        get_admin_user
    ),
):
    users, total = (
        service.get_users(
            limit=limit,
            offset=offset,
            search=search,
        )
    )

    http_response.headers.update(
        build_pagination_headers(
            total=total,
            limit=limit,
            offset=offset,
        )
    )

    data = [
        UserResponse
        .model_validate(user)
        .model_dump()
        for user in users
    ]

    return response(
        "Users retrieved successfully",
        data,
    )


@router.get(
    "/{user_id}",
    response_model=APIResponse[
        UserResponse
    ],
    summary="Get user by ID",
)
def get_user(
    user_id: int,
    service: UserService = Depends(
        get_user_service
    ),
    _admin: User = Depends(
        get_admin_user
    ),
):
    user = service.get_user(
        user_id
    )

    data = (
        UserResponse
        .model_validate(user)
        .model_dump()
    )

    return response(
        "User found",
        data,
    )


@router.post(
    "/",
    response_model=APIResponse[
        UserResponse
    ],
    status_code=status.HTTP_201_CREATED,
    summary="Create user",
)
def create_user(
    user: UserCreate,
    service: UserService = Depends(
        get_user_service
    ),
):
    db_user = service.create_user(
        user
    )

    data = (
        UserResponse
        .model_validate(db_user)
        .model_dump()
    )

    return response(
        "User created successfully",
        data,
    )


@router.put(
    "/{user_id}",
    response_model=APIResponse[
        UserResponse
    ],
    summary="Replace user",
)
def update_user(
    user_id: int,
    user: UserUpdate,
    service: UserService = Depends(
        get_user_service
    ),
    _admin: User = Depends(
        get_admin_user
    ),
):
    updated_user = (
        service.update_user(
            user_id,
            user,
        )
    )

    data = (
        UserResponse
        .model_validate(
            updated_user
        )
        .model_dump()
    )

    return response(
        "User updated successfully",
        data,
    )


@router.patch(
    "/{user_id}",
    response_model=APIResponse[
        UserResponse
    ],
    summary="Partially update user",
)
def patch_user(
    user_id: int,
    user_data: UserPatch,
    service: UserService = Depends(
        get_user_service
    ),
    _admin: User = Depends(
        get_admin_user
    ),
):
    updated_user = (
        service.patch_user(
            user_id,
            user_data,
        )
    )

    data = (
        UserResponse
        .model_validate(
            updated_user
        )
        .model_dump()
    )

    return response(
        "User partially updated successfully",
        data,
    )


@router.delete(
    "/{user_id}",
    response_model=APIResponse[
        None
    ],
    summary="Delete user",
)
def delete_user(
    user_id: int,
    service: UserService = Depends(
        get_user_service
    ),
    _admin: User = Depends(
        get_admin_user
    ),
):
    service.delete_user(
        user_id
    )

    return response(
        "User deleted successfully",
        None,
    )
```


---

## `app/schemas/__init__.py`

```python
from app.schemas.auth import LoginRequest, Token
from app.schemas.common import APIResponse, MessageResponse
from app.schemas.post import (
    PostCreate,
    PostPatch,
    PostResponse,
    PostSimple,
    PostUpdate,
    UserSimple,
)
from app.schemas.user import (
    UserCreate,
    UserPatch,
    UserResponse,
    UserUpdate,
)

__all__ = [
    "APIResponse",
    "MessageResponse",
    "LoginRequest",
    "Token",
    "UserCreate",
    "UserUpdate",
    "UserPatch",
    "UserResponse",
    "PostCreate",
    "PostUpdate",
    "PostPatch",
    "PostSimple",
    "PostResponse",
    "UserSimple",
]
```


---

## `app/schemas/auth.py`

```python
from pydantic import BaseModel, EmailStr


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str 
```


---

## `app/schemas/common.py`

```python
from typing import Generic, Literal, TypeVar

from pydantic import BaseModel


T = TypeVar("T")


class APIResponse(
    BaseModel,
    Generic[T],
):
    status: Literal["success"] = "success"
    message: str
    data: T | None = None


class MessageResponse(BaseModel):
    message: str
```


---

## `app/schemas/post.py`

```python
from datetime import datetime
from typing import Annotated, Literal

from pydantic import (
    BaseModel,
    ConfigDict,
    StringConstraints,
    field_validator,
)


PostTitle = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        min_length=2,
        max_length=255,
    ),
]


PostStatus = Literal[
    "draft",
    "published",
    "archived",
]


class StrictRequestModel(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )


class PostCreate(StrictRequestModel):
    title: PostTitle
    content: str | None = None
    status: PostStatus = "published"


class PostUpdate(StrictRequestModel):
    title: PostTitle
    content: str | None = None


class PostPatch(StrictRequestModel):
    title: PostTitle | None = None
    content: str | None = None
    status: PostStatus | None = None

    @field_validator("title")
    @classmethod
    def title_cannot_be_null(
        cls,
        value,
    ):
        if value is None:
            raise ValueError(
                "title cannot be null"
            )

        return value

    @field_validator("status")
    @classmethod
    def status_cannot_be_null(
        cls,
        value,
    ):
        if value is None:
            raise ValueError(
                "status cannot be null"
            )

        return value


class PostSimple(BaseModel):
    id: int
    title: str

    model_config = ConfigDict(
        from_attributes=True,
    )


class UserSimple(BaseModel):
    id: int
    name: str
    email: str

    model_config = ConfigDict(
        from_attributes=True,
    )


class PostResponse(BaseModel):
    id: int
    title: str
    content: str | None
    user_id: int

    status: PostStatus
    created_at: datetime
    updated_at: datetime

    owner: UserSimple

    model_config = ConfigDict(
        from_attributes=True,
    )
```


---

## `app/schemas/user.py`

```python
from typing import Annotated, Literal
from datetime import datetime
from pydantic import (
    BaseModel,
    ConfigDict,
    EmailStr,
    Field,
    StringConstraints,
    field_validator,
)

from app.schemas.post import PostSimple


UserRole = Literal[
    "user",
    "admin",
]

UserName = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        min_length=2,
        max_length=100,
    ),
]

FullName = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        max_length=100,
    ),
]


class StrictRequestModel(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )


class UserCreate(StrictRequestModel):
    name: UserName

    email: EmailStr

    password: str = Field(
        min_length=6,
        max_length=128,
    )

    full_name: FullName | None = None


class UserUpdate(StrictRequestModel):
    name: UserName

    email: EmailStr

    role: UserRole

    full_name: FullName | None = None


class UserPatch(StrictRequestModel):
    name: UserName | None = None

    email: EmailStr | None = None

    role: UserRole | None = None

    full_name: FullName | None = None

    is_active: bool | None = None

    @field_validator(
        "name",
        "email",
        "role",
    )
    @classmethod
    def non_nullable_fields_cannot_be_null(
        cls,
        value,
    ):
        if value is None:
            raise ValueError(
                "Field cannot be null"
            )

        return value


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: UserRole
    full_name: str | None = None

    is_active: bool
    created_at: datetime
    updated_at: datetime
    last_login_at: datetime | None = None

    posts: list[PostSimple] = Field(
        default_factory=list,
    )

    model_config = ConfigDict(
        from_attributes=True,
    )
```


---

## `app/services/__init__.py`

```python

```


---

## `app/services/auth_service.py`

```python
from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.core.security import (
    create_access_token,
    verify_password,
)
from app.models.user import User
from app.repositories.user_repository import (
    UserRepository,
)
from app.schemas.auth import Token


class AuthService:
    """Authentication business rules."""

    def __init__(
        self,
        db: Session,
    ):
        self.db = db
        self.repository = UserRepository(
            db
        )

    def authenticate_user(
        self,
        email: str,
        password: str,
    ) -> User | None:
        email = email.strip().lower()

        user = self.repository.get_by_email(
            email
        )

        if user is None:
            return None

        if not verify_password(
            password,
            user.password,
        ):
            return None

        if not user.is_active:
            return None

        return user

    def login(
        self,
        email: str,
        password: str,
    ) -> Token | None:
        user = self.authenticate_user(
            email,
            password,
        )

        if user is None:
            return None

        try:
            user.last_login_at = datetime.now(
                timezone.utc
            )

            self.db.commit()
            self.db.refresh(user)

        except Exception:
            self.db.rollback()
            raise

        return Token(
            access_token=create_access_token(
                {
                    "sub": str(user.id),
                }
            ),
            token_type="bearer",
        )

    def get_user_by_email(
        self,
        email: str,
    ) -> User | None:
        return self.repository.get_by_email(
            email.strip().lower()
        )

    def get_user_by_id(
        self,
        user_id: int,
    ) -> User | None:
        return self.repository.get_by_id(
            user_id
        )
```


---

## `app/services/post_service.py`

```python
from sqlalchemy.orm import Session

from app.core.exceptions import (
    PermissionDeniedError,
    ResourceNotFoundError,
)
from app.models.post import Post
from app.repositories.post_repository import PostRepository
from app.schemas.post import (
    PostCreate,
    PostPatch,
    PostUpdate,
)


class PostService:
    """Business rules for posts, ownership and transactions."""

    def __init__(self, db: Session):
        self.db = db
        self.repository = PostRepository(db)

    def create_post(
        self,
        post_data: PostCreate,
        user_id: int,
    ) -> Post:
        post = Post(
            title=post_data.title,
            content=post_data.content,
            status=post_data.status,
            user_id=user_id,
        )

        try:
            post = self.repository.add(post)

            self.db.commit()

            created_post = self.repository.get_by_id(
                post.id
            )

            if created_post is None:
                raise ResourceNotFoundError(
                    "Post not found after creation"
                )

            return created_post

        except Exception:
            self.db.rollback()
            raise

    def get_posts(
        self,
        limit: int = 10,
        offset: int = 0,
        search: str = "",
    ) -> tuple[list[Post], int]:
        posts = (
            self.repository.get_all(
                limit=limit,
                offset=offset,
                search=search,
            )
        )

        total = (
            self.repository.count(
                search=search
            )
        )

        return posts, total
    
    def get_my_posts(
        self,
        user_id: int,
    ) -> list[Post]:
        return self.repository.get_by_user_id(
            user_id
        )

    def get_post(
        self,
        post_id: int,
    ) -> Post:
        post = self.repository.get_by_id(
            post_id
        )

        if post is None:
            raise ResourceNotFoundError(
                "Post not found"
            )

        return post

    def update_post(
        self,
        post_id: int,
        post_data: PostUpdate,
        user_id: int,
    ) -> Post:
        post = self._get_owned_post(
            post_id,
            user_id,
        )

        post.title = post_data.title
        post.content = post_data.content

        return self._commit_update(post)

    def patch_post(
        self,
        post_id: int,
        post_data: PostPatch,
        user_id: int,
    ) -> Post:
        post = self._get_owned_post(
            post_id,
            user_id,
        )

        update_data = post_data.model_dump(
            exclude_unset=True
        )

        for field_name, value in update_data.items():
            setattr(
                post,
                field_name,
                value,
            )

        return self._commit_update(post)

    def delete_post(
        self,
        post_id: int,
        user_id: int,
    ) -> None:
        post = self._get_owned_post(
            post_id,
            user_id,
        )

        try:
            self.repository.delete(post)
            self.db.commit()

        except Exception:
            self.db.rollback()
            raise

    def _get_owned_post(
        self,
        post_id: int,
        user_id: int,
    ) -> Post:
        post = self.repository.get_by_id(
            post_id
        )

        if post is None:
            raise ResourceNotFoundError(
                "Post not found"
            )

        if post.user_id != user_id:
            raise PermissionDeniedError(
                "You do not own this post"
            )

        return post

    def _commit_update(
        self,
        post: Post,
    ) -> Post:
        try:
            post = self.repository.update(post)

            self.db.commit()
            self.db.refresh(post)

            return post

        except Exception:
            self.db.rollback()
            raise
```


---

## `app/services/user_service.py`

```python
from typing import NoReturn

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.core.exceptions import (
    ConflictError,
    ResourceNotFoundError,
)
from app.core.security import hash_password
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import (
    UserCreate,
    UserPatch,
    UserUpdate,
)


class UserService:
    def __init__(self, db: Session):
        self.db = db
        self.repository = UserRepository(db)

    def get_users(
        self,
        limit: int = 10,
        offset: int = 0,
        search: str = "",
    ) -> tuple[list[User], int]:
        users = (
            self.repository.get_all(
                limit=limit,
                offset=offset,
                search=search,
            )
        )

        total = (
            self.repository.count(
                search=search
            )
        )

        return users, total
    
    def get_user(
        self,
        user_id: int,
    ) -> User:
        user = self.repository.get_by_id(
            user_id
        )

        if user is None:
            raise ResourceNotFoundError(
                "User not found"
            )

        return user

    def create_user(
        self,
        user_data: UserCreate,
    ) -> User:
        email = self._normalize_email(
            str(user_data.email)
        )

        if (
            self.repository.get_by_email(email)
            is not None
        ):
            raise ConflictError(
                "Email already exists"
            )

        user = User(
            name=user_data.name,
            email=email,
            role="user",
            password=hash_password(
                user_data.password
            ),
            full_name=user_data.full_name,
        )

        try:
            user = self.repository.add(user)

            self.db.commit()
            self.db.refresh(user)

            return user

        except IntegrityError as exc:
            self._handle_integrity_error(exc)

        except Exception:
            self.db.rollback()
            raise

    def update_user(
        self,
        user_id: int,
        user_data: UserUpdate,
    ) -> User:
        user = self.repository.get_by_id(
            user_id
        )

        if user is None:
            raise ResourceNotFoundError(
                "User not found"
            )

        email = self._normalize_email(
            str(user_data.email)
        )

        if (
            user.email != email
            and self.repository.get_by_email(email)
            is not None
        ):
            raise ConflictError(
                "Email already exists"
            )

        user.name = user_data.name
        user.email = email
        user.role = user_data.role
        user.full_name = user_data.full_name

        return self._commit_update(user)

    def patch_user(
        self,
        user_id: int,
        user_data: UserPatch,
    ) -> User:
        user = self.repository.get_by_id(
            user_id
        )

        if user is None:
            raise ResourceNotFoundError(
                "User not found"
            )

        update_data = user_data.model_dump(
            exclude_unset=True
        )

        if (
            "email" in update_data
            and update_data["email"] is not None
        ):
            email = self._normalize_email(
                str(update_data["email"])
            )

            if (
                user.email != email
                and self.repository.get_by_email(
                    email
                )
                is not None
            ):
                raise ConflictError(
                    "Email already exists"
                )

            update_data["email"] = email

        for field_name, value in update_data.items():
            setattr(
                user,
                field_name,
                value,
            )

        return self._commit_update(user)

    def delete_user(
        self,
        user_id: int,
    ) -> None:
        user = self.repository.get_by_id(
            user_id
        )

        if user is None:
            raise ResourceNotFoundError(
                "User not found"
            )

        try:
            self.repository.delete(user)
            self.db.commit()

        except Exception:
            self.db.rollback()
            raise

    def _commit_update(
        self,
        user: User,
    ) -> User:
        try:
            user = self.repository.update(user)

            self.db.commit()
            self.db.refresh(user)

            return user

        except IntegrityError as exc:
            self._handle_integrity_error(exc)

        except Exception:
            self.db.rollback()
            raise

    @staticmethod
    def _normalize_email(
        email: str,
    ) -> str:
        return email.strip().lower()

    def _handle_integrity_error(
        self,
        exc: IntegrityError,
    ) -> NoReturn:
        self.db.rollback()

        original_error = str(
            exc.orig
        ).lower()

        diagnostic = getattr(
            exc.orig,
            "diag",
            None,
        )

        constraint_name = getattr(
            diagnostic,
            "constraint_name",
            None,
        )

        email_constraints = {
            "ix_users_email",
            "users_email_key",
        }

        is_email_conflict = (
            constraint_name in email_constraints
            or (
                "users.email" in original_error
                and (
                    "unique" in original_error
                    or "duplicate" in original_error
                )
            )
        )

        if is_email_conflict:
            raise ConflictError(
                "Email already exists"
            ) from exc

        raise exc
```


---

## `app/utils/helpers.py`

```python

```


---

## `app/utils/pagination.py`

```python
PAGINATION_HEADERS_OPENAPI = {
    "X-Total-Count": {
        "description": (
            "Total number of records matching "
            "the current filters."
        ),
        "schema": {
            "type": "integer",
        },
    },
    "X-Limit": {
        "description": (
            "Maximum number of records "
            "requested for this page."
        ),
        "schema": {
            "type": "integer",
        },
    },
    "X-Offset": {
        "description": (
            "Number of records skipped "
            "before this page."
        ),
        "schema": {
            "type": "integer",
        },
    },
    "X-Has-More": {
        "description": (
            "Whether more matching records "
            "exist after this page."
        ),
        "schema": {
            "type": "boolean",
        },
    },
}


def build_pagination_headers(
    *,
    total: int,
    limit: int,
    offset: int,
) -> dict[str, str]:
    has_more = (
        offset + limit
        < total
    )

    return {
        "X-Total-Count": str(total),
        "X-Limit": str(limit),
        "X-Offset": str(offset),
        "X-Has-More": (
            "true"
            if has_more
            else "false"
        ),
    }
```


---

## `app/utils/response.py`

```python
def response(
    message: str,
    data=None
):

    return {

        "status": "success",

        "message": message,

        "data": data

    }
```


---

## `app/utils/validators.py`

```python

```


---

## `docker-compose.yml`

```yaml
services:

  api:
    build: .

    # user: "${UID}:${GID}"

    container_name: fastapi-api

    security_opt:
      - seccomp:unconfined

    ports:
      - "8000:8000"

    volumes:
      - .:/app

    env_file:
      - .env

    depends_on:
      - postgres

  postgres:
    image: postgres:16

    container_name: fastapi-postgres

    restart: always

    environment:
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: 123456
      POSTGRES_DB: fastapi_db

    ports:
      - "5433:5432"

    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```


---

## `docs/diary/2026-07-28-current-progress.md`

```markdown
<h1 align="center">
📅 Development Log #01
</h1>

<p align="center">
Current Project Progress
</p>

---

# 📖 Overview

This document records the current development milestone of the project.

Although the project has already reached a functional state before this document was created, this log serves as the starting point for documenting future development, technical decisions, and learning progress.

---

# 🚀 Current Progress

Implemented modules:

- User CRUD
- JWT Authentication
- Password Hashing (BCrypt)
- OAuth2 Password Flow
- Protected APIs
- Post CRUD
- User ↔ Post Relationship
- Search API (`ILIKE`)
- Docker Development Environment
- Standardized API Response

---

# 🏗 Current Architecture

```
Client

   │

FastAPI Router

   │

CRUD Layer

   │

SQLAlchemy ORM

   │

PostgreSQL
```

Current project structure:

```
app/

├── routers/
├── models.py
├── schemas.py
├── crud.py
├── database.py
├── core/
└── utils/
```

---

# 📚 Concepts Practiced

Backend

- APIRouter
- Dependency Injection
- Response Model
- Request Validation

Authentication

- JWT
- OAuth2 Password Flow
- Password Hashing

Database

- SQLAlchemy ORM
- Relationship
- Foreign Key
- Joined Loading
- Ordering
- Pagination Preparation
- Text Search using `ILIKE`

Development

- Docker
- Docker Compose
- Linux CLI
- Git

---

# 💡 Technical Decisions

Current design principles:

- Router handles HTTP requests and responses.
- CRUD layer is responsible for database operations.
- JWT stores the user's email in the `sub` claim.
- Passwords are stored as BCrypt hashes.
- API responses are standardized using `APIResponse`.
- SQLAlchemy relationships are loaded using `joinedload()` when necessary.
- Search functionality is implemented using PostgreSQL `ILIKE` for case-insensitive matching.

---

# 📈 Current Completion Status

| Module | Status |
|---------|:------:|
| User CRUD | ✅ |
| Authentication | ✅ |
| Authorization | ✅ |
| Post CRUD | ✅ |
| Search | ✅ |
| Pagination | ✅ |
| Docker | ✅ |
| Response Wrapper | ✅ |
| Alembic | ⏳ |
| Unit Testing | ⏳ |
| Logging | ⏳ |

---

# 🔍 Code Highlights

Current implementation includes:

- `crud.py` centralizes database operations.
- `routers/` separates API endpoints by feature.
- `schemas.py` manages request and response validation.
- `models.py` defines ORM entities and relationships.
- `core/security.py` handles authentication and password hashing.
- Search is implemented using SQLAlchemy `ilike()` with PostgreSQL.

---

# 🎯 Next Learning Goal

The next topic focuses on building more flexible database queries using SQLAlchemy logical operators.

Planned topics:

- `and_()`
- `or_()`
- Multiple conditions
- Dynamic filtering
- Combining search with filters

Example goals:

```

GET /posts?search=docker

GET /posts?role=admin

GET /posts?search=docker&role=admin

```

These concepts will be applied to create more realistic filtering APIs similar to production backend systems.

---

# 🗄 SQL Queries Practiced

Current SQL concepts translated into SQLAlchemy:

- SELECT
- INSERT
- UPDATE
- DELETE
- WHERE
- ORDER BY
- LIMIT
- OFFSET
- ILIKE
- JOIN (through relationship)
- Joined Loading

Next:

- AND
- OR
- IN
- NOT
- Aggregate Functions

---

# 📝 Notes

This document marks the first official development log for the project.

Future logs will focus on incremental improvements instead of rewriting existing features, allowing the repository to better reflect the actual learning journey and project evolution.
```


---

## `docs/diary/2026-07-29-current-progress.md`

```markdown
# 📅 Development Log #02

**Date:** 2026-07-29

---

# 📖 Overview

Today's learning focused on writing more expressive SQL queries with SQLAlchemy ORM.

Instead of simple CRUD operations, the project now moves toward production-style database querying, allowing flexible filtering and more realistic API behavior.

This stage marks the transition from basic API development to practical backend query design.

---

# 🚀 New Progress

New concepts studied today:

* Logical Operators (`AND`, `OR`)
* Search with PostgreSQL `ILIKE`
* Multi-condition Filtering
* `IN` Queries
* `BETWEEN` Queries
* `COUNT()` Aggregation

These topics build the foundation for more advanced SQL features such as `GROUP BY`, aggregate functions, and joins.

---

# 🏗 Query Flow

Current query flow:

```text
HTTP Request

        │

FastAPI Router

        │

CRUD Layer

        │

SQLAlchemy Query Builder

        │

PostgreSQL
```

Example:

```text
GET /posts?search=sql

↓

Post.title.ilike("%sql%")

↓

SELECT *
FROM posts
WHERE title ILIKE '%sql%'
```

---

# 📚 SQLAlchemy Concepts Practiced

### Text Search

* `LIKE`
* `ILIKE`

Example:

```sql
WHERE title ILIKE '%docker%'
```

---

### Logical Operators

Studied:

* `and_()`
* `or_()`

Example:

```sql
WHERE title ILIKE '%SQL%'
AND user_id = 2
```

Example:

```sql
WHERE title ILIKE '%SQL%'
OR user_id = 2
```

---

### Membership Query

Studied:

```python
Post.id.in_([1,3,5])
```

Equivalent SQL:

```sql
WHERE id IN (1,3,5)
```

---

### Range Query

Studied:

```python
Post.id.between(1,5)
```

Equivalent SQL:

```sql
WHERE id BETWEEN 1 AND 5
```

---

### Counting Records

Studied:

```python
db.query(Post).count()
```

Equivalent SQL:

```sql
SELECT COUNT(*)
FROM posts;
```

---

# 💡 Technical Understanding

Today's learning emphasized that SQLAlchemy is not a replacement for SQL.

Instead:

```
Python

↓

SQLAlchemy ORM

↓

Generated SQL

↓

PostgreSQL
```

Understanding the SQL generated by SQLAlchemy makes debugging and optimization significantly easier.

---

# 🧪 Practice Completed

Successfully practiced:

* Searching posts using `ILIKE`
* Filtering with multiple conditions
* Using `AND`
* Using `OR`
* Filtering records with `IN`
* Selecting ranges with `BETWEEN`
* Counting database records

Swagger API was used to validate each query against PostgreSQL.

---

# 📈 Updated Progress

| Feature             | Status |
| ------------------- | :----: |
| User CRUD           |    ✅   |
| Authentication      |    ✅   |
| Authorization       |    ✅   |
| Post CRUD           |    ✅   |
| Search (`ILIKE`)    |    ✅   |
| AND / OR Filtering  |    ✅   |
| IN Query            |    ✅   |
| BETWEEN Query       |    ✅   |
| COUNT               |    ✅   |
| Pagination          |    ✅   |
| Docker              |    ✅   |
| Response Wrapper    |    ✅   |
| Alembic             |    ⏳   |
| GROUP BY            |    ⏳   |
| Aggregate Functions |    ⏳   |
| Raw SQL             |    ⏳   |
| Unit Testing        |    ⏳   |

---

# 🎯 Next Learning Goals

Planned topics:

* GROUP BY
* Aggregate Functions (`AVG`, `MAX`, `MIN`, `SUM`)
* SQL JOIN
* Raw SQL with SQLAlchemy
* Alembic Migration

These topics will move the project closer to production-level backend development.

---

# 🗄 SQL Concepts Covered

Current SQL topics:

* SELECT
* INSERT
* UPDATE
* DELETE
* WHERE
* ORDER BY
* LIMIT
* OFFSET
* LIKE
* ILIKE
* AND
* OR
* IN
* BETWEEN
* COUNT
* JOIN (Relationship)
* Joined Loading

Upcoming topics:

* GROUP BY
* HAVING
* AVG
* MAX
* MIN
* SUM
* Raw SQL
* Database Migration (Alembic)

---

# 📝 Learning Notes (Vietnamese)

Hôm nay đánh dấu bước chuyển từ việc xây dựng các API CRUD cơ bản sang học cách viết truy vấn SQL thực tế bằng SQLAlchemy ORM.

Điểm quan trọng nhất không phải là ghi nhớ cú pháp, mà là hiểu được mỗi câu lệnh SQLAlchemy sẽ sinh ra câu SQL tương ứng trong PostgreSQL.

Qua quá trình thực hành, mình đã hiểu rõ hơn về:

* Cách tìm kiếm dữ liệu bằng `ILIKE`.
* Khác biệt giữa `AND` và `OR`.
* Khi nào nên sử dụng `IN`.
* Cách lọc dữ liệu theo khoảng bằng `BETWEEN`.
* Cách đếm số lượng bản ghi bằng `COUNT()`.

Những kiến thức này sẽ là nền tảng cho các chủ đề khó hơn như `GROUP BY`, các hàm tổng hợp (`AVG`, `MAX`, `MIN`, `SUM`), `JOIN`, Raw SQL và Alembic Migration.

Mục tiêu tiếp theo là hiểu được cách SQLAlchemy ánh xạ từng truy vấn Python sang câu SQL thực tế và dần xây dựng tư duy thiết kế truy vấn giống như trong các dự án backend sử dụng PostgreSQL ở môi trường production.
```


---

## `docs/diary/2026-07-30-current-progress.md`

```markdown
# 📅 2026-07-30 Current Progress

---

# 🇻🇳 Tiếng Việt

## Mục tiêu hôm nay

Tiếp tục hoàn thiện project FastAPI theo hướng production-ready thay vì chỉ chạy được chức năng.

---

# 1. Docker

## Đã sửa lỗi BuildKit

Trong quá trình build image gặp lỗi:

```
failed to prepare extraction snapshot
parent snapshot ... does not exist
```

Đây không phải lỗi source code.

Nguyên nhân đến từ Docker BuildKit / overlayfs snapshot bị hỏng.

Đã xử lý bằng cách:

- restart docker daemon
- prune build cache
- build lại image

Sau khi xử lý:

```
docker compose up --build
```

đã build thành công.

---

## Đã hiểu Healthcheck

Đã thêm

```dockerfile
HEALTHCHECK
```

để Docker kiểm tra application còn sống hay không.

Healthcheck sẽ gọi

```
GET /health
```

định kỳ.

Log xuất hiện liên tục:

```
GET /health 200 OK
```

không phải bug.

Đó là Docker tự kiểm tra container.

---

## Đã tạo .dockerignore

Giảm build context.

Không copy các file không cần thiết vào image.

Ví dụ:

- __pycache__
- .git
- .venv
- .pytest_cache
- docs
- logs

Hiểu được vì sao build nhanh hơn.

---

## Đã tạo requirements-dev.txt

Tách dependency:

requirements.txt

→ Production

requirements-dev.txt

→ Development

Ví dụ:

- pytest
- black
- isort
- flake8
- mypy

---

# 2. Dockerfile

Đã hiểu:

```
FROM
WORKDIR
COPY
RUN
CMD
HEALTHCHECK
```

Hiểu được:

Dockerfile là quá trình build image.

CMD là process chính.

HEALTHCHECK là process kiểm tra container.

---

# 3. Docker Compose

Đã sử dụng thành thạo:

```
docker compose up

docker compose up --build

docker compose down

docker compose ps
```

Đã phân biệt được:

Image

Container

Network

Volume

Build Cache

---

# 4. Alembic

Đã tích hợp Alembic vào project.

Đã tạo:

```
alembic/
```

bao gồm:

```
env.py

script.py.mako

README

versions/
```

---

## Đã chỉnh sửa env.py

Đã kết nối Alembic với:

```
settings.DATABASE_URL
```

và

```
Base.metadata
```

để Alembic tự phát hiện model.

---

## Database

Đã hiểu:

Không nên sử dụng

```
Base.metadata.create_all()
```

cho production.

Thay vào đó:

Alembic quản lý toàn bộ schema.

---

## Migration

Đã tạo migration đầu tiên.

Đã hiểu:

```
revision

upgrade()

downgrade()
```

Hiểu ý nghĩa của migration history.

---

# 5. Docker + Alembic

Đã hiểu:

Khi chạy Docker,

Database không còn được tạo bằng:

```
create_all()
```

mà sẽ dùng:

```
alembic upgrade head
```

để đồng bộ schema.

---

# 6. Kiến thức mới

Hôm nay học được:

- Docker BuildKit snapshot
- overlayfs
- build cache
- docker healthcheck
- dockerignore
- dependency production/dev
- Alembic architecture
- migration history
- schema versioning

---

# 7. Những lỗi đã xử lý

✅ Docker BuildKit snapshot error

✅ Dockerfile parse error

✅ Sai cú pháp CMD

✅ HEALTHCHECK syntax

✅ Docker image rebuild

✅ Alembic configuration

✅ Metadata import

---

# 8. Trạng thái project

Đến cuối ngày:

✅ Docker hoạt động ổn định

✅ PostgreSQL hoạt động

✅ FastAPI hoạt động

✅ Healthcheck hoạt động

✅ Docker Compose hoạt động

✅ Alembic hoạt động

✅ Migration đầu tiên đã tạo

Project đã chuyển sang cách quản lý database chuẩn bằng Alembic thay cho create_all().

---

# 🇬🇧 English

## Today's Goal

Continue improving the FastAPI project toward a production-ready architecture instead of simply making it run.

---

# 1. Docker

## Fixed BuildKit issue

Encountered:

```
failed to prepare extraction snapshot
```

The problem was related to Docker BuildKit / overlayfs rather than the application source code.

Resolved by:

- restarting Docker
- cleaning BuildKit cache
- rebuilding the image

The project now builds successfully.

---

## Learned Docker HEALTHCHECK

Added

```
HEALTHCHECK
```

to periodically verify the application status.

Docker now sends

```
GET /health
```

requests automatically.

Repeated health requests inside the logs are expected behavior.

---

## Added .dockerignore

Reduced Docker build context by excluding unnecessary files such as:

- __pycache__
- .git
- virtual environments
- documentation
- logs

This improves build speed and keeps images smaller.

---

## Added requirements-dev.txt

Separated dependencies into:

Production:

```
requirements.txt
```

Development:

```
requirements-dev.txt
```

including tools like:

- pytest
- black
- isort
- flake8
- mypy

---

# 2. Dockerfile

Understood the purpose of:

- FROM
- WORKDIR
- COPY
- RUN
- CMD
- HEALTHCHECK

Also learned the distinction between the container's main process and health monitoring.

---

# 3. Docker Compose

Practiced:

```
docker compose up

docker compose up --build

docker compose down

docker compose ps
```

Also gained a better understanding of:

- Images
- Containers
- Networks
- Volumes
- Build Cache

---

# 4. Alembic

Integrated Alembic into the project.

Generated:

```
alembic/
```

including:

- env.py
- script.py.mako
- README
- versions/

---

## Updated env.py

Configured Alembic to use:

```
settings.DATABASE_URL
```

and

```
Base.metadata
```

so migrations are generated automatically from SQLAlchemy models.

---

## Database Management

Learned that

```
Base.metadata.create_all()
```

is not appropriate for production.

Database schema should instead be managed entirely through Alembic migrations.

---

## Migration

Created the initial migration.

Understood:

- revision
- upgrade()
- downgrade()

and how Alembic tracks schema history.

---

# 5. Docker + Alembic

Understood that containers should initialize the database using:

```
alembic upgrade head
```

instead of relying on create_all().

---

# 6. New Knowledge

Today's learning included:

- Docker BuildKit
- overlayfs snapshots
- build cache
- Docker health checks
- dockerignore
- dependency separation
- Alembic architecture
- migration history
- schema versioning

---

# 7. Issues Resolved

✔ BuildKit snapshot issue

✔ Dockerfile syntax error

✔ Incorrect CMD format

✔ HEALTHCHECK syntax

✔ Docker rebuild

✔ Alembic configuration

✔ SQLAlchemy metadata configuration

---

# 8. Current Status

Current project status:

- Docker is working correctly.
- PostgreSQL is running successfully.
- FastAPI starts normally.
- Health checks are operational.
- Docker Compose works correctly.
- Alembic is integrated.
- Initial migration has been created.

The project now manages database schema using Alembic instead of create_all(), making it closer to a production-ready architecture.
```


---

## `docs/diary/2026-07-31-current-progress.md`

```markdown
# 📘 Current Progress
# Ngày / Date: 2026-07-31

---

# 🇻🇳 Tiếng Việt

## Chủ đề học

Repository Pattern trong FastAPI.

Đây là ngày đầu tiên bắt đầu tách tầng truy cập dữ liệu (Data Access Layer) ra khỏi Router để chuẩn bị cho kiến trúc nhiều tầng của dự án.

---

# Những gì đã học

## 1. Hiểu vấn đề của CRUD truyền thống

Trước đây Router gọi trực tiếp:

```
Router
    ↓
CRUD
    ↓
Database
```

Ví dụ

```python
user = user_crud.get_user(db, user_id)
```

Router biết toàn bộ cách CRUD làm việc.

Điều này dẫn đến:

- Router phụ thuộc trực tiếp vào CRUD
- Khó thay đổi tầng truy cập dữ liệu
- Khó mở rộng project
- Khó test độc lập

---

## 2. Repository Pattern là gì

Repository là lớp chuyên giao tiếp với Database.

Router sẽ không còn thao tác trực tiếp với SQLAlchemy nữa.

Kiến trúc chuyển thành

```
Router
    ↓
Repository
    ↓
SQLAlchemy
    ↓
Database
```

Repository chịu trách nhiệm:

- Query
- Insert
- Update
- Delete

Router chỉ quan tâm tới business flow.

---

## 3. Tạo thư mục repositories

Đã tạo

```
app/
    repositories/
        __init__.py
        user_repository.py
```

---

## 4. Xây dựng UserRepository

Đã tạo class

```python
class UserRepository:
```

Repository nhận Session thông qua constructor

```python
def __init__(self, db: Session):
    self.db = db
```

Đây là Dependency Injection đơn giản.

---

## 5. Các hàm Repository đã xây dựng

### get_all()

Lấy toàn bộ User

---

### get_by_id()

Lấy User theo ID

---

### create()

Thêm User mới

---

### update()

Commit thay đổi

---

### delete()

Xóa User

---

## 6. Vì sao update() không nhận UserUpdate

Đã hiểu Repository chỉ làm việc với Model SQLAlchemy.

Repository không biết:

- UserCreate
- UserUpdate
- UserPatch

Đó là nhiệm vụ của tầng cao hơn.

---

## 7. Router bắt đầu chuyển sang Repository

Đã xác định các endpoint có thể chuyển ngay

- GET ALL
- GET BY ID
- DELETE

Các endpoint

- POST
- PUT
- PATCH

chưa chuyển được hoàn toàn vì vẫn đang nhận Pydantic Schema.

---

## 8. Hiểu giới hạn của Repository

Repository không nên chứa:

- Validation
- HTTPException
- Response
- Business Logic

Repository chỉ làm Database Access.

---

## 9. Chuẩn bị cho Service Layer

Đã hiểu lý do cần Service.

Sau này kiến trúc sẽ trở thành

```
Router
    ↓
Service
    ↓
Repository
    ↓
Database
```

Service sẽ:

- Validate dữ liệu
- Chuyển Schema thành SQLAlchemy Model
- Gọi Repository
- Thực hiện Business Logic

Repository chỉ còn tập trung vào Database.

---

# Những lỗi đã phát hiện

## Lỗi 1

Import

```python
from app.crud import user as user_crud
```

nhưng bên dưới lại gọi

```python
crud.get_user(...)
```

Sai.

Phải dùng

```python
user_crud.get_user(...)
```

---

## Lỗi 2

Repository hiện tại chưa thể thay thế toàn bộ CRUD.

Điều này hoàn toàn bình thường.

Không phải lỗi.

---

# Kiến thức rút ra

Repository không phải là CRUD mới.

Repository chỉ là lớp chịu trách nhiệm truy cập dữ liệu.

Repository không biết:

- HTTP
- FastAPI
- Response
- Business Logic

Repository chỉ biết Database.

---

# Tiến độ hiện tại

Đã hoàn thành

- Repository Pattern cơ bản
- UserRepository
- Dependency Injection cho Repository
- Chuyển một phần Router sang Repository
- Hiểu giới hạn của Repository
- Chuẩn bị cho Service Layer

---

# 🇺🇸 English

## Learning Topic

Repository Pattern in FastAPI.

Today focused on separating the data access layer from the Router to move toward a clean multi-layer architecture.

---

## What I Learned

### Understanding the problem with traditional CRUD

Previously

```
Router
    ↓
CRUD
    ↓
Database
```

Router depended directly on CRUD functions.

This creates tight coupling and makes future maintenance harder.

---

### Understanding Repository Pattern

Repository is responsible only for database access.

New architecture

```
Router
    ↓
Repository
    ↓
SQLAlchemy
    ↓
Database
```

Repository performs

- Query
- Insert
- Update
- Delete

without containing business logic.

---

### Repository Structure

Created

```
app/repositories/

    __init__.py

    user_repository.py
```

---

### UserRepository

Implemented

- get_all()
- get_by_id()
- create()
- update()
- delete()

Repository receives SQLAlchemy Session through constructor injection.

---

### Router Migration

Successfully identified endpoints that can already use Repository.

Completed:

- GET ALL
- GET BY ID
- DELETE

POST, PUT and PATCH still require CRUD because they receive Pydantic Schemas instead of SQLAlchemy Models.

---

### Repository Responsibilities

Repository should NOT contain

- HTTP Exceptions
- Validation
- Business Rules
- FastAPI Responses

Repository should ONLY communicate with the database.

---

### Preparing for Service Layer

Understood why Service Layer is needed.

Future architecture

```
Router
    ↓
Service
    ↓
Repository
    ↓
Database
```

Service will convert Pydantic Schemas into SQLAlchemy Models before calling Repository.

---

## Bugs Found

- Incorrect variable name (`crud` vs `user_crud`)
- Repository cannot fully replace CRUD yet because it currently accepts SQLAlchemy Models only.

---

## Current Progress

Completed

- Basic Repository Pattern
- UserRepository implementation
- Repository Dependency Injection
- Partial Router migration
- Understanding Repository responsibilities
- Preparing for Service Layer
```


---

## `docs/diary/2026-08-01-current-progress.md`

```markdown
# 📅 2026-08-01 Current Progress

---

# 🇻🇳 Tiếng Việt

## Chủ đề hôm nay

Thực hành **Repository Pattern** hoàn chỉnh trong dự án FastAPI.

Mục tiêu của buổi học không phải thêm tính năng mới mà là học cách tổ chức code theo chuẩn mà các dự án lớn sử dụng.

---

# 1. Hiểu vấn đề trước khi Refactor

Ban đầu Router gọi trực tiếp SQLAlchemy.

Ví dụ
```


---

## `docs/diary/2026-08-02-current-progress.md`

```markdown
# 📅 Development Diary — 2026-08-02

## Chủ đề
**Tiếp tục refactor kiến trúc và làm rõ trách nhiệm giữa các tầng.**

> Nhật ký giai đoạn 02/08–08/08 được tổng hợp lại từ trạng thái source code, migration, test và các vấn đề đã được trao đổi trong quá trình học. Mục tiêu là ghi lại hành trình học tập một cách trung thực, không biến project thành một “perfect project” giả định.

---

## Hôm nay tôi tập trung vào điều gì?

Sau khi thực hành Repository Pattern, tôi bắt đầu nhận ra rằng việc tách file/tách folder không tự động làm code tốt hơn. Điều quan trọng hơn là phải hiểu **mỗi tầng chịu trách nhiệm gì**.

Luồng kiến trúc tôi hướng tới:

```text
Router
  ↓
Service
  ↓
Repository / Data Access
  ↓
SQLAlchemy
  ↓
PostgreSQL
```

---

## Điều tôi học được

- Router nên tập trung vào HTTP request/response.
- Service phù hợp với business logic và orchestration.
- Repository phù hợp với database access.
- Schema dùng để validate dữ liệu vào/ra.
- Model đại diện cho database entity.

Điểm quan trọng nhất tôi nhận ra: **refactor architecture phải đi kèm kiểm tra import, dependency và flow thực tế**, nếu không rất dễ tạo ra code cũ và code mới cùng tồn tại.

---

## Bài học thực tế

Không nên chỉ nhìn cây thư mục rồi kết luận rằng architecture đã đúng. Cần kiểm tra cả đường đi của một request:

```text
HTTP request
→ Router
→ Service
→ Repository
→ Database
→ Model
→ Schema
→ HTTP response
```

Đây là cách tôi bắt đầu kiểm tra project có thực sự “đi đúng đường ray” hay chưa.

---

## Ghi chú

Tôi bắt đầu quan tâm nhiều hơn đến **tính nhất quán của toàn project** thay vì chỉ làm cho từng endpoint chạy được.
```


---

## `docs/diary/2026-08-03-current-progress.md`

```markdown
# 📅 Development Diary — 2026-08-03

## Chủ đề
**Service Layer và business logic.**

---

## Mục tiêu học tập

Tìm hiểu vì sao một project có Repository nhưng vẫn có thể cần Service Layer.

Repository không nên biết:

- FastAPI
- HTTPException
- HTTP status code
- API response
- Business rule

Service là nơi phù hợp hơn cho các quy tắc như:

- Chuẩn hóa email.
- Kiểm tra email đã tồn tại.
- Quyết định khi nào trả về lỗi business.
- Điều phối nhiều thao tác repository.

---

## Một flow tôi cần ghi nhớ

```text
UserCreate
   ↓
Router
   ↓
User Service
   ↓
Validate business rule
   ↓
Repository
   ↓
User Model
   ↓
PostgreSQL
```

---

## PUT và PATCH

Tôi tiếp tục củng cố sự khác nhau giữa:

### PUT
Thay thế resource theo schema đầy đủ.

### PATCH
Chỉ thay đổi những field được gửi lên.

Với PATCH, ý tưởng quan trọng là:

```python
model_dump(exclude_unset=True)
```

để tránh vô tình ghi đè những field người dùng không gửi.

---

## Bài học

Service Layer không phải là nơi “ném tất cả code vào cho dài project”.

Một tầng mới chỉ có giá trị khi nó giúp trách nhiệm rõ ràng hơn.
```


---

## `docs/diary/2026-08-04-current-progress.md`

```markdown
# 📅 Development Diary — 2026-08-04

## Chủ đề
**Models, Schemas và quan hệ User–Post.**

---

## Database Model

Project sử dụng hai entity chính:

```text
User 1 ───────── * Post
```

`Post.user_id` là foreign key trỏ tới `users.id`.

SQLAlchemy relationship được thiết lập hai chiều thông qua `back_populates`.

---

## Schema Layer

Tôi phân biệt rõ hơn ba loại schema cho User:

- `UserCreate`: dữ liệu tạo mới.
- `UserUpdate`: dữ liệu PUT.
- `UserPatch`: dữ liệu PATCH.
- `UserResponse`: dữ liệu trả về client.

Điều này giúp tránh việc dùng trực tiếp SQLAlchemy Model làm request/response model.

---

## Validation

Pydantic được dùng để kiểm tra:

- độ dài `name`
- định dạng email
- độ dài password
- role
- các field optional trong PATCH

`UserResponse` dùng:

```python
ConfigDict(from_attributes=True)
```

để có thể chuyển dữ liệu từ SQLAlchemy ORM object sang Pydantic response model.

---

## Bài học quan trọng

Model và Schema có liên quan nhưng không phải cùng một thứ:

```text
SQLAlchemy Model → Database representation
Pydantic Schema  → API contract / validation
```

Đây là một trong những điểm tôi muốn giải thích được với mentor thay vì chỉ biết viết code theo mẫu.
```


---

## `docs/diary/2026-08-05-current-progress.md`

```markdown
# 📅 Development Diary — 2026-08-05

## Chủ đề
**Testing và kiểm tra API theo hướng thực tế.**

---

## Vì sao cần test?

Sau khi refactor nhiều tầng, tôi nhận ra rằng code “nhìn có vẻ đúng” chưa đủ.

Một thay đổi ở:

- model
- schema
- repository
- service
- router
- database

đều có thể làm endpoint khác hỏng theo.

Vì vậy tôi bắt đầu coi test như một cách kiểm tra toàn bộ đường đi của request.

---

## Các loại test trong project

Project hiện có các nhóm:

```text
tests/
├── api/
├── swagger/
└── e2e/
```

Có test cho:

- health endpoint
- create user
- get users
- authentication
- posts
- Swagger-related checks
- end-to-end Swagger capture

---

## Cách kiểm tra

Một request test đi theo hướng:

```text
pytest
  ↓
HTTP request
  ↓
FastAPI
  ↓
Database
  ↓
HTTP response
  ↓
assert
```

Điều này giúp tôi hiểu rằng test API không chỉ kiểm tra một function Python đơn lẻ mà có thể kiểm tra cả integration giữa nhiều thành phần.

---

## Bài học

Khi test fail, không nên lập tức sửa assertion.

Cần xem:

1. request thực sự gửi gì?
2. endpoint nào được gọi?
3. status code là gì?
4. response body là gì?
5. log server nói gì?
6. database schema có khớp model không?

Đây trở thành một thói quen debugging quan trọng.
```


---

## `docs/diary/2026-08-06-current-progress.md`

```markdown
# 📅 Development Diary — 2026-08-06

## Chủ đề
**Docker, PostgreSQL và môi trường phát triển.**

---

## Docker Compose

Project chạy hai service chính:

```text
fastapi-api
fastapi-postgres
```

API expose port `8000`.

PostgreSQL container expose port `5433` ở host và `5432` bên trong container.

---

## Những thứ tôi đã hiểu rõ hơn

### Image
Template để tạo container.

### Container
Instance đang chạy của image.

### Network
Cho phép API container giao tiếp với PostgreSQL container.

### Volume
Giữ dữ liệu PostgreSQL không biến mất khi container bị remove.

---

## Healthcheck

API có endpoint:

```text
GET /health
```

Docker sử dụng healthcheck để kiểm tra application còn hoạt động.

Các dòng:

```text
GET /health 200 OK
```

trong log không phải lỗi; đó là dấu hiệu healthcheck đang chạy.

---

## Alembic

Tôi tiếp tục phân biệt:

```text
SQLAlchemy Model
       ↓
Alembic Migration
       ↓
PostgreSQL Schema
```

Model thay đổi không có nghĩa database tự động thay đổi theo.

Migration phải phản ánh thay đổi schema.

---

## Bài học

Docker giúp môi trường nhất quán hơn, nhưng Docker không tự sửa lỗi application.

Nếu database schema sai hoặc migration sai, container vẫn có thể “Up” và healthcheck vẫn có thể trả `200` trong khi một API business vẫn trả `500`.
```


---

## `docs/diary/2026-08-07-current-progress.md`

```markdown
# 📅 Development Diary — 2026-08-07

## Chủ đề
**Alembic migration và thay đổi schema `full_name`.**

---

## Thay đổi model

User model được bổ sung field:

```text
full_name
```

Schema cũng được bổ sung để API có thể nhận/đại diện field này.

---

## Migration được tạo

Project có migration:

```text
5614567ad165_add_full_name.py
```

Migration này kế thừa:

```text
e122a64acbc0
```

và revision chain trở thành:

```text
e122a64acbc0
        ↓
5614567ad165
```

---

## Điều tôi học được

Một migration file tồn tại chưa có nghĩa migration đã thay đổi database.

Cần phân biệt:

```text
Model changed
      ≠
Migration file exists
      ≠
Database schema changed
```

Phải kiểm tra migration `upgrade()` thực sự có operation tương ứng và kiểm tra schema PostgreSQL sau khi upgrade.

---

## Bài học debugging

Đây là một điểm rất quan trọng trong quá trình học của tôi: **Alembic phải được kiểm tra cả lịch sử migration lẫn trạng thái schema thực tế.**

Không nên chỉ nhìn:

```text
alembic current
```

rồi kết luận database đã đúng.
```


---

## `docs/diary/2026-08-08-current-progress.md`

```markdown
# 📅 Development Diary — 2026-08-08

## Chủ đề
**Debugging sau refactor: tìm lỗi nằm ở đâu thay vì sửa ngẫu nhiên.**

---

## Vấn đề nổi bật

Khi gọi:

```text
GET /users
```

API trả:

```text
500 Internal Server Error
```

Log PostgreSQL/SQLAlchemy chỉ ra lỗi:

```text
column users.full_name does not exist
```

Trong khi SQLAlchemy Model đã có `full_name`.

---

## Điều này cho thấy

Application code và database schema đang **không đồng bộ**.

SQLAlchemy sinh query có:

```sql
users.full_name
```

nhưng PostgreSQL table `users` thực tế chưa có column đó.

---

## Một bài học rất lớn

Container có thể:

```text
Up
Healthy
```

nhưng endpoint business vẫn có thể:

```text
500
```

Vì vậy:

```text
Docker health
≠
Application correctness
≠
Database correctness
```

---

## Cách debugging tôi học được

Không đoán.

Đi từ log:

```text
HTTP 500
 ↓
Traceback
 ↓
SQLAlchemy exception
 ↓
PostgreSQL exception
 ↓
UndefinedColumn
 ↓
users.full_name
```

Sau đó kiểm tra database schema thật bằng PostgreSQL.

---

## Kết luận của ngày hôm nay

Refactor kiến trúc giúp code dễ tổ chức hơn, nhưng cũng làm tôi nhận ra một điều quan trọng:

> **Tách code chỉ là bước đầu. Điều khó hơn là giữ toàn bộ hệ thống đồng bộ.**

Đây là lý do project cần migration, test, logging và quy trình kiểm tra rõ ràng.
```


---

## `docs/diary/2026-08-09-project-summary.md`

```markdown
# 🚀 FastAPI User Management — Learning Journey

> **Một tài liệu duy nhất dành cho mentor:** nếu chị chỉ muốn xem nhanh quá trình học, kiến trúc, những gì đã làm, những lỗi đã gặp và những gì tôi đang học tiếp, chỉ cần mở file này.
>
> **Khoảng thời gian:** 28/07/2026 → 09/08/2026
>
> Nhật ký 02/08–08/08 được tổng hợp lại từ source code, migration, test và trạng thái project trong archive. Đây là **learning summary**, không phải commit history theo giờ. Những điểm chưa hoàn thiện cũng được giữ lại để mentor có thể nhìn thấy quá trình học và debugging thực tế.

---

## 🧭 1. Tôi bắt đầu project này để làm gì?

Đây là một backend learning project dùng **FastAPI** để học cách xây dựng một REST API thực tế thay vì chỉ viết các endpoint đơn lẻ.

Mục tiêu học tập gồm:

- FastAPI routing
- Pydantic validation
- SQLAlchemy ORM
- PostgreSQL
- Authentication / JWT
- Docker / Docker Compose
- Alembic migration
- Repository Pattern
- Service Layer
- Testing với pytest
- Linux / Bash
- Debugging theo log và database state
- Hiểu request flow từ HTTP đến PostgreSQL

Điểm quan trọng nhất không phải là “code càng nhiều càng tốt”, mà là hiểu **một request đi qua hệ thống như thế nào** và có thể tìm nguyên nhân khi các tầng không còn đồng bộ.

---

# 🗺 2. Hành trình học tập

## 28/07 — Nền tảng project

Project có các chức năng backend chính:

- User CRUD
- JWT authentication
- OAuth2 Password Flow
- Password hashing
- Protected API
- Post CRUD
- User–Post relationship
- Search bằng PostgreSQL `ILIKE`
- Docker development environment
- Standardized API response

Đây là điểm xuất phát để chuyển từ “API chạy được” sang “API có architecture rõ hơn”.

📓 [Development Log — 28/07](./2026-07-28-current-progress.md)

---

## 29/07 — SQL và SQLAlchemy Query

Tập trung vào query thực tế:

- `LIKE` / `ILIKE`
- `AND`
- `OR`
- `IN`
- `BETWEEN`
- `COUNT()`
- filtering nhiều điều kiện

Một nhận thức quan trọng: SQLAlchemy không thay thế SQL. Nó cung cấp cách xây dựng query bằng Python, còn PostgreSQL vẫn là database thực thi truy vấn.

📓 [Development Log — 29/07](./2026-07-29-current-progress.md)

---

## 30/07 — Docker và Alembic

Tôi học sâu hơn về:

- Docker image / container / network / volume
- Docker BuildKit
- `.dockerignore`
- `requirements-dev.txt`
- healthcheck
- Alembic
- migration history
- `upgrade()` / `downgrade()`

Một bài học quan trọng là **`Base.metadata.create_all()` và Alembic có vai trò khác nhau**. Với project dùng migration, schema cần được quản lý bằng migration có version rõ ràng thay vì phụ thuộc vào việc application tự tạo bảng.

📓 [Development Log — 30/07](./2026-07-30-current-progress.md)

---

## 31/07 — Repository Pattern

Tôi bắt đầu tách database access khỏi Router.

Từ:

```text
Router
  ↓
SQLAlchemy query
```

sang tư duy:

```text
Router
  ↓
Repository
  ↓
Database
```

Tôi học được Repository nên tập trung vào data access, không nên biết HTTP status code, response hay business rule.

📓 [Development Log — 31/07](./2026-07-31-current-progress.md)

---

## 01/08 — Repository thực hành sâu hơn

Tiếp tục với:

- GET all
- GET by ID
- CREATE
- UPDATE
- PATCH
- DELETE
- `exclude_unset=True`
- phân biệt PUT / PATCH
- HTTPException nằm ở tầng HTTP thay vì Repository

Tôi bắt đầu nhận ra rằng refactor architecture không chỉ là “tách file”. Import, dependency và request flow cũng phải được kiểm tra lại.

📓 [Development Log — 01/08](./2026-08-01-current-progress.md)

---

## 02/08 → 04/08 — Architecture, Service, Model và Schema

Tôi củng cố tư duy kiến trúc nhiều tầng:

```text
Router
   ↓
Service
   ↓
Repository / Data Access
   ↓
SQLAlchemy
   ↓
PostgreSQL
```

Đồng thời học rõ hơn sự khác nhau giữa:

- SQLAlchemy Model
- Pydantic Schema
- `UserCreate`
- `UserUpdate`
- `UserPatch`
- `UserResponse`

và quan hệ:

```text
User 1 ───── * Post
```

📓 [Diary — 02/08](./2026-08-02-current-progress.md)  
📓 [Diary — 03/08](./2026-08-03-current-progress.md)  
📓 [Diary — 04/08](./2026-08-04-current-progress.md)

---

## 05/08 — Testing

Tôi bắt đầu sử dụng pytest như một phần của workflow thay vì chỉ mở Swagger và thử bằng tay.

Project hiện có các nhóm:

```text
tests/api/
tests/swagger/
tests/e2e/
```

Tôi học cách đọc:

```text
request
→ status code
→ response body
→ server log
→ traceback
→ database state
```

📓 [Diary — 05/08](./2026-08-05-current-progress.md)

---

## 06/08 — Docker + Database + Migration

Tiếp tục kiểm tra môi trường Docker và database.

Một nhận thức quan trọng:

```text
Container healthy
        ≠
API hoàn toàn đúng
        ≠
Database schema hoàn toàn đúng
```

Healthcheck chỉ chứng minh phần health endpoint đang hoạt động; nó không chứng minh mọi business endpoint đều đúng.

📓 [Diary — 06/08](./2026-08-06-current-progress.md)

---

## 07/08 — `full_name` và Alembic

User model/schema được bổ sung `full_name`.

Migration chain trong source:

```text
e122a64acbc0
        ↓
5614567ad165
```

Nhưng khi review source, migration:

```text
alembic/versions/5614567ad165_add_full_name.py
```

hiện có:

```python
def upgrade() -> None:
    pass

def downgrade() -> None:
    pass
```

Điều này có nghĩa migration file **chưa thực sự thêm column `full_name` vào PostgreSQL**.

Đây là một phát hiện quan trọng của quá trình review chứ không phải điều tôi muốn che đi.

📓 [Diary — 07/08](./2026-08-07-current-progress.md)

---

## 08/08 — Debugging database mismatch

Khi gọi:

```text
GET /users/
```

API trả:

```text
500 Internal Server Error
```

Root cause trong log:

```text
psycopg2.errors.UndefinedColumn:
column users.full_name does not exist
```

Trong khi SQLAlchemy query lại có:

```sql
users.full_name
```

Và User model đã có field `full_name`.

Điều này cho thấy:

```text
Application Model
       ↓
       ✕
PostgreSQL Schema
```

đang không đồng bộ.

Tôi học được cách debug từ:

```text
HTTP 500
 ↓
Traceback
 ↓
SQLAlchemy
 ↓
psycopg2
 ↓
PostgreSQL
 ↓
UndefinedColumn
 ↓
users.full_name
```

📓 [Diary — 08/08](./2026-08-08-current-progress.md)

---

# 📸 3. Evidence — API testing screenshots

Phần này được thêm để mentor có thể nhìn thấy **bằng chứng trực quan** của quá trình test API thay vì chỉ đọc mô tả.

README của project hiện tham chiếu các screenshot tại:

```text
tests/screenshots/
```

Các evidence được ghi nhận trong README:

### 🔐 Authentication

![Authentication — Swagger login](../../tests/screenshots/Authentication/Authentication%20Post%20Auth%20Login.png)

[🔎 Mở ảnh Authentication](../../tests/screenshots/Authentication/Authentication%20Post%20Auth%20Login.png)

### 👤 Users

![Users — GET users](../../tests/screenshots/User/Test%20Get%20User.png)

[🔎 Mở ảnh Users](../../tests/screenshots/User/Test%20Get%20User.png)

### 📝 Posts

![Posts — GET posts](../../tests/screenshots/Post/Get%20Posts.png)

[🔎 Mở ảnh Posts](../../tests/screenshots/Post/Get%20Posts.png)

> **Lưu ý về archive hiện tại:** trong `fastapi-user-management.zip` được cung cấp cho lần review này, thư mục `tests/screenshots/` và các file ảnh binary không xuất hiện, mặc dù README có tham chiếu đến chúng. Vì vậy tôi giữ **đúng các đường dẫn evidence mà README đã khai báo** nhưng không tự tạo hoặc bịa thêm tên ảnh. Nếu các ảnh đang có trong working copy thực tế của project, các link trên sẽ hiển thị bình thường khi file summary này nằm tại `docs/diary/`.

---

# 🏗 4. Kiến trúc project hiện tại

Source hiện có các khu vực chính:

```text
app/
├── core/
├── crud/
├── models/
├── repositories/
├── routers/
├── schemas/
├── services/
└── utils/

alembic/
tests/
scripts/
Dockerfile
docker-compose.yml
```

### Vai trò dự kiến

| Layer | Vai trò |
|---|---|
| `routers/` | HTTP endpoints, request/response |
| `schemas/` | Pydantic validation và API contract |
| `models/` | SQLAlchemy ORM models |
| `services/` | Business logic / orchestration |
| `repositories/` | Data access |
| `crud/` | Các database operation còn tồn tại trong source |
| `core/` | Configuration, security, exceptions, logging |
| `utils/` | Helper, pagination, response, validation |
| `alembic/` | Database migration history |
| `tests/` | API, Swagger và E2E tests |

### ⚠️ Một điểm cần tiếp tục refactor

Source hiện **đồng thời có `crud/` và `repositories/`**.

Đây là điểm tôi không muốn giả định rằng đã “clean” chỉ vì folder đã được tách. Cần quyết định rõ data-access architecture cuối cùng để tránh duplicate responsibility.

---

# 🔄 5. Request flow mà tôi đang học

Mục tiêu kiến trúc:

```text
HTTP Request
      ↓
Router
      ↓
Schema validation
      ↓
Service
      ↓
Repository
      ↓
SQLAlchemy ORM
      ↓
PostgreSQL
      ↓
Repository result
      ↓
Service
      ↓
Response Schema
      ↓
HTTP Response
```

Điều quan trọng tôi học được là **folder structure chỉ là hình thức**. Muốn biết architecture có thực sự đúng hay không phải theo dõi request flow thật.

---

# 👤 6. User và Post

Quan hệ chính:

```text
User 1 ───────── * Post
```

`posts.user_id` tham chiếu tới `users.id`.

SQLAlchemy relationship sử dụng:

```text
User.posts
Post.owner
```

với `back_populates`.

---

# 🧩 7. Models và Schemas

## SQLAlchemy Model

Model đại diện cho database entity.

Ví dụ User có các field:

```text
id
name
email
role
password
full_name
```

## Pydantic Schema

Schema đại diện cho API contract.

Các schema User hiện có:

```text
UserCreate
UserUpdate
UserPatch
UserResponse
```

Tôi học được rằng:

```text
SQLAlchemy Model
      ≠
Pydantic Schema
```

Model phục vụ ORM/database; Schema phục vụ validation và API input/output.

---

# 🔐 8. Authentication

Project thực hành:

- JWT
- OAuth2 Password Flow
- password hashing
- login
- protected endpoints
- current user

Đây là phần giúp tôi hiểu thêm rằng authentication không chỉ là tạo một endpoint `/login`, mà còn liên quan đến:

```text
credentials
 ↓
password verification
 ↓
token
 ↓
dependency
 ↓
current user
 ↓
protected endpoint
```

---

# 🐳 9. Docker workflow

Project có hai service chính:

```text
fastapi-api
      │
      │ Docker network
      ↓
fastapi-postgres
```

Các lệnh đã thực hành:

```bash
docker compose up
docker compose up --build
docker compose down
docker compose ps
docker compose logs api
docker compose exec api ...
```

Một bài học quan trọng:

```text
Container Up
    ↓
Container Healthy
```

không đồng nghĩa:

```text
Business API Correct
```

---

# 🗄 10. Database và Alembic

Database sử dụng PostgreSQL 16.

Migration chain hiện có:

```text
e122a64acbc0
        ↓
5614567ad165
```

Tuy nhiên source review cho thấy migration `5614567ad165_add_full_name.py` hiện chưa có operation để thêm column.

Vì vậy cần phân biệt:

```text
Model changed
      ≠
Migration file exists
      ≠
Migration actually changes DB
      ≠
Database schema is correct
```

Đây là một trong những bài học quan trọng nhất của project.

---

# 🧪 11. Testing

Project có:

```text
tests/
├── api/
├── swagger/
└── e2e/
```

Các nhóm test hiện có:

- health
- create user
- get users
- authentication
- posts
- Swagger checks
- E2E Swagger capture

Một test đã phát hiện lỗi thực tế:

```text
GET /users/
→ 500
```

thay vì:

```text
200
```

Sau đó traceback giúp xác định root cause:

```text
users.full_name does not exist
```

Đây là cách tôi bắt đầu sử dụng test như một **debugging tool**, không chỉ như một thủ tục “chạy test cho có”.

---

# 🧠 12. Những bài học lớn nhất

## 1. Clean architecture không phải là nhiều folder

Tách thành:

```text
routers/
services/
repositories/
crud/
```

chưa có nghĩa architecture sạch.

Các layer phải có responsibility rõ ràng và dependency phải nhất quán.

---

## 2. Model và database phải đồng bộ

Nếu Model có:

```python
full_name
```

nhưng PostgreSQL không có:

```sql
full_name
```

thì API có thể trả `500`.

---

## 3. Migration phải thực sự thay đổi schema

Một file migration tồn tại nhưng:

```python
upgrade():
    pass
```

không thể được xem là migration đã hoàn tất.

---

## 4. `alembic current` chưa đủ

Việc Alembic báo:

```text
5614567ad165 (head)
```

chỉ cho biết migration version đang được ghi nhận ở head.

Nó không tự chứng minh rằng database schema có đúng với model hay không.

---

## 5. Docker healthy không có nghĩa application hoàn hảo

Healthcheck chỉ kiểm tra một phần của hệ thống.

---

## 6. Test giúp học debugging

Tôi học cách đi từ:

```text
AssertionError
↓
HTTP status
↓
response body
↓
server log
↓
traceback
↓
SQLAlchemy
↓
PostgreSQL
```

thay vì sửa code theo cảm tính.

---

# ⚠️ 13. Những điểm chưa hoàn thiện — và tôi muốn mentor nhìn thấy

Project này là **learning project**, vì vậy tôi giữ lại các điểm chưa hoàn thiện thay vì biến summary thành một báo cáo “mọi thứ đều hoàn hảo”.

### Database / Migration

- Migration `5614567ad165_add_full_name.py` cần có operation thật sự thêm `full_name`.
- Cần kiểm tra lại schema PostgreSQL sau migration.
- Cần test migration từ database sạch.

### Architecture

- `crud/` và `repositories/` đang cùng tồn tại.
- Cần chọn data-access approach nhất quán.
- Cần kiểm tra Router → Service → Repository có thực sự được sử dụng nhất quán hay không.
- Cần dọn import và code cũ sau refactor.

### Application startup

`app/main.py` hiện vẫn có:

```python
Base.metadata.create_all(bind=engine)
```

với comment cho biết đây là phần tạm giữ trong giai đoạn hiện tại.

Nếu Alembic trở thành nguồn quản lý schema chính, phần này cần được xem xét và loại bỏ khi migration workflow đã ổn định.

### Testing

- Cần chạy toàn bộ test suite sau khi database schema được sửa.
- Cần kiểm tra cả success path và failure path.
- Cần tiếp tục kiểm tra API sau các thay đổi architecture.

### Docker

Project còn warning:

```text
The "UID" variable is not set.
The "GID" variable is not set.
```

Cần quyết định đây có phải cấu hình cần thiết hay chỉ là warning có thể dọn.

---

# 🎯 14. Next Steps

Thứ tự ưu tiên tôi đề xuất:

### 1. Sửa migration `full_name`

Đảm bảo migration thực sự tạo column.

### 2. Kiểm tra database từ trạng thái sạch

Không dựa vào database đã được thao tác thủ công trước đó.

### 3. Chọn architecture cuối cùng

Mục tiêu rõ ràng:

```text
Router
  ↓
Service
  ↓
Repository
  ↓
Database
```

và loại bỏ code/data-access path cũ không còn cần thiết.

### 4. Chạy toàn bộ test

Không chỉ:

```text
GET /users
```

mà toàn bộ:

```text
tests/api
tests/swagger
tests/e2e
```

### 5. Review lại dependency/import

Kiểm tra các file cũ sau refactor để tránh:

```text
duplicate logic
unused code
wrong import
old dependency
```

### 6. Sau đó mới tiếp tục feature mới

Tôi muốn ưu tiên:

```text
Correctness
   ↓
Consistency
   ↓
Testability
   ↓
Clean architecture
   ↓
New features
```

---

# 📚 15. Tôi đã học được gì từ project này?

Nếu tóm tắt thành một câu:

> **Tôi đang học cách biến một API “chạy được” thành một hệ thống mà tôi có thể giải thích được request flow, database flow, migration flow, testing flow và debugging flow.**

Hành trình chính:

```text
FastAPI basics
      ↓
CRUD
      ↓
SQLAlchemy
      ↓
PostgreSQL
      ↓
Docker
      ↓
Alembic
      ↓
Repository Pattern
      ↓
Service Layer
      ↓
Testing
      ↓
Debugging
      ↓
Architecture review
```

Điều quan trọng nhất không phải là project đã hoàn hảo, mà là tôi bắt đầu biết **cách kiểm tra xem nó có thực sự đúng hay không**.

---

# 👩‍🏫 16. Mentor có thể xem project theo cách nhanh nhất

Nếu chỉ có vài phút, có thể đọc theo thứ tự:

1. **File này** — tổng quan hành trình.
2. `app/routers/` — API layer.
3. `app/services/` — business logic.
4. `app/repositories/` + `app/crud/` — data-access và phần đang cần thống nhất.
5. `app/models/` + `app/schemas/` — database/API contract.
6. `alembic/versions/` — database evolution.
7. `tests/` — cách kiểm tra hệ thống.
8. `docs/diary/` — nhật ký chi tiết theo ngày.

### Evidence trực quan

Các screenshot API được README tham chiếu:

- [Authentication screenshot](../../tests/screenshots/Authentication/Authentication%20Post%20Auth%20Login.png)
- [Users screenshot](../../tests/screenshots/User/Test%20Get%20User.png)
- [Posts screenshot](../../tests/screenshots/Post/Get%20Posts.png)
- [Screenshot directory](../../tests/screenshots/)

---

# 🔗 17. Diary Index

| Ngày | Nội dung |
|---|---|
| [28/07](./2026-07-28-current-progress.md) | Project baseline và feature ban đầu |
| [29/07](./2026-07-29-current-progress.md) | SQLAlchemy query và filtering |
| [30/07](./2026-07-30-current-progress.md) | Docker + Alembic |
| [31/07](./2026-07-31-current-progress.md) | Repository Pattern |
| [01/08](./2026-08-01-current-progress.md) | Repository thực hành sâu hơn |
| [02/08](./2026-08-02-current-progress.md) | Architecture và responsibility |
| [03/08](./2026-08-03-current-progress.md) | Service Layer |
| [04/08](./2026-08-04-current-progress.md) | Models & Schemas |
| [05/08](./2026-08-05-current-progress.md) | Testing |
| [06/08](./2026-08-06-current-progress.md) | Docker + Database |
| [07/08](./2026-08-07-current-progress.md) | Alembic + `full_name` |
| [08/08](./2026-08-08-current-progress.md) | Debugging database mismatch |
| **09/08** | **Project summary / mentor overview** |

---

# ❤️ Final Note

Project này là **learning project**, vì vậy tôi không muốn che các lỗi trong quá trình học.

Điều tôi muốn mentor nhìn thấy không chỉ là số lượng folder hay số lượng feature, mà là quá trình:

```text
Thử
 ↓
Sai
 ↓
Đọc log
 ↓
Tìm nguyên nhân
 ↓
Hiểu architecture
 ↓
Refactor
 ↓
Test lại
 ↓
Rút kinh nghiệm
```

Một trong những bài học rõ nhất là:

> **Tách code chỉ là bước đầu. Điều khó hơn là giữ toàn bộ hệ thống đồng bộ: source code, dependency, migration, database schema, test và runtime environment.**

Đó chính là phần giá trị nhất tôi nhận được từ project FastAPI này.
```


---

## `docs/diary/2026-08-10-to-2026-08-28-retrospective-gap.md`

```markdown
# 📚 Retrospective Learning Record — 2026-08-10 → 2026-08-28

> **Lưu ý về tính trung thực:** Khoảng thời gian này không còn log nhật ký nguyên bản theo từng ngày trong project context hiện tại. Vì vậy tôi **không dựng một lịch sử giả**. Tài liệu này ghi nhận khoảng trống và những gì có thể xác nhận từ trạng thái project về sau.

## Vì sao có khoảng trống?

Sau bản tổng hợp ngày 09/08, diary không được cập nhật đều. Project vẫn tiếp tục được thay đổi/refactor, nhưng record hiện có không đủ để xác định chính xác ngày nào thực hiện thay đổi nào.

## Những gì có thể xác nhận

Ở trạng thái project được ghi nhận về sau, kiến trúc đã có:

```text
app/
├── core/
├── models/
├── repositories/
├── routers/
├── schemas/
├── services/
└── utils/
```

Ngoài ra có:

```text
alembic/
tests/
scripts/
Dockerfile
docker-compose.yml
pytest.ini
```

Điều này cho thấy project đã phát triển từ cấu trúc ban đầu sang architecture có nhiều layer hơn.

## Những vấn đề tôi tiếp tục phải kiểm chứng

- Router → Service → Repository có thực sự nhất quán không?
- Có code cũ hoặc duplicate responsibility sau refactor không?
- SQLAlchemy Model và Pydantic Schema có đồng bộ không?
- Alembic migration có phản ánh đúng database schema không?
- Docker healthy có đồng nghĩa business API đúng không?
- pytest đang kiểm tra behavior thực tế đến mức nào?
- Authentication và authorization có được kiểm chứng độc lập không?

## Bài học

Việc bỏ diary một thời gian cho tôi thấy documentation cũng là một phần của engineering workflow.

Từ đây tôi muốn ghi:

```text
Ngày
↓
Mục tiêu
↓
Thực hành
↓
Kết quả
↓
Lỗi
↓
Root cause
↓
Insight
↓
Next step
```

Nếu thiếu log, tôi sẽ ghi rõ **không có log nguyên bản**, thay vì biến suy đoán thành lịch sử.
```


---

## `docs/diary/2026-08-29-current-progress.md`

```markdown
# 📅 Development Diary — 2026-08-29

## Chủ đề
**Kiểm chứng runtime thực tế: authentication và API flow.**

Sau một khoảng thời gian không ghi diary đều đặn, tôi quay lại kiểm chứng project bằng runtime thực tế thay vì chỉ nhìn source code.

### Kết quả đã ghi nhận

- `GET /` → `200 OK`.
- OpenAPI load được các endpoint `/health`, `/auth/login`, `/auth/me`, `/users/`, `/users/{user_id}`, `/posts/`, `/posts/me`, `/posts/{post_id}`.
- `POST /users/` → `201 Created`.
- `POST /auth/login` → `200 OK` và trả JWT.
- Protected endpoints với `$TOKEN` → `401 Could not validate credentials`.

Sau khi kiểm tra terminal, tôi phát hiện `$TOKEN` đang rỗng (`echo "$TOKEN"` không in ra gì). Vì vậy chưa thể kết luận JWT implementation bị lỗi; trước tiên phải lưu access token thật vào biến shell rồi test lại.

### Một vấn đề khác cần điều tra

Request tạo user gửi `role="admin"` nhưng response trả `role="user"`.

Đây là một điểm cần xác định xem là business/security rule có chủ đích hay bug.

### Insight

> Khi debugging, phải kiểm tra runtime state trước khi sửa code và phải phân biệt authentication với authorization.

```


---

## `docs/diary/2026-08-30-current-progress.md`

```markdown
# 📅 Development Diary — 2026-08-30

## Chủ đề
**Tiếp tục refactor Clean Architecture cho FastAPI User Management.**

---

## 1. Kiến trúc được chốt

Kiến trúc mục tiêu:

```text
Router
   ↓
Service
   ↓
Repository
   ↓
Database
```

Router xử lý HTTP. Service xử lý business logic và orchestration. Repository xử lý database access.

---

## 2. CRUD / Repository

Nhận ra project có sự chồng chéo giữa `crud/`, `repository/` và `service/`.

Khi đã có Repository và Service thì CRUD layer cũ không còn cần thiết. Mục tiêu là loại bỏ logic database trùng lặp và giữ flow:

```text
Router → Service → Repository → PostgreSQL
```

---

## 3. Alembic

Thống nhất nguyên tắc:

```text
Alembic → Database schema
```

Không sử dụng `Base.metadata.create_all()` trong `app/main.py`. `main.py` chỉ khởi tạo FastAPI và đăng ký router.

---

## 4. Bài học

Refactor không chỉ là đổi tên folder. Cần kiểm tra import, dependency injection, request flow, transaction, database schema và test.
```


---

## `docs/diary/2026-08-31-current-progress.md`

```markdown
# 📅 Development Diary — 2026-08-31

## Chủ đề
**Hoàn thiện User schema, password handling và response model.**

---

## 1. User schema

Tiếp tục kiểm tra `UserCreate`, `UserUpdate`, `UserPatch` và `UserResponse`.

`full_name` được bổ sung để hỗ trợ tạo và cập nhật đầy đủ thông tin user.

---

## 2. Password

Nguyên tắc:

```text
UserCreate.password
        ↓
Password hashing
        ↓
User.password
        ↓
Database
```

Password không được đưa vào `UserResponse`.

---

## 3. PUT và PATCH

PUT cập nhật resource theo schema đầy đủ. PATCH chỉ cập nhật field được gửi lên.

Ý tưởng quan trọng:

```python
model_dump(exclude_unset=True)
```

để tránh ghi đè field không được gửi.

---

## 4. Bài học

Schema là boundary kiểm soát dữ liệu đi vào và đi ra khỏi API, không chỉ đơn thuần là khai báo kiểu dữ liệu.
```


---

## `docs/diary/2026-09-01-current-progress.md`

```markdown
# 📅 Development Diary — 2026-09-01

## Chủ đề
**Authentication, dependency injection và request flow.**

---

## 1. Authentication flow

```text
POST /auth/login
      ↓
Authenticate user
      ↓
Create JWT
      ↓
Bearer token
      ↓
Protected endpoint
```

---

## 2. Current user

`get_current_user()` đọc Bearer token, decode JWT, lấy `sub`, tìm user theo email và từ chối token/user không hợp lệ.

---

## 3. Dependency Injection

Các service được tạo thông qua dependency:

```text
get_db()
   ↓
get_user_service()
get_post_service()
get_auth_service()
```

Router không tự tạo database session hoặc service bằng logic thủ công.

---

## 4. Ownership

```text
JWT
 ↓
get_current_user()
 ↓
current_user.id
 ↓
PostService
 ↓
ownership check
```

Các endpoint Post protected phải kiểm tra ownership.

---

## 5. Bài học

Authentication không chỉ là tạo token; cần kiểm tra toàn bộ đường đi của token từ request đến business logic và database.
```


---

## `docs/diary/2026-09-02-current-progress.md`

```markdown
# 📅 Development Diary — 2026-09-02

## Chủ đề
**Ổn định Alembic và database schema.**

---

## 1. Migration baseline

Migration cũ không còn phản ánh đúng trạng thái model hiện tại nên được thay bằng baseline mới.

Revision hiện tại:

```text
e7d9b8aad922
```

---

## 2. Alembic state

Đã kiểm tra:

```bash
alembic heads
alembic current
```

Database ở:

```text
e7d9b8aad922 (head)
```

---

## 3. Schema verification

Các thành phần chính:

```text
users
posts
alembic_version
```

Quan hệ:

```text
users.id
    ↓
posts.user_id
```

`users.full_name` đã tồn tại trong schema.

---

## 4. Nguyên tắc

```text
Model change
     ↓
Alembic migration
     ↓
PostgreSQL
```

Không dùng `create_all()` để tự động sửa schema.

---

## 5. Bài học

Python Model, Alembic Migration và PostgreSQL Schema phải được giữ đồng bộ.
```


---

## `docs/diary/2026-09-03-current-progress.md`

```markdown
# 📅 Development Diary — 2026-09-03

## Chủ đề
**API testing bằng pytest.**

---

## 1. Test structure

```text
tests/
├── api/
├── e2e/
├── screenshots/
└── reports/
```

Bắt đầu chuyển trọng tâm từ manual Swagger testing sang automated testing.

---

## 2. API tests

Các nhóm được kiểm tra:

```text
test_users.py
test_auth.py
test_create_user.py
test_health.py
test_posts.py
```

Tập trung vào status code, response body, validation, authentication, authorization, ownership và CRUD behavior.

---

## 3. Post API

Kiểm tra các endpoint create, list, search, current-user posts, get by ID, update, patch và delete.

Ownership được kiểm tra để user không thể sửa/xóa post của user khác.

---

## 4. Bài học

Test cần kiểm tra behavior thực tế của API, không chỉ kiểm tra `200 OK`.
```


---

## `docs/diary/2026-09-04-current-progress.md`

```markdown
# 📅 Development Diary — 2026-09-04

## Chủ đề
**Hoàn thiện API test cho Posts và xử lý test assumption.**

---

## 1. Post tests

Bộ test Posts được mở rộng để kiểm tra:

- create post
- unauthorized request
- get posts
- search
- get my posts
- get post by ID
- not found
- update
- patch
- delete
- ownership forbidden
- invalid title

Tổng cộng:

```text
12 tests
```

---

## 2. Test assumption

Một test giả định thứ tự các post trong response, trong khi repository chưa cam kết thứ tự đó.

Test được sửa để kiểm tra requirement thực tế, không phụ thuộc vào thứ tự không được quy định.

---

## 3. Kết quả

```text
tests/api/test_posts.py
12 passed
```

Các nhóm API test trước đó cũng pass. Tổng API tests:

```text
22 passed
```

Có 2 deprecation warnings từ dependency, nhưng không phải test failure.

---

## 4. Bài học

Cần phân biệt implementation bug và test assumption bug. Không nên sửa production code chỉ để thỏa mãn một assumption không nằm trong requirement.
```


---

## `docs/diary/2026-09-05-current-progress.md`

```markdown
# 📅 Development Diary — 2026-09-05

## Chủ đề
**Playwright E2E và automated screenshot evidence cho Swagger UI.**

---

## 1. Playwright

Bắt đầu sử dụng Playwright để kiểm tra Swagger UI bằng Firefox.

```text
Firefox
   ↓
Swagger UI
   ↓
API endpoint
   ↓
Response
   ↓
Screenshot evidence
```

---

## 2. E2E test

Tạo:

```text
tests/e2e/test_swagger_capture.py
tests/e2e/utils.py
```

Thêm:

```text
tests/__init__.py
tests/e2e/__init__.py
```

---

## 3. Helper

Các thao tác chung:

```text
open_swagger()
get_post_endpoint()
click_try_it_out()
click_execute()
fill_request_body()
screenshot()
```

Mục tiêu là giảm code lặp và giữ test dễ đọc.

---

## 4. Screenshot evidence

```text
tests/screenshots/
├── 01_swagger_home.png
├── 02_swagger_endpoints.png
└── 03_swagger_create_user_success.png
```

Hai screenshot đầu được kiểm tra và xác nhận giao diện giống Swagger UI khi mở thủ công bằng Firefox.

---

## 5. POST /users/

```text
Open Swagger
    ↓
POST /users/
    ↓
Try it out
    ↓
Fill request body
    ↓
Execute
    ↓
Check 201
    ↓
Check response body
    ↓
Screenshot
```

---

## 6. Điểm dừng

Workflow tiếp theo:

```text
POST /users/
    ↓
POST /auth/login
    ↓
Authorize
    ↓
POST /posts/
    ↓
GET /posts/{post_id}
    ↓
PATCH /posts/{post_id}
    ↓
DELETE /posts/{post_id}
```

Authentication và Posts E2E chưa hoàn thiện.
```


---

## `docs/diary/2026-09-06-current-progress.md`

```markdown
# 📅 Development Diary — 2026-09-06

## Chủ đề
**Playwright E2E, Swagger UI và Docker environment persistence.**

Hôm nay tiếp tục phần Testing của project FastAPI User Management, tập trung vào việc chạy E2E test bằng Playwright trên Firefox và đảm bảo môi trường Playwright không bị mất sau khi `docker compose down`.

---

## 1. Playwright E2E

Project hiện có:

```text
tests/
├── api/
├── e2e/
│   ├── __init__.py
│   ├── test_swagger_capture.py
│   └── utils.py
├── screenshots/
└── reports/
```

Đã thêm `tests/__init__.py` và `tests/e2e/__init__.py`.

---

## 2. Swagger UI

E2E test sử dụng Firefox để mở:

```text
http://api:8000/docs
```

Đã kiểm tra Swagger UI, OpenAPI document, API title và các endpoint chính `/health`, `/auth/login`, `/users/`, `/posts/`. Swagger UI cũng có thể tìm và thao tác với POST `/users/`.

Helper dùng chung được tách vào `tests/e2e/utils.py`:

```text
open_swagger()
get_post_endpoint()
click_try_it_out()
click_execute()
fill_request_body()
screenshot()
```

---

## 3. Screenshot evidence

```text
tests/screenshots/
├── 01_swagger_home.png
├── 02_swagger_endpoints.png
└── 03_swagger_create_user_success.png
```

Hai screenshot đầu được kiểm tra và xác nhận giao diện giống Swagger UI khi mở thủ công bằng Firefox tại `http://127.0.0.1:8000/docs#/`.

Screenshot thứ ba ghi lại kết quả thành công của POST `/users/`.

---

## 4. Firefox bị mất sau khi recreate container

Ban đầu Playwright báo:

```text
BrowserType.launch:
Executable doesn't exist at
/root/.cache/ms-playwright/firefox-1538/firefox/firefox
```

Firefox trước đó được cài thủ công bằng:

```bash
docker compose exec api playwright install firefox
```

Browser nằm trong container đang chạy. Sau `docker compose down`, container cũ bị remove nên browser binary cũng mất.

---

## 5. Đưa Firefox vào Dockerfile

Để môi trường E2E reproducible, thêm:

```dockerfile
RUN playwright install --with-deps firefox
```

`--with-deps` cần thiết vì Firefox còn cần các system libraries để chạy.

---

## 6. Kiểm tra Docker image

Đã chạy:

```bash
docker compose up --build -d
docker compose down
docker compose up -d
```

Sau đó:

```bash
docker compose exec api playwright install --list
```

Kết quả:

```text
Playwright version: 1.62.0

Browsers:
    /root/.cache/ms-playwright/ffmpeg-1011
    /root/.cache/ms-playwright/firefox-1538
```

Điều này xác nhận Firefox nằm trong môi trường container được tạo từ Docker image.

---

## 7. E2E test cuối ngày

Đã chạy:

```bash
docker compose exec -e PYTHONPATH=/app api pytest -q tests/e2e --browser firefox
```

Kết quả:

```text
collected 3 items
tests/e2e/test_swagger_capture.py ... [100%]

3 passed, 2 warnings in 6.70s
```

Tests:

```text
✅ test_swagger_health
✅ test_swagger_openapi
✅ test_swagger_create_user
```

2 warnings là deprecation warning từ Starlette/AnyIO và Passlib/crypt; không phải test failure.

---

## 8. Trạng thái cuối ngày

```text
FastAPI
   ↓
Docker Compose
   ↓
PostgreSQL
   ↓
Alembic
   ↓
Pytest API
   ↓
Playwright E2E
   ↓
Firefox
   ↓
Swagger UI
   ↓
Screenshot evidence
```

Các phần quan trọng đang hoạt động:

- ✅ FastAPI
- ✅ PostgreSQL
- ✅ Docker Compose
- ✅ Alembic
- ✅ API tests
- ✅ Swagger UI
- ✅ Playwright
- ✅ Firefox
- ✅ Automated screenshot
- ✅ E2E test
- ✅ Docker image chứa Firefox
- ✅ Firefox không còn phụ thuộc vào việc cài thủ công trong container hiện tại

---

## 9. Điểm dừng hôm nay

```text
Swagger UI
    ↓
POST /users/
    ↓
Playwright
    ↓
Firefox
    ↓
3 E2E tests PASS
```

Chưa tiếp tục sang toàn bộ workflow authentication và Posts.

Phần tiếp theo:

```text
POST /users/
      ↓
POST /auth/login
      ↓
Authorize
      ↓
POST /posts/
      ↓
GET /posts/{post_id}
      ↓
PATCH /posts/{post_id}
      ↓
DELETE /posts/{post_id}
      ↓
Screenshot evidence
```

---

## 📌 Commands đã xác nhận hoạt động

```bash
docker compose up --build -d
docker compose down
docker compose up -d
docker compose exec api playwright install --list
docker compose exec -e PYTHONPATH=/app api pytest -q tests/e2e --browser firefox
```

Kết quả cuối ngày:

```text
3 passed, 2 warnings
```

---

## ❤️ Ghi chú

> **Environment cũng là một phần của project.**

Không chỉ source code cần đúng. Browser, system dependencies, Python packages và Docker image cũng phải được quản lý để test có thể chạy ổn định sau khi container được tạo lại.

Bài học này nối tiếp nguyên tắc lớn của project: **tách code chỉ là bước đầu; điều khó hơn là giữ source code, dependency, migration, database schema, test và runtime environment đồng bộ.**
```


---

## `docs/diary/2026-09-07-current-progress.md`

```markdown
# Diary – 07/09/2026

Hôm nay em tiếp tục rà lại project FastAPI User Management. Sau khi đã làm xong phần API cơ bản thì em không muốn thêm feature mới ngay mà quay lại kiểm tra những phần cũ.

Em chủ yếu xem lại User, Auth, Post và cách các phần này liên quan với nhau.

Flow em đang hướng tới là:

Create User → Login → lấy JWT → Authorize → Post

Lúc đọc lại code em thấy các phần liên quan với nhau khá nhiều nên khi test một phần bị lỗi thì phải quay lại kiểm tra cả những bước trước.

Em bắt đầu tập trung nhiều hơn vào phần testing thay vì chỉ kiểm tra API bằng Swagger thủ công.

**Tình trạng:** Chưa có lỗi mới rõ ràng nhưng bắt đầu bị chậm vì phải rà lại nhiều phần.
```


---

## `docs/diary/2026-09-08-current-progress.md`

```markdown
# Diary – 08/09/2026

Hôm nay em tiếp tục kiểm tra phần User và Auth.

Em thử lại flow tạo user rồi login để lấy access token. Sau đó kiểm tra việc dùng Bearer token cho các endpoint cần authentication.

Phần này giúp em hiểu rõ hơn là API login trả token chưa có nghĩa là toàn bộ flow authentication đã ổn. Khi sang endpoint protected thì còn liên quan đến dependency lấy current user, token và quyền của user.

Em cũng xem lại test cũ và chỉnh lại một số phần để test dễ đọc hơn.

Sau đó em bắt đầu nghĩ đến việc đưa flow này vào E2E thay vì chỉ test từng API riêng lẻ.

**Tình trạng:** Vẫn làm được từng phần nhưng khi nối thành một flow thì bắt đầu phát sinh vấn đề.
```


---

## `docs/diary/2026-09-09-current-progress.md`

```markdown
# Diary – 09/09/2026

Hôm nay em chuyển sang phần Swagger UI + Playwright.

Mục tiêu là dùng browser để test giống cách người dùng thao tác trên Swagger:

Open Swagger → chọn endpoint → Try it out → nhập dữ liệu → Execute

Em bắt đầu làm test cho Post vì phần Post cần user đã đăng nhập và có token.

Trong lúc làm em gặp khá nhiều vấn đề với locator của Swagger. Có lúc locator tìm đúng endpoint nhưng Playwright vẫn không click được.

Em phải đọc lại log của Playwright để xem element nào đang nằm phía trên và đang chặn thao tác.

**Tình trạng:** Bắt đầu bị kẹt ở phần E2E, chưa đi được nhanh như dự kiến.
```


---

## `docs/diary/2026-09-10-current-progress.md`

```markdown
# Diary – 10/09/2026

Hôm nay em tiếp tục debug phần Swagger E2E.

Em kiểm tra lại flow Authorize. Ý định là sau khi login lấy được token thì đưa token vào Swagger Authorize, sau đó mới thực hiện POST /posts/.

Vấn đề là Swagger có modal Authorize và backdrop phía sau. Sau khi authorize xong, em tưởng modal đã đóng nhưng Playwright vẫn thấy .backdrop-ux còn visible.

Vì vậy khi test cố click sang endpoint /posts/ thì bị lỗi do overlay đang chặn pointer events.

Em thử kiểm tra locator và thứ tự thao tác thay vì chỉ tăng thời gian chờ.

**Tình trạng:** Chưa fix được. Em bắt đầu mất khá nhiều thời gian ở phần UI của Swagger chứ không phải ở API Post.
```


---

## `docs/diary/2026-09-11-current-progress.md`

```markdown
# Diary – 11/09/2026

Hôm nay em tiếp tục rà lại phần Post và E2E.

Em không muốn sửa API Post lung tung khi chưa chắc lỗi nằm ở API hay ở browser test nên tập trung tách hai vấn đề này ra.

Flow em muốn test là:

Create User
→ Login
→ Authorize
→ POST /posts/
→ GET /posts/{post_id}
→ PATCH /posts/{post_id}
→ DELETE /posts/{post_id}

Em kiểm tra lại helper trong tests/e2e/utils.py, đặc biệt là phần tìm endpoint và các thao tác Try it out / Execute.

Locator của /posts/ có thể tìm được endpoint, nhưng vấn đề vẫn nằm ở bước sau Authorize.

**Tình trạng:** Flow Post chưa chạy xuyên suốt được.
```


---

## `docs/diary/2026-09-12-current-progress.md`

```markdown
# Diary – 12/09/2026

Hôm nay em tiếp tục thử chạy test trong Docker.

Em muốn đảm bảo test chạy trong đúng môi trường project chứ không chỉ chạy riêng ở máy local.

Em chạy pytest với Firefox trong container và kiểm tra lại log.

Có một số warning liên quan đến UID và GID, nhưng em đang cố tách warning này ra khỏi lỗi chính để không sửa nhầm vấn đề.

Lỗi chính vẫn là Swagger Authorize chưa đóng overlay đúng cách. Vì vậy khi Playwright chuyển sang POST /posts/ thì thao tác click bị chặn.

Em có thử thêm bước wait nhưng cảm giác chỉ wait lâu hơn không giải quyết được nguyên nhân thật sự.

**Tình trạng:** Vẫn bị kẹt ở Authorize → Post.
```


---

## `docs/diary/2026-09-13-current-progress.md`

```markdown
# Diary – 13/09/2026

Hôm nay em chạy lại test E2E:

tests/e2e/test_swagger_posts.py

Test được chạy trong Docker bằng Firefox.

Kết quả hiện tại:

1 failed, 2 warnings

Lỗi xảy ra ở bước kiểm tra backdrop của Swagger:

expect(backdrop).to_be_hidden()

Nhưng thực tế .backdrop-ux vẫn đang visible.

Sau đó nếu tiếp tục click endpoint thì overlay có thể chặn pointer event.

Qua lỗi này em thấy vấn đề hiện tại chưa chắc nằm ở Post API hay database mà nhiều khả năng nằm ở trạng thái của Swagger UI sau khi Authorize.

Em đã thử hướng wait nhưng chưa fix dứt điểm được.

Hiện tại em chưa muốn đi tiếp thêm feature vì nếu flow User → Auth → Authorize → Post chưa ổn thì test các bước GET/PATCH/DELETE phía sau cũng khó kiểm tra chính xác.

**Tình trạng cuối tuần:** Vẫn đang kẹt ở E2E Swagger Authorize → Post. Chưa hoàn thành flow Post như kế hoạch.
```


---

## `docs/diary/2026-09-24-current-progress.md`

```markdown
# 📅 Development Diary — 2026-09-24

## Chủ đề
**Phân tích sự phân mảnh giữa `crud/` và `repositories/` trước khi tiến hành Refactor.**

---

## 1. Vấn đề phát hiện
Khi rà soát lại toàn bộ cây thư mục mã nguồn để chuẩn bị cho giai đoạn tối ưu hóa, tôi nhận thấy dự án đang rơi vào tình trạng **Split Responsibility (Phân mảnh trách nhiệm)** ở tầng truy cập dữ liệu:
* Thư mục `app/crud/` cũ (từ giai đoạn phát triển ban đầu) và thư mục `app/repositories/` mới đang cùng tồn tại song song.
* Một số hàm ở Router vẫn gọi gián tiếp qua cơ chế cũ, trong khi các tính năng nâng cao lại dùng cơ chế Class Injection của tầng Repository.
* `app/main.py` vẫn giữ lệnh cấu hình thô:
  ```python
  Base.metadata.create_all(bind=engine)
  ```
  Điều này gây xung đột vùng xám với lịch sử di cư (Migration Chain) của **Alembic** (`e7d9b8aad922_initial_schema.py`).

---

## 2. Giải pháp kiến trúc đề xuất
Tôi quyết định thiết lập một kế hoạch refactor nghiêm túc để ép toàn bộ luồng request chạy qua một trục duy nhất:
```text
Router (HTTP) ➔ Service (Business/Orchestration) ➔ Repository (Data Access) ➔ PostgreSQL
```
* **Hành động 1:** Chuyển dịch toàn bộ logic database còn sót lại từ `crud/` sang các hàm nghiệp vụ của `UserRepository` và `PostRepository`.
* **Hành động 2:** Vô hiệu hóa hoàn toàn lệnh `create_all()` tại file khởi chạy để giao trọn quyền quản trị Schema cho hệ thống Migration.

---

## 3. Bài học rút ra
Tách folder chỉ là hình thức bên ngoài. Để đạt được Clean Architecture thực sự, cấu trúc dữ liệu đi vào và đi ra giữa các lớp ranh giới phải có sự nhất quán và không được chồng chéo trách nhiệm lên nhau.
```


---

## `docs/diary/2026-09-25-current-progress.md`

```markdown
# 📅 Development Diary — 2026-09-25

## Chủ đề
**Thực hiện Refactor hạ tầng dữ liệu và bàn giao toàn quyền cho Alembic.**

---

## 1. Các hạng mục đã thực hiện

### 🔹 Cập nhật `app/main.py`
Tôi đã mở tệp khởi chạy ứng dụng và tiến hành **xóa bỏ hoàn toàn** dòng lệnh cấu hình tự động sinh bảng:
```python
# ĐÃ XÓA: Base.metadata.create_all(bind=engine)
```
Từ thời điểm này, toàn bộ vòng đời của cơ sở dữ liệu (PostgreSQL 16) sẽ được kiểm soát nghiêm ngặt thông qua lệnh di cư:
```bash
docker compose exec api alembic upgrade head
```

### 🔹 Làm sạch dự án
Để đảm bảo mã nguồn không còn tài liệu hay tàn dư gây nhiễu, tôi tiến hành xóa sổ hoàn toàn thư mục cũ bằng lệnh hệ thống trên máy host:
```bash
rm -rf app/crud/
```

### 🔹 Tối ưu hóa môi trường Test (`pytest.ini`)
Trong các đợt chạy test trước, màn hình console bị tràn ngập các dòng thông báo màu vàng `DeprecationWarning` từ thư viện `starlette`. Tôi đã bổ sung cấu hình bộ lọc cảnh báo vào `pytest.ini` để làm sạch báo cáo đầu ra:
```ini
filterwarnings =
    ignore::DeprecationWarning:starlette.*
```

---

## 2. Kết quả đạt được
* Kiến trúc dự án trở nên đồng nhất, gọn gàng theo chuẩn Layered Architecture.
* Không còn rủi ro ghi đè hoặc tự động sửa đổi bảng ngoài ý muốn từ SQLAlchemy ORM khi chạy ứng dụng trên môi trường Production.
```


---

## `docs/diary/2026-09-26-current-progress.md`

```markdown
# 📅 Development Diary — 2026-09-26

## Chủ đề
**Xử lý cảnh báo môi trường Docker Linux (UID/GID) và tối ưu hóa tốc độ Test.**

---

## 1. Vấn đề rào cản môi trường
Mỗi khi tôi thực hiện các lệnh gọi kiểm thử hoặc vận hành container, hệ thống liên tục đưa ra cảnh báo:
```text
WARN[0000] The "UID" variable is not set. Defaulting to a blank string.
WARN[0000] The "GID" variable is not set. Defaulting to a blank string.
```
Nguyên nhân do Docker Compose cố gắng map quyền sở hữu tệp tin (`user: "${UID}:${GID}"` trong `docker-compose.yml`) giữa máy Host chạy Linux Ubuntu và môi trường ảo hóa bên trong Container nhưng hai biến này chưa được khởi tạo ở môi trường cục bộ.

---

## 2. Giải pháp khắc phục
Tôi đã tiến hành nạp trực tiếp mã định danh định danh User (UID) và Group (GID) của tài khoản hệ điều hành hiện tại vào tệp cấu hình ẩn `.env`:
```bash
echo "UID=\$(id -u)" >> .env
echo "GID=\$(id -g)" >> .env
```
Sau đó tiến hành khởi động lại toàn bộ các dịch vụ để áp dụng:
```bash
docker compose down && docker compose up -d
```

---

## 3. Bước nhảy vọt về hiệu năng kiểm thử
Sau khi dọn sạch các cảnh báo môi trường và cấu hình ẩn Warning Starlette, tôi thực hiện chạy bộ thử nghiệm giả lập E2E trên trình duyệt Firefox:
```bash
docker compose exec api pytest tests/e2e -v --browser firefox
```
* **Kết quả:** **PASSED 100% (9/9 tests E2E thành công)**.
* **Thời gian thực thi:** Giảm mạnh từ **95.70 giây xuống còn 20.75 giây** (Nhanh gấp 4.5 lần). Việc giải phóng các cảnh báo nghẽn luồng và làm sạch cache giúp Playwright tương tác với phần tử Swagger UI mượt mà hơn rất nhiều.
```


---

## `docs/diary/2026-09-27-current-progress.md`

```markdown
# 📅 Development Diary — 2026-09-27

## Chủ đề
**Thiết kế và tích hợp Server-Side Pagination & Search cho bảng dữ liệu Users.**

---

## 1. Mục tiêu nghiệp vụ
Hiện tại endpoint `GET /users/` đang lấy ra toàn bộ danh sách người dùng trong hệ thống mà không có sự kiểm soát về dung lượng. Nếu số lượng tài khoản lên tới hàng vạn, việc này sẽ gây nghẽn băng thông truyền tải dữ liệu và tràn bộ nhớ đệm của API. 

Mục tiêu hôm nay là áp dụng bộ lọc phân trang chủ động (Pagination) và tìm kiếm không phân biệt hoa thường (Case-Insensitive Search) theo đúng mô hình 3 lớp.

---

## 2. Mã nguồn triển khai chi tiết

### 🔹 Lớp Dữ liệu (`app/repositories/user_repository.py`)
Nâng cấp hàm `get_all` để nhận tham số lọc, sử dụng cấu trúc toán tử logic toán tử `OR` (`|`) để tìm kiếm song song cả tên hoặc email:
```python
def get_all(self, limit: int = 10, offset: int = 0, search: str = "") -> list[User]:
    statement = select(User).options(joinedload(User.posts))
    
    if search:
        statement = statement.where(
            User.name.ilike(f"%{search}%") | 
            User.email.ilike(f"%{search}%")
        )
        
    statement = statement.order_by(asc(User.id)).offset(offset).limit(limit)
    return list(self.db.scalars(statement).unique().all())
```

### 🔹 Lớp Nghiệp vụ (`app/services/user_service.py`)
Mở rộng hàm chuyển tiếp tham số điều phối dữ liệu từ tầng trên xuống kho lưu trữ:
```python
def get_users(self, limit: int = 10, offset: int = 0, search: str = "") -> list[User]:
    return self.repository.get_all(limit=limit, offset=offset, search=search)
```

### 🔹 Lớp Giao tiếp (`app/routers/user.py`)
Định nghĩa Query Parameter kèm điều kiện ràng buộc dữ liệu đầu vào thông qua đối tượng `Query` của FastAPI:
```python
@router.get("/", response_model=APIResponse, summary="Get all users")
def get_users(
    limit: int = Query(default=10, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    search: str = Query(default="", max_length=100),
    service: UserService = Depends(get_user_service),
    admin: User = Depends(get_admin_user)
):
    users = service.get_users(limit=limit, offset=offset, search=search)
    data = [UserResponse.model_validate(user).model_dump() for user in users]
    return response("Users retrieved successfully", data)
```

---

## 3. Tình trạng cuối ngày
Tính năng đã được tích hợp thành công lên hệ thống thực thi runtime. Kiểm tra Swagger UI cho thấy các tham số đầu vào hiển thị tường minh và chính xác. Tiến hành thực hiện lệnh lưu vết Git an toàn trước khi đăng xuất hệ thống:
```bash
git add .
git commit -m "feat: add pagination and search queries to get all users endpoint"
```
```


---

## `docs/diary/2026-09-28-future-plan.md`

```markdown
# 📅 Development Diary — 2026-09-28

## Chủ đề
**Kế hoạch ngày làm việc tiếp theo: Viết bộ test phân trang và thiết lập Endpoint Analytics.**

---

## 1. Trạng thái xuất phát điểm (Baseline)
Hệ thống hiện tại đang dừng ở trạng thái cực kỳ ổn định:
* Tầng `crud` lai căng đã được xóa bỏ hoàn toàn.
* Toàn bộ **31/31 kiểm thử tự động** (API + E2E Playwright Swagger) đều đạt trạng thái **PASSED 100%**.
* Tính năng phân trang đầu cuối cho danh sách người dùng đã chạy ổn định trên môi trường thực tế nhưng **chưa có ca kiểm thử tự động (`pytest`) nào bao phủ**.

---

## 2. Kế hoạch hành động chi tiết cho ngày mai

### 📌 Nhiệm vụ 1: Bổ sung Test Coverage cho tính năng Phân trang User
Tôi sẽ mở file `tests/api/test_users.py` và viết thêm 3 ca kiểm thử mới:
1. `test_get_users_pagination`: Tạo hàng loạt user giả lập bằng vòng lặp, sau đó gọi API với các cặp tham số `limit=2&offset=0` và `limit=2&offset=2` để đối chiếu tính chính xác của dữ liệu trả về dựa trên ID tăng dần.
2. `test_get_users_search_by_name`: Kiểm tra tính năng tìm kiếm tài khoản theo từ khóa tên.
3. `test_get_users_search_by_email`: Kiểm tra tính năng lọc tài khoản theo đuôi email.

### 📌 Nhiệm vụ 2: Đưa tầng xử lý số liệu Analytics lên Web API
Hiện tại gói phân tích dữ liệu chuyên sâu nâng cao của dự án (`analytics/charts.py`, `analytics/user_analysis.py`) mới chỉ chạy độc lập dưới dạng file kịch bản cục bộ hoặc nhúng thô ở một router đơn sơ.
* Tôi sẽ tiến hành tích hợp toàn diện các hàm tính toán thống kê (Tính độ lệch chuẩn độ tuổi `age_std`, tìm trung vị tuổi `age_median`, đếm số lượng bài viết trung bình của từng vai trò quản trị) để tạo thành một endpoint API chính thức có đường dẫn:
  ```text
  GET /analytics/users/summary
  ```
  Endpoint này sẽ được cấu hình bảo mật cao, chỉ cho phép những tài khoản có quyền `admin` truy cập để xem báo cáo tổng quan hệ thống.
### ⚠️ Ghi chú Debug lỗi hệ thống ngày 27/09:
* **Hiện tượng:** Xung đột plugin `pytest-html` gây crash lỗi `pytest_sessionfinish` khi khởi tạo lại container sạch.
* **Bài học/Giải pháp:** Phải chạy `mkdir -p tests/reports && chmod 777 tests/reports` trên máy host để cấp quyền ghi tệp báo cáo cho Docker, hoặc thêm cờ `-p no:html` khi cần quét nhanh kiểm thử.
```


---

## `docs/diary/2026-09-29-current-progress.md`

```markdown
# Hoàn thiện Authentication và kiểm tra project

## 📝 Công việc đã làm

Trong ngày đầu tiên của tuần, tôi tiếp tục kiểm tra phần authentication của project **FastAPI User Management**.

Tôi tập trung vào phần **password security**, đặc biệt là các hàm:
* `hash_password()`
* `verify_password()`
* `create_access_token()`

Project đang sử dụng `pwdlib` với **Argon2** để hash password và `python-jose` để tạo **JWT**.

Tôi chạy thử trực tiếp các hàm hash và verify trong container để kiểm tra:
- [x] Password đúng có verify thành công không.
- [x] Password sai có bị từ chối không.
- [x] Password có được lưu dưới dạng hash hay không.

> **Kết quả:** Quá trình password hashing và verification hoạt động chính xác.

Tôi cũng kiểm tra lại cách tạo access token và cập nhật phần xử lý thời gian sang `datetime` có timezone **UTC**.

---

## 🐳 Docker

Trong quá trình chạy `docker-compose`, tôi gặp một số cảnh báo (*warning*):
```text
The "UID" variable is not set.
The "GID" variable is not set.
```

**Cách xử lý:**
1. Kiểm tra lại cấu hình Docker Compose configuration.
2. Kiểm tra cách container API được khởi chạy.

Sau khi điều chỉnh cấu hình, API vẫn hoạt động bình thường và không ảnh hưởng đến dữ liệu **PostgreSQL** hiện tại.

---

## 🚀 Kết quả

Kiểm tra trạng thái hoạt động (*Health check*) của API:

```bash
curl http://localhost:8000/health
```

Kết quả trả về:
```json
{
  "status": "healthy",
  "api": "running",
  "database": "connected"
}
```

Qua phần này, tôi hiểu rõ hơn về cách kiểm tra một backend service đang chạy, cũng như cách kiểm tra nhanh kết nối giữa API với database.
```


---

## `docs/diary/2026-09-30-current-progress.md`

```markdown
# Debug Playwright Firefox trong Docker

## 📝 Công việc đã làm

Hôm nay tôi tập trung vào việc chạy **E2E test** bằng **Playwright** với trình duyệt **Firefox** bên trong Docker.

Ban đầu, API vẫn chạy bình thường nhưng Firefox không thể khởi động bên trong container. Lỗi gặp phải như sau:

```text
Sandbox: CanCreateUserNamespace() clone() failure: EPERM
```

**Phân tích ban đầu:**
* Tôi đã kiểm tra lại quá trình cài đặt Playwright và Firefox nhưng nhận ra vấn đề không nằm ở việc cài thiếu package.
* Nguyên nhân gốc rễ liên quan đến **sandbox** và **Linux user namespace** bên trong Docker container.

---

## 🔍 Quá trình Debug

Tôi tiến hành kiểm tra việc tạo user namespace bên trong container và phát hiện **Docker security profile** đang ngăn chặn thao tác này.

**Giải pháp xử lý:**
Sau khi tìm hiểu và thử nghiệm, tôi đã bổ sung cấu hình `security_opt` vào container API trong môi trường development hiện tại:

```yaml
security_opt:
  - seccomp:unconfined
```

**Kết quả sau cấu hình:**
* Tiến hành rebuild và restart lại container, Firefox đã có thể khởi động thành công.
* Tôi đã kiểm tra trực tiếp việc launch Firefox trước khi chạy toàn bộ E2E test.
* **Kết quả:** `Firefox launch OK`

---

## 💡 Bài học kinh nghiệm

Qua lỗi này, tôi rút ra được bài học rằng khi một chương trình chạy tốt ở máy local nhưng thất bại trong Docker, nguyên nhân có thể nằm ở:
* **Permission** (Quyền truy cập)
* **Sandbox** (Cơ chế cô lập)
* **Security profile** (Cấu hình bảo mật)
* **Container configuration** (Cấu hình container)

> 📌 **Lưu ý quan trọng:** Cấu hình `seccomp:unconfined` hiện tại chỉ được áp dụng để phục vụ môi trường **development / E2E test** và **không** được xem là cấu hình mặc định khi triển khai lên môi trường **production** để đảm bảo tính an toàn hệ thống.
```


---

## `docs/diary/2026-10-01-current-progress.md`

```markdown
# Chạy lại toàn bộ test và kiểm tra database

## 🧪 Quá trình Testing

Sau khi xử lý thành công vấn đề với Playwright Firefox, tôi tiến hành chạy lại toàn bộ API test và E2E test bằng lệnh sau:

```bash
docker compose exec \
  -e PYTHONPATH=/app \
  api pytest -q \
  tests/api tests/e2e \
  --browser firefox \
  --cov=app \
  --cov-report=term-missing \
  --cov-report=html
```

**Kết quả kiểm thử:**
* **Tổng số:** `31 passed`
  * bao gồm **22 API tests** và **9 E2E tests**.
* **Mức độ bao phủ (Coverage):** Đạt khoảng **79%**.

Tôi cũng đã khởi tạo **HTML coverage report** để xem chi tiết những phần code nào đã được test và những phần nào còn đang bị thiếu sót.

---

## 🗄️ Cấu trúc PostgreSQL và Alembic

Tôi đã thực hiện kiểm tra lại database và quá trình migration:
* **Alembic current state:** Đang ở revision `e7d9b8aad922 (head)`.
* **Quản lý Schema:** Project hiện tại đã **không còn** sử dụng `create_all()` trong file `main.py` để tự tạo schema tự động khi application khởi động. Việc quản lý và cập nhật database schema hoàn toàn được thực hiện thông qua **Alembic migration**.
* **Dữ liệu:** Tôi đã xác nhận lại PostgreSQL container và đảm bảo toàn bộ dữ liệu vẫn được lưu trữ an toàn, độc lập trong **Docker volume**.

---

## 💡 Bài học kinh nghiệm

* **Phân biệt kiểm thử:** Hiểu rõ hơn sự khác nhau giữa **API test** (tập trung vào từng API/chức năng cụ thể) và **E2E test** (kiểm tra toàn bộ luồng hoạt động thực tế gần nhất với cách người dùng cuối sử dụng hệ thống).
* **Bản chất của Test Coverage:** Hiểu thêm rằng *coverage* là một chỉ số tốt giúp đo lường mức độ mã nguồn được kiểm thử, tuy nhiên coverage đạt tỷ lệ cao không đồng nghĩa với việc project chắc chắn hoàn toàn sạch bug.
```


---

## `docs/diary/2026-10-02-current-progress.md`

```markdown
# Bắt đầu học NumPy và Pandas

## 📊 Bắt đầu phần Data Analysis

Sau khi phần backend và testing đã tương đối ổn định, tôi chuyển sang lộ trình học tập mới bao gồm các thư viện:
* **NumPy**
* **Pandas**
* **Matplotlib**

Để chuẩn bị, tôi đã tạo riêng thư mục `practice/` để chứa toàn bộ mã nguồn thực hành, nhằm đảm bảo cô lập hoàn toàn và không làm ảnh hưởng đến mã nguồn production của dự án.

---

## 💾 Làm việc với dữ liệu User

Tôi thực hiện kết nối và trích xuất dữ liệu `User` trực tiếp từ cơ sở dữ liệu **PostgreSQL** thông qua **SQLAlchemy**, sau đó chuyển đổi tập dữ liệu này thành một **Pandas DataFrame**.

### Cấu trúc dữ liệu thu được:
* **Kích thước:** `93 rows` × `5 columns`
* **Chi tiết các trường thông tin (Fields):**

| Model thực tế trong DB | DataFrame thu được |
| :--- | :--- |
| `id`, `name`, `email`, `role`, `password`, `full_name` | `id`, `name`, `email`, `role`, `full_name` *(loại bỏ `password`)* |

---

## 🧮 Thực hành với NumPy

Tôi làm quen với các phép toán thống kê cơ bản của **NumPy** bao gồm:
* `mean` (trung bình)
* `median` (trung vị)
* `min` / `max` (giá trị nhỏ nhất / lớn nhất)
* `sum` (tổng)
* `std` (độ lệch chuẩn)

> 💡 **Bài học rút ra:** Ban đầu, tôi sử dụng cột `id` để luyện tập các phép tính trên. Tuy nhiên, tôi nhanh chóng nhận ra rằng vì `id` chỉ đóng vai trò là định danh (*identifier*), các chỉ số thống kê toán học trên cột này hoàn toàn không mang lại giá trị hay ý nghĩa về mặt nghiệp vụ (*business logic*). Mặc dù vậy, bài tập này vẫn giúp tôi hiểu rõ cách thức NumPy xử lý và vận hành trên các mảng dữ liệu số.

---

## 🐛 Lỗi gặp phải trong quá trình thực hành

Trong đoạn code ban đầu, tôi đã gọi ra trường dữ liệu `username` theo thói quen cũ. Do model thực tế không tồn tại trường này, hệ thống đã trả về cảnh báo lỗi:

```text
AttributeError: 'User' object has no attribute 'username'
```

**Cách xử lý:** Tôi đã tiến hành đối chiếu lại cấu trúc định nghĩa của model `User` và điều chỉnh mã nguồn để sử dụng chính xác các trường dữ liệu hiện có (`id`, `name`, `email`, `role`, `full_name`).

---

## 💡 Bài học kinh nghiệm

* **Tránh tư duy lối mòn:** Khi làm việc với một dự án thực tế có sẵn, tuyệt đối không được tự giả định cấu trúc dữ liệu hay các model sẽ giống hệt với các bài hướng dẫn (*tutorials*) trên mạng.
* **Quy trình chuẩn:** Luôn có bước kiểm tra, rà soát lại cấu trúc thực tế của database schema hoặc file định nghĩa model trước khi bắt tay vào viết code xử lý dữ liệu.
```


---

## `docs/diary/2026-10-03-current-progress.md`

```markdown
# Học Pandas: Filter, Sort và GroupBy

## 📂 Thao tác với DataFrame

Hôm nay tôi tiếp tục làm việc với file `practice/pandas_lesson2.py` để thực hành các cách trích xuất dữ liệu từ DataFrame.

* **Chọn một column:**
  ```python
  df["name"]
  ```
* **Chọn nhiều column:**
  ```python
  df[["name", "email", "role"]]
  ```

Tôi cũng thử trích xuất đồng thời `df[["name", "full_name"]]` để quan sát và đối chiếu mối quan hệ giữa hai trường dữ liệu này.

---

## 🔍 Kỹ thuật Filter (Lọc dữ liệu)

Tôi thực hành lọc dữ liệu người dùng dựa trên các điều kiện cụ thể:

* **Lọc theo role:**
  ```python
  df[df["role"] == "user"]
  ```
* **Lọc những user có tên chứa chuỗi "Swagger"** (không phân biệt hoa thường và bỏ qua giá trị rỗng):
  ```python
  df[df["name"].str.contains("Swagger", case=False, na=False)]
  ```

> 📊 **Kết quả:** Hệ thống lọc ra được **91 Swagger users**.

---

## 🔀 Kỹ thuật Sort (Sắp xếp dữ liệu)

Tôi thực hành sắp xếp dữ liệu theo các chiều hướng khác nhau:
* Sắp xếp theo tên tăng dần: `df.sort_values("name")`
* Sắp xếp theo tên giảm dần: `df.sort_values("name", ascending=False)`
* Sắp xếp theo ID giảm dần và dùng `.head(10)` để lấy ra 10 bản ghi đầu tiên:
  ```python
  df.sort_values("id", ascending=False).head(10)
  ```

💡 **Bài học rút ra:** Hàm `sort_values()` chỉ thay đổi thứ tự hiển thị của các hàng (*rows*) trong DataFrame chứ không làm biến đổi bản chất dữ liệu. Ngoài ra, việc xếp ngược ID chỉ là một mẹo đơn giản để xem nhanh các bản ghi. Để xác định chính xác người dùng nào được tạo gần đây nhất, cấu trúc database chuẩn bắt buộc phải có trường mốc thời gian như `created_at`.

---

## 👥 Kỹ thuật GroupBy (Gom nhóm dữ liệu)

Khi bắt đầu gọi lệnh `df.groupby("role")`, kết quả trả về chỉ là một đối tượng `DataFrameGroupBy` ẩn. Để thu được số liệu thực tế, tôi kết hợp thêm các hàm tổng hợp (*aggregation*):

* **Đếm số lượng phần tử theo nhóm:**
  ```python
  df.groupby("role").size()
  # Kết quả trả về: user    93
  ```
* **Đếm số lượng theo cột định danh:**
  ```python
  df.groupby("role")["id"].count()
  ```
* **Chuyển đổi kết quả gom nhóm ngược lại thành một DataFrame hoàn chỉnh:**
  ```python
  df.groupby("role").size().reset_index(name="user_count")
  ```

---

## 💡 Bài học kinh nghiệm

Tôi bắt đầu nhận thấy sự tương đồng rất lớn và có tính hệ thống giữa ngôn ngữ truy vấn **SQL** và thư viện **Pandas**:

| Tính năng | Câu lệnh SQL (PostgreSQL) | Cú pháp tương đương trong Pandas |
| :--- | :--- | :--- |
| **Lọc dữ liệu** | `WHERE` | `df[condition]` |
| **Sắp xếp** | `ORDER BY` | `.sort_values()` |
| **Gom nhóm** | `GROUP BY` | `.groupby()` |
| **Đếm số lượng** | `COUNT()` | `.size()` hoặc `.count()` |

Mối liên hệ trực quan này giúp tôi tận dụng tốt những kiến thức backend đã học về PostgreSQL để tiếp thu thư viện Pandas nhanh chóng hơn.
```


---

## `docs/diary/2026-10-04-project-summary.md`

```markdown
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
```


---

## `docs/diary/2026-10-05-to-2026-10-11-retrospective-gap.md`

```markdown
# Retrospective Documentation Gap — 2026-10-05 → 2026-10-11

## Context

The development diary and mentor-facing weekly report were not maintained consistently during this period.

There is not enough reliable day-by-day evidence to reconstruct a precise daily history without introducing assumptions.

For that reason, this period is recorded as a **documentation gap** instead of being rewritten later as a normal weekly report.

---

## Reporting decision

I decided not to backfill a Week 24 report after the week had already passed.

The next actual mentor-facing report continues with:

```text
W25
2026-10-12 → 2026-10-18
```

The timeline therefore remains honest:

```text
previous submitted report
        ↓
W24 — not submitted
        ↓
W25 — next actual report
```

The missing report is acknowledged as a gap rather than being disguised as a report written on time.

---

## What can be confirmed

The project continued moving toward a more stable backend and database foundation around this period.

The surrounding verified milestones show continued work related to:

- FastAPI architecture;
- PostgreSQL;
- Alembic migrations;
- authentication and authorization;
- automated tests;
- database consistency;
- preparation for the transition toward data analysis.

These activities are intentionally **not assigned to specific dates inside this gap** because the original daily record is unavailable.

---

## Documentation lesson

Documentation is part of the engineering workflow.

When the original record is missing, the safer rule is:

```text
actual evidence
      >
a perfectly continuous-looking timeline
```

Going forward, the diary should be updated from verified commands, test results, commits, database state, and concrete learning outcomes.
```


---

## `docs/diary/2026-10-12-to-2026-10-18-current-progress.md`

```markdown
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
```


---

## `docs/diary/2026-10-18-project-summary.md`

```markdown
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
```


---

## `docs/diary/README.md`

```markdown
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
```


---

## `docs/mentor/DOCKER_AND_ANALYTICS_NOTES.md`

```markdown
# FastAPI User Management --- Docker, Testing và Analytics Notes

## 1. Trạng thái đã xác nhận

-   Docker Compose khởi động được API và PostgreSQL.
-   Firefox chạy được trong container API.
-   Playwright E2E: **9 passed** với `tests/e2e --browser firefox`.
-   API health endpoint trước đó trả về
    `{"status":"healthy","api":"running","database":"connected"}`.
-   PostgreSQL dùng named volume `postgres_data`. Không xóa volume khi
    chỉ restart/rebuild ứng dụng.

> `security_opt: - seccomp:unconfined` đã giúp Firefox tạo user
> namespace trong môi trường local. Cấu hình này làm giảm mức cô lập bảo
> mật; chỉ dùng cho development/E2E đáng tin cậy, không dùng làm cấu
> hình production.

## 2. Các lệnh Docker thường dùng

Chạy tại thư mục gốc dự án, nơi có `docker-compose.yml`:

``` bash
docker compose ps
docker compose up -d
docker compose up --build -d
docker compose logs -f api
docker compose logs -f postgres
curl http://localhost:8000/health
docker compose exec api sh
docker compose exec api id
docker compose down
```

`docker compose down` thông thường giữ named volume. Tránh
`docker compose down -v` nếu muốn giữ dữ liệu PostgreSQL.

## 3. Kiểm tra Firefox / Playwright

``` bash
docker compose exec api playwright --version
docker compose exec api python -c "from playwright.sync_api import sync_playwright; p=sync_playwright().start(); b=p.firefox.launch(headless=True); print('Firefox launch OK'); b.close(); p.stop()"
docker compose exec api sh -c 'unshare -Ur true; echo exit_code=$?'
```

Nếu Firefox báo `Firefox launch OK`, browser khởi chạy được. Nếu gặp
`CanCreateUserNamespace() clone() failure: EPERM`, kiểm tra Docker
security trước khi cài lại browser hoặc sửa code.

## 4. Chạy kiểm thử

### API tests

``` bash
docker compose exec -e PYTHONPATH=/app api pytest -q tests/api
```

### E2E tests với Firefox

``` bash
docker compose exec \
  -e PYTHONPATH=/app \
  api pytest -q tests/e2e \
  --browser firefox
```

### Toàn bộ API + E2E và coverage

``` bash
docker compose exec \
  -e PYTHONPATH=/app \
  api pytest -q \
  tests/api tests/e2e \
  --browser firefox \
  --cov=app \
  --cov-report=term-missing \
  --cov-report=html
```

Đọc số test pass/fail và coverage ở terminal. Báo cáo HTML được tạo tại
`htmlcov/`; với bind mount `.:/app`, thư mục này cũng xuất hiện trên máy
host.

Nếu test lỗi: 1. Đọc lỗi đầu tiên có ý nghĩa. 2. Nếu lỗi tại browser
fixture, kiểm tra Firefox launch độc lập. 3. Nếu lỗi DB, kiểm tra
`docker compose ps` và log PostgreSQL. 4. Nếu lỗi import, xác nhận có
`PYTHONPATH=/app`. 5. Chạy lại test liên quan trước, rồi chạy toàn bộ
suite.

## 5. Lộ trình NumPy, Pandas và Matplotlib

Thực hành trước trong notebook hoặc script riêng với dữ liệu dự án. Khi
đã hiểu kết quả, mới chuyển hàm ổn định vào `analytics/` và tích hợp API
nếu hữu ích.

### Bước 1 --- Pandas: khám phá dữ liệu

-   Dùng `head()`, `shape`, `columns`, `dtypes`, `info()`.
-   Kiểm tra thiếu dữ liệu bằng `isna().sum()`.
-   Lọc/sắp xếp bằng `loc`, boolean filtering và `sort_values()`.
-   Đếm bằng `value_counts()` và `groupby()`.

Câu hỏi: có bao nhiêu user; số user theo role/gender; bao nhiêu bài viết
mỗi user; ai có nhiều bài viết nhất?

### Bước 2 --- NumPy: thống kê

Thực hành `np.mean()`, `np.median()`, `np.min()`, `np.max()`, `np.std()`
trên tuổi hoặc số bài viết/user. Ghi rõ xử lý giá trị thiếu và việc
`np.std()` mặc định dùng population standard deviation (`ddof=0`);
`ddof=1` dùng sample standard deviation.

### Bước 3 --- Pandas: biến đổi và kết hợp

-   Tạo cột tuổi từ `birth_year`.
-   Phân nhóm tuổi bằng `pd.cut()` và ghi rõ biên nhóm.
-   Kết hợp users và post counts bằng `merge()`.
-   Tổng hợp theo role bằng `groupby()`.

Kiểm tra DataFrame rỗng, birth year thiếu, user không có bài viết và
user có nhiều bài viết.

### Bước 4 --- Matplotlib: trực quan hóa

-   Bar chart: user theo role/gender/age group.
-   Histogram: phân phối tuổi.
-   Bar chart: top users theo số bài viết.

Thêm tiêu đề, nhãn trục, đơn vị nếu có, và ghi chú cách xử lý dữ liệu
thiếu.

### Bước 5 --- Tổ chức và tích hợp

-   Giữ bài thử trong `notebook/` hoặc script học riêng.
-   Chuyển hàm đã hiểu và kiểm tra vào `analytics/`.
-   Giữ router mỏng; tránh đặt toàn bộ logic phân tích trong router.
-   Chỉ tạo endpoint analytics khi có mục đích cụ thể.

## 6. Nhật ký mỗi buổi học

``` text
Ngày:
Mục tiêu:
Dữ liệu sử dụng:
Câu hỏi cần trả lời:
Các hàm/thao tác đã học:
Kết quả:
Điều đã hiểu:
Lỗi gặp phải và cách xử lý:
Việc tiếp theo:
```

## 7. Quy trình làm việc gợi ý

1.  `docker compose up -d`
2.  `docker compose ps` và `curl http://localhost:8000/health`
3.  Thực hành Pandas/NumPy/Matplotlib.
4.  Chạy test liên quan sau khi sửa code.
5.  Lưu ghi chú và trạng thái test/coverage.
6.  Dừng bằng `docker compose down` nếu cần, không thêm `-v` khi cần giữ
    DB.
```


---

## `docs/mentor/development-notes.md`

```markdown
# Development Notes — FastAPI User Management

## 1. Mục đích

Tài liệu này ghi lại các lệnh thường dùng để chạy dự án FastAPI bằng Docker Compose, kiểm tra PostgreSQL, chạy test và xử lý lỗi Firefox khi chạy E2E test.

## 2. Khởi động dự án

Mở Terminal tại thư mục gốc `fastapi-user-management`.

Khởi động container:

`docker compose up -d`

Nếu vừa thay đổi Dockerfile hoặc cấu hình cần build lại:

`docker compose up --build -d`

Kiểm tra trạng thái container:

`docker compose ps`

Kiểm tra API:

`curl http://localhost:8000/health`

Kết quả mong đợi là API báo `healthy` và database báo `connected`.

## 3. Các lệnh Docker thường dùng

- `docker compose logs api` — xem log API.
- `docker compose logs -f api` — theo dõi log API liên tục.
- `docker compose logs postgres` — xem log PostgreSQL.
- `docker compose exec api sh` — mở shell trong container API.
- `docker compose exec api id` — xem user đang chạy trong container.
- `docker compose down` — dừng và xóa container/network của Compose.
- `docker compose up --build -d` — build image và chạy lại container.

**Lưu ý:** Không dùng `docker compose down -v` nếu không có chủ đích xóa volume. Volume `postgres_data` chứa dữ liệu PostgreSQL của dự án.

## 4. Chạy kiểm thử

Chạy toàn bộ API tests:

`docker compose exec -e PYTHONPATH=/app api pytest -q tests/api`

Chạy E2E tests với Firefox:

`docker compose exec -e PYTHONPATH=/app api pytest -q tests/e2e --browser firefox`

Chạy toàn bộ API và E2E tests kèm coverage:

`docker compose exec -e PYTHONPATH=/app api pytest -q tests/api tests/e2e --browser firefox --cov=app --cov-report=term-missing --cov-report=html`

- `-q`: output ngắn gọn.
- `--browser firefox`: chọn Firefox cho E2E.
- `--cov=app`: đo coverage cho package `app`.
- `--cov-report=term-missing`: hiển thị coverage và các dòng chưa được kiểm thử.
- `--cov-report=html`: tạo báo cáo HTML trong `htmlcov/`.

## 5. Lỗi Firefox sandbox trong Docker

### Hiện tượng

Firefox không khởi động khi chạy Playwright. Log có thông báo:

`Sandbox: CanCreateUserNamespace() clone() failure: EPERM`

Lệnh kiểm tra namespace trong container mặc định cũng trả về `Operation not permitted`.

### Nguyên nhân đã xác minh

Container mặc định bị chặn thao tác tạo user namespace. Khi thử một container tạm với `seccomp=unconfined`, lệnh `unshare -Ur true` chạy thành công. Sau khi cấu hình `seccomp:unconfined` cho service API trong môi trường phát triển, Firefox khởi động thành công và 9 E2E tests đã PASS.

### Cấu hình hiện tại

Service `api` dùng `security_opt` với `seccomp:unconfined`. Cấu hình này làm giảm mức bảo vệ seccomp của container, vì vậy chỉ nên dùng trong môi trường local development/E2E đã kiểm soát, không mặc định đưa vào production.

Container API hiện chạy bằng root vì cấu hình `user: "${UID}:${GID}"` đã được bỏ để kiểm tra và xử lý lỗi. Cần xem xét lại quyền chạy container và cách tách cấu hình E2E/dev khỏi cấu hình production trước khi triển khai.

### Kiểm tra Firefox

`docker compose exec api python -c "from playwright.sync_api import sync_playwright; p=sync_playwright().start(); b=p.firefox.launch(headless=True); print('Firefox launch OK'); b.close(); p.stop()"`

Kết quả đã quan sát: `Firefox launch OK`.

Kiểm tra namespace:

`docker compose exec api sh -c 'unshare -Ur true; echo exit_code=$?'`

Sau khi áp dụng cấu hình hiện tại, kết quả đã quan sát: `exit_code=0`.

## 6. Kết quả E2E gần nhất

Ngày ghi nhận: 2026-10-02

Lệnh chạy:

`docker compose exec -e PYTHONPATH=/app api pytest -q tests/e2e --browser firefox`

Kết quả: **9 passed in 26.45s**.

Đây là kết quả E2E; cần chạy lại toàn bộ API và E2E tests để xác nhận trạng thái hiện tại của toàn dự án.

## 7. Quy trình sau khi thay đổi code hoặc cấu hình

1. Xác định file đã thay đổi và lý do.
2. Nếu thay đổi Dockerfile hoặc cấu hình Compose, build/chạy lại container khi cần.
3. Kiểm tra `docker compose ps` và `/health`.
4. Chạy test phù hợp với phần vừa thay đổi.
5. Chạy toàn bộ test và coverage trước khi chốt một mốc hoàn thành.
6. Cập nhật tài liệu này nếu có lệnh, cấu hình hoặc cách xử lý lỗi mới.

## 8. Ghi chú học NumPy, Pandas và Matplotlib

Mục tiêu tiếp theo là học và thực hành phân tích dữ liệu dựa trên dữ liệu users và posts của chính dự án.

- **Pandas:** tạo DataFrame, lọc dữ liệu, `value_counts`, `groupby`, `merge`, xử lý giá trị thiếu.
- **NumPy:** tính mean, median, min, max và standard deviation.
- **Matplotlib:** trực quan hóa số lượng users, phân bố độ tuổi và số posts theo user/role.

Nên thực hành từng chủ đề trong notebook trước, sau đó chuyển các hàm đã hiểu rõ vào thư mục `analytics/` và tích hợp vào FastAPI khi có mục đích cụ thể.

Không cần tạo dữ liệu giả khổng lồ ngay từ đầu. Hãy bắt đầu với dữ liệu users/posts hiện có và kiểm tra các trường hợp DataFrame rỗng hoặc dữ liệu thiếu.

```


---

## `export_project.py`

```python
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "project_context.md"

# Những thư mục không cần đưa cho ChatGPT
EXCLUDED_DIRS = {
    ".git",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    "node_modules",
    "venv",
    ".venv",
    "env",
    ".env",
}

# Những file không cần đưa
EXCLUDED_FILES = {
    ".env",
    ".env.docker",
    "project_context.md",
}

# Chỉ lấy những loại file có ích cho việc đọc source
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

# Một số file không có extension
ALLOWED_FILENAMES = {
    "Dockerfile",
    "LICENSE",
    ".gitignore",
    ".dockerignore",
}


def should_include(path: Path) -> bool:
    # Loại thư mục
    if any(part in EXCLUDED_DIRS for part in path.parts):
        return False

    # Loại file cụ thể
    if path.name in EXCLUDED_FILES:
        return False

    # Loại binary Python
    if path.suffix.lower() in {".pyc", ".pyo", ".so"}:
        return False

    # Chỉ lấy file phù hợp
    if path.name in ALLOWED_FILENAMES:
        return True

    return path.suffix.lower() in ALLOWED_EXTENSIONS


def main():
    files = [
        p
        for p in ROOT.rglob("*")
        if p.is_file() and should_include(p)
    ]

    # Sắp xếp để project context có cấu trúc ổn định
    files.sort(key=lambda p: str(p.relative_to(ROOT)))

    with OUTPUT.open("w", encoding="utf-8") as out:

        # =========================================================
        # PROJECT CONTEXT
        # =========================================================

        out.write("# PROJECT CONTEXT\n\n")

        out.write(f"**Project root:** `{ROOT}`  \n")
        out.write(f"**Total included files:** {len(files)}\n\n")

        # =========================================================
        # 1. PROJECT STRUCTURE
        # =========================================================

        out.write("## Project Structure\n\n")

        for file in files:
            relative = file.relative_to(ROOT)
            out.write(f"- `{relative}`\n")

        # =========================================================
        # 2. FILE CONTENTS
        # =========================================================

        out.write("\n## File Contents\n")

        for file in files:
            relative = file.relative_to(ROOT)

            out.write("\n\n")
            out.write("---\n\n")
            out.write(f"## `{relative}`\n\n")

            try:
                content = file.read_text(encoding="utf-8")

                # Xác định ngôn ngữ cho Markdown code fence
                suffix = file.suffix.lower()

                language_map = {
                    ".py": "python",
                    ".md": "markdown",
                    ".txt": "text",
                    ".ini": "ini",
                    ".yml": "yaml",
                    ".yaml": "yaml",
                    ".sh": "bash",
                    ".dockerfile": "dockerfile",
                }

                language = language_map.get(suffix, "")

                # Các file không có extension
                if file.name == "Dockerfile":
                    language = "dockerfile"
                elif file.name in {".gitignore", ".dockerignore"}:
                    language = "gitignore"
                elif file.name == "LICENSE":
                    language = "text"

                out.write(f"```{language}\n")
                out.write(content)

                # Đảm bảo code fence không dính vào nội dung file
                if not content.endswith("\n"):
                    out.write("\n")

                out.write("```\n")

            except UnicodeDecodeError:
                out.write(
                    "[Could not decode this file as UTF-8]\n"
                )

            except Exception as e:
                out.write(
                    f"[Could not read file: {e}]\n"
                )

    print("Done!")
    print(f"Included files: {len(files)}")
    print(f"Output: {OUTPUT}")


if __name__ == "__main__":
    main()

```


---

## `htmlcov/.gitignore`

```gitignore
# Created by coverage.py
*
```


---

## `mentor-web/.gitignore`

```gitignore
# See https://help.github.com/articles/ignoring-files/ for more about ignoring files.

# dependencies
/node_modules
/.pnp
.pnp.*
.yarn/*
!.yarn/patches
!.yarn/plugins
!.yarn/releases
!.yarn/versions

# testing
/coverage

# next.js
/.next/
/out/

# production
/build

# misc
.DS_Store
*.pem

# debug
npm-debug.log*
yarn-debug.log*
yarn-error.log*
.pnpm-debug.log*

# env files (can opt-in for committing if needed)
.env*

# vercel
.vercel

# typescript
*.tsbuildinfo
next-env.d.ts

# Auto-generated mentor progress data
/src/data/progress.generated.json
```


---

## `mentor-web/AGENTS.md`

```markdown
<!-- BEGIN:nextjs-agent-rules -->

## This is NOT the Next.js you know

This version has breaking changes — APIs, conventions, and file structure may all differ from your training data. Read the relevant guide in `node_modules/next/dist/docs/` (resolved from this file's directory; in monorepos the `next` package may not be visible from the repo root) before writing any code. Heed deprecation notices.

This block is written and re-added by `next dev` — verify at `node_modules/next/dist/server/lib/generate-agent-files.js`. Removing it from a diff only re-creates the uncommitted change; committing it with your work keeps the tree clean.

<!-- END:nextjs-agent-rules -->
```


---

## `mentor-web/README.md`

```markdown
This is a [Next.js](https://nextjs.org) project bootstrapped with [`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/app/building-your-application/optimizing/fonts) to automatically optimize and load [Geist](https://vercel.com/font), a new font family for Vercel.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.
```


---

## `practice/pandas_lesson2.py`

```python
import pandas as pd

from sqlalchemy import select

from app.database import SessionLocal
from app.models.user import User


# ==========================================
# 1. LOAD USERS FROM DATABASE
# ==========================================

with SessionLocal() as db:
    users = db.scalars(
        select(User)
    ).all()


# ==========================================
# 2. CONVERT DATABASE DATA -> DATAFRAME
# ==========================================

data = []

for user in users:
    data.append(
        {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "role": user.role,
            "full_name": user.full_name,
        }
    )

df = pd.DataFrame(data)


# ==========================================
# 3. SELECT ONE COLUMN
# ==========================================

print("\n========== ONE COLUMN ==========")

print(df["name"])


# ==========================================
# 4. SELECT MULTIPLE COLUMNS
# ==========================================

print("\n========== MULTIPLE COLUMNS ==========")

print(
    df[
        ["name", "email", "role"]
    ]
)


print("\n========== NAME + FULL NAME ==========")

print(
    df[
        ["name", "full_name"]
    ]
)

# ==========================================
# 5. FILTER BY ROLE
# ==========================================

print("\n========== FILTER: ROLE = USER ==========")

users = df[df["role"] == "user"]

print(users)

# ==========================================
# 6. FILTER NAME CONTAINS "SWAGGER"
# ==========================================

print("\n========== FILTER: NAME CONTAINS SWAGGER ==========")

swagger_users = df[
    df["name"].str.contains("Swagger", case=False, na=False)
]

print(swagger_users)


# ==========================================
# 7. COUNT SWAGGER USERS
# ==========================================

print("\n========== NUMBER OF SWAGGER USERS ==========")

print(len(swagger_users))


# ==========================================
# 8. SORT BY NAME
# ==========================================

print("\n========== SORT BY NAME ==========")

sorted_by_name = df.sort_values(
    "name"
)

print(
    sorted_by_name[
        ["id", "name", "role"]
    ]
)


# ==========================================
# 9. SORT NAME DESCENDING
# ==========================================

print("\n========== SORT NAME DESCENDING ==========")

sorted_by_name_desc = df.sort_values(
    "name",
    ascending=False
)

print(
    sorted_by_name_desc[
        ["id", "name"]
    ]
)


# ==========================================
# 10. SORT BY ID DESCENDING
# ==========================================

print("\n========== SORT BY ID DESCENDING ==========")

latest_users = df.sort_values(
    "id",
    ascending=False
)

print(
    latest_users[
        ["id", "name", "email"]
    ].head(10)
)

# ==========================================
# 11. GROUP BY ROLE
# ==========================================

print("\n========== GROUP BY ROLE ==========")

grouped_by_role = df.groupby("role")

print(grouped_by_role)


# ==========================================
# 11. GROUP BY ROLE + SIZE
# ==========================================

print("\n========== USERS BY ROLE ==========")

users_by_role = (
    df.groupby("role")
      .size()
)

print(users_by_role)


# ==========================================
# 12. GROUP BY ROLE + COUNT ID
# ==========================================

print("\n========== COUNT USERS BY ROLE ==========")

user_count_by_role = (
    df.groupby("role")["id"]
      .count()
)

print(user_count_by_role)


# ==========================================
# 13. GROUP BY ROLE -> DATAFRAME
# ==========================================

print("\n========== USERS BY ROLE DATAFRAME ==========")

users_by_role_df = (
    df.groupby("role")
      .size()
      .reset_index(name="user_count")
)

print(users_by_role_df)


# ==========================================
# 11. USERS BY ROLE
# ==========================================

print("\n========== USERS BY ROLE ==========")

users_by_role = (
    df.groupby("role")
      .size()
)

print(users_by_role)


# ==========================================
# 12. COUNT ID BY ROLE
# ==========================================

print("\n========== COUNT ID BY ROLE ==========")

user_count_by_role = (
    df.groupby("role")["id"]
      .count()
)

print(user_count_by_role)


# ==========================================
# 13. USERS BY ROLE DATAFRAME
# ==========================================

print("\n========== USERS BY ROLE DATAFRAME ==========")

users_by_role_df = (
    df.groupby("role")
      .size()
      .reset_index(name="user_count")
)

print(users_by_role_df)


# ==========================================
# 14. VALUE COUNTS
# ==========================================

print("\n========== VALUE COUNTS ==========")

role_counts = df["role"].value_counts()

print(role_counts)


# ==========================================
# 15. GROUP BY FIRST LETTER OF NAME
# ==========================================

print("\n========== USERS BY FIRST LETTER ==========")

users_by_first_letter = (
    df["name"]
      .str[0]
      .value_counts()
      .sort_index()
)

print(users_by_first_letter)


# ==========================================
# 16. GROUP BY FIRST LETTER - CASE INSENSITIVE
# ==========================================

print("\n========== FIRST LETTER CASE INSENSITIVE ==========")

users_by_first_letter = (
    df["name"]
      .str[0]
      .str.upper()
      .value_counts()
      .sort_index()
)

print(users_by_first_letter)

# ==========================================
# 14. VALUE COUNTS
# ==========================================

print("\n========== VALUE COUNTS ==========")

role_counts = df["role"].value_counts()

print(role_counts)


# ==========================================
# 15. FIRST LETTER OF NAME
# ==========================================

print("\n========== USERS BY FIRST LETTER ==========")

users_by_first_letter = (
    df["name"]
      .str[0]
      .str.upper()
      .value_counts()
      .sort_index()
)

print(users_by_first_letter)


# ==========================================
# 16. CHECK MISSING VALUES
# ==========================================

print("\n========== MISSING VALUES ==========")

missing_values = df.isna().sum()

print(missing_values)


# ==========================================
# 17. SMALL PRACTICE
# ==========================================

print("\n========== SWAGGER USERS SORTED ==========")

swagger_users = df[
    df["name"].str.contains("Swagger", case=False, na=False)
]

swagger_users = swagger_users.sort_values("name")

print(swagger_users[["id", "name", "email"]])

print("\n========== SWAGGER NAME COUNTS ==========")

swagger_name_counts = swagger_users["name"].value_counts()

print(swagger_name_counts)

print("\n========== MISSING VALUES ==========")

print(swagger_users.isna().sum())
```


---

## `practice/pandas_numpy_lesson1.py`

```python
import numpy as np
import pandas as pd

from sqlalchemy import select

from app.database import SessionLocal
from app.models.user import User


# ==========================================
# 1. Lấy User từ PostgreSQL
# ==========================================

with SessionLocal() as db:
    users = db.scalars(
        select(User)
    ).all()


# ==========================================
# 2. SQLAlchemy objects -> Pandas DataFrame
# ==========================================

data = []

for user in users:
    data.append(
        {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "role": user.role,
            "full_name": user.full_name,
        }
    )

df = pd.DataFrame(data)


# ==========================================
# 3. Xem DataFrame
# ==========================================

print("\n========== DATAFRAME ==========")
print(df)


# ==========================================
# 4. Kích thước DataFrame
# ==========================================

print("\n========== SHAPE ==========")
print(df.shape)


# ==========================================
# 5. Tên các cột
# ==========================================

print("\n========== COLUMNS ==========")
print(df.columns)


# ==========================================
# 6. Kiểu dữ liệu
# ==========================================

print("\n========== DTYPES ==========")
print(df.dtypes)


# ==========================================
# 7. 5 dòng đầu
# ==========================================

print("\n========== HEAD ==========")
print(df.head())


# ==========================================
# 8. Thống kê cơ bản
# ==========================================

print("\n========== DESCRIBE ==========")
print(df.describe())


# ==========================================
# 9. Đếm User theo Role
# ==========================================

print("\n========== USERS BY ROLE ==========")
print(df["role"].value_counts())


# ==========================================
# 10. Kiểm tra dữ liệu thiếu
# ==========================================

print("\n========== MISSING VALUES ==========")
print(df.isna().sum())


# ==========================================
# 11. Lấy riêng cột name
# ==========================================

print("\n========== NAMES ==========")
print(df["name"])


# ==========================================
# 12. Lấy nhiều cột
# ==========================================

print("\n========== NAME + ROLE ==========")

print(
    df[
        [
            "name",
            "role",
        ]
    ]
)


# ==========================================
# 13. Chuyển User ID sang NumPy array
# ==========================================

user_ids = df["id"].to_numpy()

print("\n========== NUMPY USER IDS ==========")
print(user_ids)


# ==========================================
# 14. NumPy statistics
# ==========================================

print("\n========== NUMPY STATISTICS ==========")

print("Mean   :", np.mean(user_ids))
print("Median :", np.median(user_ids))
print("Min    :", np.min(user_ids))
print("Max    :", np.max(user_ids))
print("Sum    :", np.sum(user_ids))
print("Std    :", np.std(user_ids))
```


---

## `pytest.ini`

```ini
[pytest]
python_files = test_*.py
python_classes = Test*
python_functions = test_*

addopts =
    -v
    --tb=short
    --browser=firefox

testpaths =
    tests

markers =
    integration: tests that require a real PostgreSQL database

filterwarnings =
    ignore::DeprecationWarning:starlette.*
```


---

## `requirements-dev.txt`

```text
-r requirements.txt

pytest
pytest-cov
httpx
black
isort
flake8
mypy
alembic
pytest-playwright
pytest-html
playwright
```


---

## `requirements.txt`

```text
# --- Phân tích dữ liệu & Đồ họa ---
pandas==2.2.3
numpy==2.1.3
matplotlib==3.9.2

# --- Web Framework & Server ---
fastapi==0.116.1
uvicorn==0.35.0

# --- Cơ sở dữ liệu (ORM & Driver) ---
sqlalchemy==2.0.43
psycopg2-binary==2.9.10

# --- Xác thực dữ liệu (Validation) ---
pydantic==2.11.7
email-validator==2.2.0

# --- Bảo mật & Xác thực (Cập nhật pwdlib thay cho passlib lỗi thời) ---
pwdlib[argon2]==0.2.1
pydantic-settings==2.10.1
python-jose[cryptography]==3.5.0
python-multipart==0.0.32

# --- Tiện ích & HTTP Client ---
requests==2.32.4
python-dotenv==1.1.1
```


---

## `scripts/menu.sh`

```bash
#!/usr/bin/env bash


# ==========================================
# FastAPI User Management
# Docker Development Menu
# ==========================================


# ---------- Colors ----------

GREEN="\033[0;32m"
RED="\033[0;31m"
BLUE="\033[0;34m"
YELLOW="\033[1;33m"
CYAN="\033[0;36m"
NC="\033[0m"


# ---------- Project Config ----------

API_SERVICE="api"
DB_SERVICE="postgres"

DB_USER="admin"
DB_NAME="fastapi_db"



# ---------- Helper Functions ----------


pause()
{
    echo
    read -p "Press Enter to continue..."
}


check_docker()
{

    if ! command -v docker >/dev/null 2>&1
    then
        echo -e "${RED}Docker is not installed.${NC}"
        exit 1
    fi


    if ! docker compose version >/dev/null 2>&1
    then
        echo -e "${RED}Docker Compose is not available.${NC}"
        exit 1
    fi

}



success()
{
    echo -e "${GREEN}$1${NC}"
}


error()
{
    echo -e "${RED}$1${NC}"
}


info()
{
    echo -e "${BLUE}$1${NC}"
}



# ---------- Docker Actions ----------


start_project()
{
    info "Starting containers..."

    docker compose up --build -d

    success "Project started."
}



stop_project()
{
    info "Stopping containers..."

    docker compose down

    success "Containers stopped."
}



restart_project()
{
    info "Restarting containers..."

    docker compose down

    docker compose up --build -d

    success "Project restarted."
}



rebuild_project()
{
    info "Rebuilding containers..."

    docker compose build --no-cache

    docker compose up -d

    success "Rebuild completed."
}



view_logs()
{
    info "Showing logs..."

    docker compose logs -f
}



app_shell()
{

    info "Opening FastAPI container shell..."


    docker compose exec $API_SERVICE bash \
    || docker compose exec $API_SERVICE sh

}



postgres_shell()
{

    info "Opening PostgreSQL shell..."


    docker compose exec \
    $DB_SERVICE \
    psql \
    -U $DB_USER \
    -d $DB_NAME

}



# ---------- Database ----------


reset_database()
{

    echo -e "${YELLOW}"
    echo "WARNING:"
    echo "This will delete PostgreSQL volume."
    echo "All database data will be removed."
    echo -e "${NC}"


    read -p "Continue? (y/N): " answer


    if [[ "$answer" == "y" ]]
    then

        docker compose down -v

        docker compose up --build -d

        success "Database reset completed."

    else

        info "Cancelled."

    fi

}



alembic_upgrade()
{

    info "Running Alembic upgrade..."

    docker compose exec \
    $API_SERVICE \
    alembic upgrade head

}



alembic_revision()
{

    read -p "Migration message: " msg


    docker compose exec \
    $API_SERVICE \
    alembic revision --autogenerate -m "$msg"

}



alembic_downgrade()
{

    docker compose exec \
    $API_SERVICE \
    alembic downgrade -1

}



# ---------- Docker Utilities ----------


show_containers()
{
    docker compose ps
}



show_images()
{
    docker images
}



show_volumes()
{
    docker volume ls
}



show_networks()
{
    docker network ls
}



clean_docker()
{

    echo -e "${YELLOW}"
    echo "This removes unused Docker resources."
    echo -e "${NC}"


    read -p "Continue? (y/N): " answer


    if [[ "$answer" == "y" ]]
    then

        docker system prune -f

        success "Docker cleanup completed."

    else

        info "Cancelled."

    fi

}



build_only()
{

    docker compose build

    success "Build completed."

}



install_requirements()
{

    info "Installing Python requirements..."

    docker compose exec \
    $API_SERVICE \
    pip install -r requirements.txt


}



# ---------- Menu ----------


show_menu()
{

clear


echo -e "${CYAN}"
echo "========================================="
echo "     FastAPI User Management"
echo "     Docker Development Menu"
echo "========================================="
echo -e "${NC}"


echo " Docker"
echo "-----------------------------------------"
echo "1.  Start Containers"
echo "2.  Stop Containers"
echo "3.  Restart Containers"
echo "4.  Rebuild Containers"
echo


echo " Development"
echo "-----------------------------------------"
echo "5.  View Logs"
echo "6.  App Shell"
echo "7.  PostgreSQL Shell"
echo


echo " Database"
echo "-----------------------------------------"
echo "8.  Reset Database"
echo "9.  Alembic Upgrade"
echo "10. Create Migration"
echo "11. Alembic Downgrade"
echo


echo " Docker Utilities"
echo "-----------------------------------------"
echo "12. Show Containers"
echo "13. Show Images"
echo "14. Show Volumes"
echo "15. Show Networks"
echo "16. Clean Docker"
echo


echo " Others"
echo "-----------------------------------------"
echo "17. Build Only"
echo "18. Install Requirements"
echo


echo "0. Exit"

echo

}



# ---------- Main Loop ----------


check_docker


while true
do

show_menu


read -p "Choose option: " choice


case $choice in


1)
start_project
pause
;;


2)
stop_project
pause
;;


3)
restart_project
pause
;;


4)
rebuild_project
pause
;;


5)
view_logs
;;


6)
app_shell
;;


7)
postgres_shell
pause
;;


8)
reset_database
pause
;;


9)
alembic_upgrade
pause
;;


10)
alembic_revision
pause
;;


11)
alembic_downgrade
pause
;;


12)
show_containers
pause
;;


13)
show_images
pause
;;


14)
show_volumes
pause
;;


15)
show_networks
pause
;;


16)
clean_docker
pause
;;


17)
build_only
pause
;;


18)
install_requirements
pause
;;


0)
echo "Goodbye!"
exit 0
;;


*)
error "Invalid option."
pause
;;

esac


done
```


---

## `test_connection.py`

```python
from app.database import engine

try:
    connection = engine.connect()

    print("Connected PostgreSQL successfully!")

    connection.close()

except Exception as e:
    print(e)

# Tạo migration initial mới
# alembic revision --autogenerate -m "initial schema"
```


---

## `tests/__init__.py`

```python

```


---

## `tests/api/test_analytics.py`

```python
def login_user(
    client,
    email: str,
    password: str = "123456",
) -> None:
    response = client.post(
        "/auth/login",
        data={
            "username": email,
            "password": password,
        },
    )

    assert response.status_code == 200

    token = response.json()["access_token"]

    client.headers.update(
        {
            "Authorization": f"Bearer {token}",
        }
    )


def test_analytics_requires_authentication(
    client,
):
    response = client.get(
        "/analytics/users/summary"
    )

    assert response.status_code == 401


def test_analytics_rejects_normal_user(
    client,
):
    create_response = client.post(
        "/users/",
        json={
            "name": "analyticsuser",
            "email": "analytics-user@example.com",
            "password": "123456",
            "full_name": "Analytics User",
        },
    )

    assert create_response.status_code == 201

    login_user(
        client,
        "analytics-user@example.com",
    )

    response = client.get(
        "/analytics/users/summary"
    )

    assert response.status_code == 403
    assert (
        response.json()["detail"]
        == "Admin access required"
    )


def test_admin_can_get_user_analytics(
    auth_client,
):
    response = auth_client.get(
        "/analytics/users/summary"
    )

    assert response.status_code == 200

    body = response.json()

    assert body["status"] == "success"

    assert (
        body["message"]
        == "User analytics retrieved successfully"
    )

    data = body["data"]

    assert isinstance(
        data["total_users"],
        int,
    )

    assert data["total_users"] >= 1

    assert isinstance(
        data["users_by_role"],
        list,
    )

    admin_rows = [
        row
        for row in data["users_by_role"]
        if row["role"] == "admin"
    ]

    assert len(admin_rows) == 1
    assert admin_rows[0]["user_count"] >= 1
```


---

## `tests/api/test_auth.py`

```python
from jose import jwt

from app.core.config import settings
from app.core.security import create_access_token


def create_user(
    client,
    *,
    name: str,
    email: str,
    password: str = "123456",
):
    response = client.post(
        "/users/",
        json={
            "name": name,
            "email": email,
            "password": password,
            "full_name": name,
        },
    )

    assert response.status_code == 201

    return response.json()["data"]


def login(
    client,
    *,
    email: str,
    password: str = "123456",
):
    return client.post(
        "/auth/login",
        data={
            "username": email,
            "password": password,
        },
    )


def test_login_success(client):
    user = create_user(
        client,
        name="Login User",
        email="login@example.com",
    )

    response = login(
        client,
        email="login@example.com",
    )

    assert response.status_code == 200

    data = response.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"

    payload = jwt.decode(
        data["access_token"],
        settings.SECRET_KEY,
        algorithms=[
            settings.ALGORITHM,
        ],
    )

    assert payload["sub"] == str(
        user["id"]
    )


def test_login_wrong_password(client):
    create_user(
        client,
        name="Wrong Password",
        email="wrong-password@example.com",
    )

    response = login(
        client,
        email="wrong-password@example.com",
        password="wrong-password",
    )

    assert response.status_code == 401
    assert (
        response.json()["detail"]
        == "Invalid email or password"
    )


def test_login_unknown_user(client):
    response = login(
        client,
        email="notfound@example.com",
    )

    assert response.status_code == 401
    assert (
        response.json()["detail"]
        == "Invalid email or password"
    )


def test_auth_me_with_valid_token(client):
    user = create_user(
        client,
        name="Current User",
        email="current-user@example.com",
    )

    login_response = login(
        client,
        email="current-user@example.com",
    )

    assert (
        login_response.status_code
        == 200
    )

    token = login_response.json()[
        "access_token"
    ]

    response = client.get(
        "/auth/me",
        headers={
            "Authorization": (
                f"Bearer {token}"
            ),
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == user["id"]
    assert (
        data["email"]
        == "current-user@example.com"
    )


def test_auth_me_with_invalid_token(
    client,
):
    response = client.get(
        "/auth/me",
        headers={
            "Authorization": (
                "Bearer invalid-token"
            ),
        },
    )

    assert response.status_code == 401

    assert (
        response.json()["detail"]
        == "Could not validate credentials"
    )

    assert (
        response.headers[
            "www-authenticate"
        ]
        == "Bearer"
    )


def test_legacy_email_subject_token_still_works(
    client,
):
    user = create_user(
        client,
        name="Legacy User",
        email="legacy@example.com",
    )

    legacy_token = create_access_token(
        {
            "sub": "legacy@example.com",
        }
    )

    response = client.get(
        "/auth/me",
        headers={
            "Authorization": (
                f"Bearer {legacy_token}"
            ),
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == user["id"]
    assert (
        data["email"]
        == "legacy@example.com"
    )
```


---

## `tests/api/test_create_user.py`

```python
import uuid


def test_create_user(client):
    email = f"{uuid.uuid4()}@gmail.com"

    payload = {
        "name": "Test User",
        "full_name": "Test User",
        "email": email,
        "password": "12345678",
    }

    response = client.post(
        "/users/",
        json=payload,
    )

    assert response.status_code == 201

    body = response.json()

    assert body["status"] == "success"
    assert body["data"]["name"] == "Test User"
    assert body["data"]["full_name"] == "Test User"
    assert body["data"]["email"] == email
    assert body["data"]["role"] == "user"
    assert "password" not in body["data"]
```


---

## `tests/api/test_health.py`

```python
def test_health(client):

    response = client.get("/health")

    assert response.status_code == 200

    body = response.json()

    assert body["status"] == "healthy"
    assert body["database"] == "connected"
```


---

## `tests/api/test_lifecycle.py`

```python
def create_user(
    client,
    *,
    email: str,
):
    response = client.post(
        "/users/",
        json={
            "name": "Lifecycle User",
            "email": email,
            "password": "123456",
            "full_name": "Lifecycle User",
        },
    )

    assert response.status_code == 201

    return response.json()["data"]


def login(
    client,
    *,
    email: str,
):
    return client.post(
        "/auth/login",
        data={
            "username": email,
            "password": "123456",
        },
    )


def test_new_user_has_lifecycle_fields(
    client,
):
    user = create_user(
        client,
        email="lifecycle-fields@example.com",
    )

    assert user["is_active"] is True
    assert user["created_at"] is not None
    assert user["updated_at"] is not None
    assert user["last_login_at"] is None


def test_login_updates_last_login_at(
    client,
):
    email = "last-login@example.com"

    create_user(
        client,
        email=email,
    )

    login_response = login(
        client,
        email=email,
    )

    assert login_response.status_code == 200

    token = login_response.json()[
        "access_token"
    ]

    response = client.get(
        "/auth/me",
        headers={
            "Authorization": (
                f"Bearer {token}"
            ),
        },
    )

    assert response.status_code == 200

    assert (
        response.json()["last_login_at"]
        is not None
    )


def test_inactive_user_cannot_login(
    client,
    admin_client,
):
    email = "inactive-login@example.com"

    user = create_user(
        client,
        email=email,
    )

    deactivate_response = admin_client.patch(
        f"/users/{user['id']}",
        json={
            "is_active": False,
        },
    )

    assert (
        deactivate_response.status_code
        == 200
    )

    login_response = login(
        client,
        email=email,
    )

    assert (
        login_response.status_code
        == 401
    )


def test_existing_token_rejected_after_deactivation(
    client,
    admin_client,
):
    email = "inactive-token@example.com"

    user = create_user(
        client,
        email=email,
    )

    login_response = login(
        client,
        email=email,
    )

    assert login_response.status_code == 200

    token = login_response.json()[
        "access_token"
    ]

    deactivate_response = admin_client.patch(
        f"/users/{user['id']}",
        json={
            "is_active": False,
        },
    )

    assert (
        deactivate_response.status_code
        == 200
    )

    response = client.get(
        "/auth/me",
        headers={
            "Authorization": (
                f"Bearer {token}"
            ),
        },
    )

    assert response.status_code == 403

    assert (
        response.json()["detail"]
        == "Inactive user"
    )


def test_post_default_status_is_published(
    user_client,
):
    response = user_client.post(
        "/posts/",
        json={
            "title": "Published Post",
            "content": "Content",
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["status"] == "published"
    assert data["created_at"] is not None
    assert data["updated_at"] is not None


def test_post_status_can_be_changed(
    user_client,
):
    create_response = user_client.post(
        "/posts/",
        json={
            "title": "Lifecycle Post",
            "content": "Lifecycle content",
        },
    )

    assert (
        create_response.status_code
        == 201
    )

    post_id = create_response.json()["id"]

    response = user_client.patch(
        f"/posts/{post_id}",
        json={
            "status": "archived",
        },
    )

    assert response.status_code == 200

    assert (
        response.json()["status"]
        == "archived"
    )


def test_invalid_post_status_rejected(
    user_client,
):
    response = user_client.post(
        "/posts/",
        json={
            "title": "Invalid Status",
            "content": "Content",
            "status": "deleted",
        },
    )

    assert response.status_code == 422
```


---

## `tests/api/test_openapi_contract.py`

```python
def get_openapi(client):
    response = client.get(
        "/openapi.json"
    )

    assert response.status_code == 200

    return response.json()


def resolve_schema(
    openapi: dict,
    schema: dict,
) -> dict:
    reference = schema.get("$ref")

    if reference is None:
        return schema

    prefix = "#/components/schemas/"

    assert reference.startswith(
        prefix
    )

    schema_name = reference.removeprefix(
        prefix
    )

    return openapi[
        "components"
    ][
        "schemas"
    ][
        schema_name
    ]


def extract_non_null_schema(
    schema: dict,
) -> dict:
    alternatives = schema.get(
        "anyOf"
    )

    if alternatives is None:
        return schema

    for alternative in alternatives:
        if (
            alternative.get("type")
            != "null"
        ):
            return alternative

    raise AssertionError(
        "No non-null schema found"
    )


def test_users_list_openapi_is_typed(
    client,
):
    openapi = get_openapi(
        client
    )

    response_schema = (
        openapi[
            "paths"
        ][
            "/users/"
        ][
            "get"
        ][
            "responses"
        ][
            "200"
        ][
            "content"
        ][
            "application/json"
        ][
            "schema"
        ]
    )

    api_response_schema = (
        resolve_schema(
            openapi,
            response_schema,
        )
    )

    data_schema = (
        api_response_schema[
            "properties"
        ][
            "data"
        ]
    )

    data_schema = (
        extract_non_null_schema(
            data_schema
        )
    )

    assert (
        data_schema["type"]
        == "array"
    )

    item_schema = (
        data_schema[
            "items"
        ]
    )

    assert (
        item_schema["$ref"]
        .endswith(
            "/UserResponse"
        )
    )


def test_user_detail_openapi_is_typed(
    client,
):
    openapi = get_openapi(
        client
    )

    response_schema = (
        openapi[
            "paths"
        ][
            "/users/{user_id}"
        ][
            "get"
        ][
            "responses"
        ][
            "200"
        ][
            "content"
        ][
            "application/json"
        ][
            "schema"
        ]
    )

    api_response_schema = (
        resolve_schema(
            openapi,
            response_schema,
        )
    )

    data_schema = (
        api_response_schema[
            "properties"
        ][
            "data"
        ]
    )

    data_schema = (
        extract_non_null_schema(
            data_schema
        )
    )

    assert (
        data_schema["$ref"]
        .endswith(
            "/UserResponse"
        )
    )


def test_users_pagination_headers_are_documented(
    client,
):
    openapi = get_openapi(
        client
    )

    headers = (
        openapi[
            "paths"
        ][
            "/users/"
        ][
            "get"
        ][
            "responses"
        ][
            "200"
        ][
            "headers"
        ]
    )

    assert (
        "X-Total-Count"
        in headers
    )

    assert (
        "X-Limit"
        in headers
    )

    assert (
        "X-Offset"
        in headers
    )

    assert (
        "X-Has-More"
        in headers
    )


def test_posts_pagination_headers_are_documented(
    client,
):
    openapi = get_openapi(
        client
    )

    headers = (
        openapi[
            "paths"
        ][
            "/posts/"
        ][
            "get"
        ][
            "responses"
        ][
            "200"
        ][
            "headers"
        ]
    )

    assert (
        "X-Total-Count"
        in headers
    )

    assert (
        "X-Limit"
        in headers
    )

    assert (
        "X-Offset"
        in headers
    )

    assert (
        "X-Has-More"
        in headers
    )
```


---

## `tests/api/test_pagination.py`

```python
def create_user(
    client,
    *,
    name: str,
    email: str,
):
    response = client.post(
        "/users/",
        json={
            "name": name,
            "email": email,
            "password": "123456",
            "full_name": name,
        },
    )

    assert response.status_code == 201

    return response.json()["data"]


def create_post(
    client,
    *,
    title: str,
):
    response = client.post(
        "/posts/",
        json={
            "title": title,
            "content": "Pagination content",
        },
    )

    assert response.status_code == 201

    return response.json()


def test_users_pagination_headers(
    admin_client,
):
    for index in range(3):
        create_user(
            admin_client,
            name=f"Page User {index}",
            email=(
                f"page-user-{index}"
                "@example.com"
            ),
        )

    response = admin_client.get(
        "/users/",
        params={
            "search": "Page User",
            "limit": 2,
            "offset": 1,
        },
    )

    assert response.status_code == 200

    body = response.json()

    assert (
        body["status"]
        == "success"
    )

    assert len(
        body["data"]
    ) == 2

    assert (
        response.headers[
            "X-Total-Count"
        ]
        == "3"
    )

    assert (
        response.headers[
            "X-Limit"
        ]
        == "2"
    )

    assert (
        response.headers[
            "X-Offset"
        ]
        == "1"
    )

    assert (
        response.headers[
            "X-Has-More"
        ]
        == "false"
    )


def test_posts_pagination_headers(
    user_client,
):
    for index in range(3):
        create_post(
            user_client,
            title=(
                f"Pagination Post {index}"
            ),
        )

    response = user_client.get(
        "/posts/",
        params={
            "search":
                "Pagination Post",
            "limit": 2,
            "offset": 0,
        },
    )

    assert response.status_code == 200

    body = response.json()

    assert len(body) == 2

    assert (
        response.headers[
            "X-Total-Count"
        ]
        == "3"
    )

    assert (
        response.headers[
            "X-Limit"
        ]
        == "2"
    )

    assert (
        response.headers[
            "X-Offset"
        ]
        == "0"
    )

    assert (
        response.headers[
            "X-Has-More"
        ]
        == "true"
    )
```


---

## `tests/api/test_posts.py`

```python
def create_user(client, name, email):
    response = client.post(
        "/users/",
        json={
            "name": name,
            "email": email,
            "password": "123456",
            "full_name": name,
        },
    )
    assert response.status_code == 201
    return response.json()["data"]


def login(client, email):
    response = client.post(
        "/auth/login",
        data={
            "username": email,
            "password": "123456",
        },
    )
    assert response.status_code == 200

    token = response.json()["access_token"]
    client.headers.update(
        {"Authorization": f"Bearer {token}"}
    )


def create_post(client, title="Test Post", content="Test content"):
    response = client.post(
        "/posts/",
        json={
            "title": title,
            "content": content,
        },
    )
    assert response.status_code == 201
    return response.json()


def test_create_post(client):
    create_user(
        client,
        "Post User",
        "postuser@example.com",
    )
    login(client, "postuser@example.com")

    response = create_post(client)

    assert response["id"] > 0
    assert response["title"] == "Test Post"
    assert response["content"] == "Test content"
    assert response["user_id"] > 0
    assert response["owner"]["email"] == "postuser@example.com"


def test_create_post_unauthorized(client):
    response = client.post(
        "/posts/",
        json={
            "title": "Unauthorized Post",
            "content": "Content",
        },
    )

    assert response.status_code == 401


def test_get_posts(client):
    create_user(
        client,
        "Post User",
        "getposts@example.com",
    )
    login(client, "getposts@example.com")

    create_post(client, "Post 1", "Content 1")
    create_post(client, "Post 2", "Content 2")

    response = client.get("/posts/")

    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, list)
    assert len(data) == 2

    titles = {post["title"] for post in data}

    assert titles == {"Post 1", "Post 2"}


def test_get_posts_search(client):
    create_user(
        client,
        "Search User",
        "search@example.com",
    )
    login(client, "search@example.com")

    create_post(client, "Python FastAPI", "Backend")
    create_post(client, "SQLAlchemy", "Database")

    response = client.get(
        "/posts/",
        params={"search": "FastAPI"},
    )

    assert response.status_code == 200
    data = response.json()

    assert len(data) == 1
    assert data[0]["title"] == "Python FastAPI"


def test_get_my_posts(client):
    create_user(
        client,
        "My Post User",
        "myposts@example.com",
    )
    login(client, "myposts@example.com")

    create_post(client, "My Post", "My content")

    response = client.get("/posts/me")

    assert response.status_code == 200
    data = response.json()

    assert len(data) == 1
    assert data[0]["title"] == "My Post"


def test_get_post(client):
    create_user(
        client,
        "Get User",
        "getpost@example.com",
    )
    login(client, "getpost@example.com")

    post = create_post(client)

    response = client.get(f"/posts/{post['id']}")

    assert response.status_code == 200
    data = response.json()

    assert data["id"] == post["id"]
    assert data["title"] == "Test Post"


def test_get_post_not_found(client):
    response = client.get("/posts/999999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Post not found"


def test_update_post(client):
    create_user(
        client,
        "Update User",
        "update@example.com",
    )
    login(client, "update@example.com")

    post = create_post(client)

    response = client.put(
        f"/posts/{post['id']}",
        json={
            "title": "Updated Title",
            "content": "Updated content",
        },
    )

    assert response.status_code == 200
    data = response.json()

    assert data["title"] == "Updated Title"
    assert data["content"] == "Updated content"


def test_patch_post(client):
    create_user(
        client,
        "Patch User",
        "patch@example.com",
    )
    login(client, "patch@example.com")

    post = create_post(client)

    response = client.patch(
        f"/posts/{post['id']}",
        json={
            "title": "Patched Title",
        },
    )

    assert response.status_code == 200
    data = response.json()

    assert data["title"] == "Patched Title"
    assert data["content"] == "Test content"


def test_delete_post(client):
    create_user(
        client,
        "Delete User",
        "delete@example.com",
    )
    login(client, "delete@example.com")

    post = create_post(client)

    response = client.delete(
        f"/posts/{post['id']}"
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Post deleted successfully"

    response = client.get(
        f"/posts/{post['id']}"
    )

    assert response.status_code == 404


def test_post_ownership_forbidden(client):
    create_user(
        client,
        "Owner User",
        "owner@example.com",
    )
    login(client, "owner@example.com")

    post = create_post(client)

    # Tạo user thứ hai
    client.headers.pop("Authorization", None)

    create_user(
        client,
        "Other User",
        "other@example.com",
    )
    login(client, "other@example.com")

    response = client.put(
        f"/posts/{post['id']}",
        json={
            "title": "Hacked",
            "content": "Hacked",
        },
    )

    assert response.status_code == 403
    assert response.json()["detail"] == "You do not own this post"


def test_create_post_invalid_title(client):
    create_user(
        client,
        "Validation User",
        "validation@example.com",
    )
    login(client, "validation@example.com")

    response = client.post(
        "/posts/",
        json={
            "title": "A",
            "content": "Content",
        },
    )

    assert response.status_code == 422

```


---

## `tests/api/test_user_filters.py`

```python
def create_user(
    client,
    *,
    name: str,
    email: str,
):
    response = client.post(
        "/users/",
        json={
            "name": name,
            "email": email,
            "password": "123456",
            "full_name": name,
        },
    )

    assert response.status_code == 201
    return response.json()["data"]


def test_filter_users_by_user_role(admin_client):
    create_user(
        admin_client,
        name="Alpha User",
        email="alpha-filter@example.com",
    )
    create_user(
        admin_client,
        name="Beta User",
        email="beta-filter@example.com",
    )

    response = admin_client.get(
        "/users/",
        params={"role": "user"},
    )

    assert response.status_code == 200

    body = response.json()

    assert len(body["data"]) == 2
    assert all(
        user["role"] == "user"
        for user in body["data"]
    )
    assert response.headers["X-Total-Count"] == "2"


def test_filter_users_by_admin_role(admin_client):
    create_user(
        admin_client,
        name="Normal User",
        email="normal-filter@example.com",
    )

    response = admin_client.get(
        "/users/",
        params={"role": "admin"},
    )

    assert response.status_code == 200

    body = response.json()

    assert len(body["data"]) == 1
    assert all(
        user["role"] == "admin"
        for user in body["data"]
    )
    assert response.headers["X-Total-Count"] == "1"


def test_role_filter_combines_with_search(admin_client):
    create_user(
        admin_client,
        name="Alpha User",
        email="alpha-search@example.com",
    )

    response = admin_client.get(
        "/users/",
        params={
            "role": "admin",
            "search": "Alpha",
        },
    )

    assert response.status_code == 200

    body = response.json()

    assert body["data"] == []
    assert response.headers["X-Total-Count"] == "0"


def test_invalid_role_returns_422(admin_client):
    response = admin_client.get(
        "/users/",
        params={"role": "superadmin"},
    )

    assert response.status_code == 422
```


---

## `tests/api/test_users.py`

```python
def test_get_users(admin_client):
    response = admin_client.get(
        "/users/"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "success"
    assert isinstance(
        data["data"],
        list,
    )


def test_get_users_unauthorized(client):
    response = client.get(
        "/users/"
    )

    assert response.status_code == 401


def test_get_users_forbidden_for_normal_user(
    user_client,
):
    response = user_client.get(
        "/users/"
    )

    assert response.status_code == 403

    assert (
        response.json()["detail"]
        == "Admin access required"
    )


def test_create_user(client):
    response = client.post(
        "/users/",
        json={
            "name": "testuser",
            "email": "testuser@example.com",
            "password": "123456",
            "full_name": "Test User",
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["status"] == "success"

    assert (
        data["data"]["name"]
        == "testuser"
    )

    assert (
        data["data"]["email"]
        == "testuser@example.com"
    )

    assert (
        data["data"]["role"]
        == "user"
    )

    assert (
        data["data"]["full_name"]
        == "Test User"
    )

    assert (
        "password"
        not in data["data"]
    )


def test_create_duplicate_email(client):
    payload = {
        "name": "testuser",
        "email": "duplicate@example.com",
        "password": "123456",
        "full_name": "Test User",
    }

    first_response = client.post(
        "/users/",
        json=payload,
    )

    assert (
        first_response.status_code
        == 201
    )

    second_response = client.post(
        "/users/",
        json=payload,
    )

    assert (
        second_response.status_code
        == 409
    )

    assert (
        second_response.json()["detail"]
        == "Email already exists"
    )


def test_create_user_invalid_password(
    client,
):
    response = client.post(
        "/users/",
        json={
            "name": "testuser",
            "email": "invalid@example.com",
            "password": "123",
            "full_name": "Invalid User",
        },
    )

    assert response.status_code == 422


def test_update_user_rejects_invalid_role(
    admin_client,
):
    create_response = admin_client.post(
        "/users/",
        json={
            "name": "Role User",
            "email": "role-user@example.com",
            "password": "123456",
            "full_name": "Role User",
        },
    )

    assert (
        create_response.status_code
        == 201
    )

    user_id = create_response.json()[
        "data"
    ]["id"]

    response = admin_client.put(
        f"/users/{user_id}",
        json={
            "name": "Role User",
            "email": "role-user@example.com",
            "role": "superadmin",
            "full_name": "Role User",
        },
    )

    assert response.status_code == 422


def test_patch_user_rejects_invalid_role(
    admin_client,
):
    create_response = admin_client.post(
        "/users/",
        json={
            "name": "Patch Role User",
            "email": "patch-role@example.com",
            "password": "123456",
            "full_name": "Patch Role User",
        },
    )

    assert (
        create_response.status_code
        == 201
    )

    user_id = create_response.json()[
        "data"
    ]["id"]

    response = admin_client.patch(
        f"/users/{user_id}",
        json={
            "role": "root",
        },
    )

    assert response.status_code == 422
```


---

## `tests/api/test_validation.py`

```python
def create_user(
    client,
    *,
    name: str,
    email: str,
):
    response = client.post(
        "/users/",
        json={
            "name": name,
            "email": email,
            "password": "123456",
            "full_name": name,
        },
    )

    assert response.status_code == 201

    return response.json()["data"]


def test_create_user_rejects_whitespace_name(
    client,
):
    response = client.post(
        "/users/",
        json={
            "name": "   ",
            "email": "whitespace@example.com",
            "password": "123456",
            "full_name": "Whitespace User",
        },
    )

    assert response.status_code == 422


def test_create_user_rejects_extra_role(
    client,
):
    response = client.post(
        "/users/",
        json={
            "name": "Normal User",
            "email": "extra-role@example.com",
            "password": "123456",
            "full_name": "Normal User",
            "role": "admin",
        },
    )

    assert response.status_code == 422


def test_patch_user_rejects_null_name(
    admin_client,
):
    user = create_user(
        admin_client,
        name="Patch User",
        email="patch-null@example.com",
    )

    response = admin_client.patch(
        f"/users/{user['id']}",
        json={
            "name": None,
        },
    )

    assert response.status_code == 422


def test_create_post_rejects_whitespace_title(
    user_client,
):
    response = user_client.post(
        "/posts/",
        json={
            "title": "   ",
            "content": "Content",
        },
    )

    assert response.status_code == 422


def test_patch_post_rejects_null_title(
    user_client,
):
    create_response = user_client.post(
        "/posts/",
        json={
            "title": "Valid Post",
            "content": "Content",
        },
    )

    assert (
        create_response.status_code
        == 201
    )

    post_id = create_response.json()["id"]

    response = user_client.patch(
        f"/posts/{post_id}",
        json={
            "title": None,
        },
    )

    assert response.status_code == 422


def test_create_post_rejects_extra_user_id(
    user_client,
):
    response = user_client.post(
        "/posts/",
        json={
            "title": "Secure Post",
            "content": "Content",
            "user_id": 999999,
        },
    )

    assert response.status_code == 422
```


---

## `tests/conftest.py`

```python
from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import StaticPool

from app.core.security import hash_password
from app.database import Base
from app.dependencies import get_db
from app.main import app
from app.models import User


SQLALCHEMY_DATABASE_URL = "sqlite://"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={
        "check_same_thread": False,
    },
    poolclass=StaticPool,
)


TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


@pytest.fixture(scope="function")
def db_session() -> Generator[
    Session,
    None,
    None,
]:
    Base.metadata.create_all(
        bind=engine
    )

    db = TestingSessionLocal()

    try:
        yield db
    finally:
        db.close()

        Base.metadata.drop_all(
            bind=engine
        )


@pytest.fixture(scope="function")
def client(
    db_session: Session,
) -> Generator[
    TestClient,
    None,
    None,
]:
    def override_get_db():
        yield db_session

    app.dependency_overrides[
        get_db
    ] = override_get_db

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()


def login_client(
    client: TestClient,
    email: str,
    password: str,
) -> None:
    response = client.post(
        "/auth/login",
        data={
            "username": email,
            "password": password,
        },
    )

    assert response.status_code == 200

    token = response.json()[
        "access_token"
    ]

    client.headers.update(
        {
            "Authorization": (
                f"Bearer {token}"
            ),
        }
    )


@pytest.fixture(scope="function")
def user_client(
    client: TestClient,
) -> Generator[
    TestClient,
    None,
    None,
]:
    response = client.post(
        "/users/",
        json={
            "name": "testuser",
            "email": "testuser@example.com",
            "password": "123456",
            "full_name": "Test User",
        },
    )

    assert response.status_code == 201

    login_client(
        client,
        email="testuser@example.com",
        password="123456",
    )

    yield client

    client.headers.pop(
        "Authorization",
        None,
    )


@pytest.fixture(scope="function")
def admin_client(
    client: TestClient,
    db_session: Session,
) -> Generator[
    TestClient,
    None,
    None,
]:
    admin = User(
        name="testadmin",
        email="testadmin@example.com",
        role="admin",
        password=hash_password(
            "123456"
        ),
        full_name="Test Admin",
    )

    db_session.add(admin)
    db_session.commit()

    login_client(
        client,
        email="testadmin@example.com",
        password="123456",
    )

    yield client

    client.headers.pop(
        "Authorization",
        None,
    )


@pytest.fixture(scope="function")
def auth_client(
    admin_client: TestClient,
) -> TestClient:
    """
    Backward-compatible alias.

    Existing tests currently expect auth_client
    to be an authenticated admin client.

    New tests should prefer the explicit fixtures:
    - user_client
    - admin_client
    """
    return admin_client
```


---

## `tests/e2e/__init__.py`

```python

```


---

## `tests/e2e/test_swagger_auth.py`

```python
import uuid

from playwright.sync_api import expect

from tests.e2e.utils import (
    click_execute,
    click_try_it_out,
    fill_form_field,
    get_post_endpoint,
    open_swagger,
    screenshot,
)


def test_swagger_login(page):
    # ---------------------------------------------------------
    # 1. Create a test user through API
    # ---------------------------------------------------------
    email = f"swagger-login-{uuid.uuid4().hex[:8]}@example.com"
    password = "123456"

    create_response = page.request.post(
        "http://api:8000/users/",
        data={
            "name": "Swagger Login User",
            "email": email,
            "password": password,
            "full_name": "Swagger Login User",
        },
    )

    assert create_response.status == 201

    # ---------------------------------------------------------
    # 2. Open Swagger UI
    # ---------------------------------------------------------
    open_swagger(page)

    # ---------------------------------------------------------
    # 3. Open POST /auth/login
    # ---------------------------------------------------------
    endpoint = get_post_endpoint(
        page,
        "/auth/login",
    )

    endpoint.click()

    # ---------------------------------------------------------
    # 4. Enable Try it out
    # ---------------------------------------------------------
    click_try_it_out(endpoint)

    # ---------------------------------------------------------
    # 5. Fill OAuth2PasswordRequestForm
    # ---------------------------------------------------------
    fill_form_field(
        endpoint,
        "username",
        email,
    )

    fill_form_field(
        endpoint,
        "password",
        password,
    )

    # ---------------------------------------------------------
    # 6. Execute login
    # ---------------------------------------------------------
    click_execute(endpoint)

    # ---------------------------------------------------------
    # 7. Verify response
    # ---------------------------------------------------------
    response_section = endpoint.locator(
        ".responses-inner"
    )

    expect(response_section).to_contain_text("200")
    expect(response_section).to_contain_text(
        "access_token"
    )
    expect(response_section).to_contain_text(
        "bearer"
    )

    # ---------------------------------------------------------
    # 8. Capture evidence
    # ---------------------------------------------------------
    screenshot(
        page,
        "swagger/04_login_success.png",
    )
```


---

## `tests/e2e/test_swagger_authorize.py`

```python
import re
import uuid

from playwright.sync_api import expect

from tests.e2e.utils import (
    open_swagger,
    screenshot,
)


def test_swagger_authorize(page):
    # ---------------------------------------------------------
    # 1. Create a test user through API
    # ---------------------------------------------------------
    email = (
        f"swagger-authorize-{uuid.uuid4().hex[:8]}"
        "@example.com"
    )
    password = "123456"

    create_response = page.request.post(
        "http://api:8000/users/",
        data={
            "name": "Swagger Authorize User",
            "email": email,
            "password": password,
            "full_name": "Swagger Authorize User",
        },
    )

    assert create_response.status == 201, (
        f"Failed to create test user: "
        f"{create_response.status} "
        f"{create_response.text()}"
    )

    # ---------------------------------------------------------
    # 2. Open Swagger UI
    # ---------------------------------------------------------
    open_swagger(page)

    # ---------------------------------------------------------
    # 3. Open Authorize dialog
    # ---------------------------------------------------------
    authorize_button = page.get_by_role(
        "button",
        name="Authorize",
    )

    expect(authorize_button).to_be_visible()
    authorize_button.click()

    dialog = page.locator(".modal-ux")

    expect(dialog).to_be_visible()

    # ---------------------------------------------------------
    # 4. Fill OAuth2 credentials
    # ---------------------------------------------------------
    username_input = dialog.get_by_role(
        "textbox",
        name="username:",
    )

    password_input = dialog.get_by_role(
        "textbox",
        name="password:",
    )

    expect(username_input).to_be_visible()
    expect(password_input).to_be_visible()

    username_input.fill(email)
    password_input.fill(password)

    # ---------------------------------------------------------
    # 5. Authorize
    # ---------------------------------------------------------
    #
    # Swagger UI uses:
    # aria-label="Apply given OAuth2 credentials"
    #
    # The visible text is "Authorize", but the accessible
    # role/name used by Playwright is "Apply given OAuth2 credentials".
    #
    authorize_dialog_button = dialog.get_by_role(
        "button",
        name="Apply given OAuth2 credentials",
    )

    expect(authorize_dialog_button).to_be_visible()
    expect(authorize_dialog_button).to_be_enabled()

    authorize_dialog_button.click()

    # ---------------------------------------------------------
    # 6. Verify authorization
    # ---------------------------------------------------------
    authorization_button = page.get_by_role(
        "button",
        name="authorization button unlocked",
    ).first

    expect(authorization_button).to_be_visible()

    # ---------------------------------------------------------
    # 7. Capture evidence
    # ---------------------------------------------------------
    screenshot(
        page,
        "swagger/05_authorize_success.png",
    )
```


---

## `tests/e2e/test_swagger_home.py`

```python
from tests.e2e.utils import open_swagger, screenshot


def test_swagger_home(page):
    open_swagger(page)

    screenshot(
        page,
        "swagger/01_home.png",
    )


def test_swagger_openapi(page):
    response = page.request.get(
        "http://api:8000/openapi.json"
    )

    assert response.status == 200

    data = response.json()

    assert data["info"]["title"] == (
        "FastAPI User Management"
    )

    assert "/health" in data["paths"]
    assert "/auth/login" in data["paths"]
    assert "/users/" in data["paths"]
    assert "/posts/" in data["paths"]

    open_swagger(page)

    screenshot(
        page,
        "swagger/02_endpoints.png",
    )
```


---

## `tests/e2e/test_swagger_posts.py`

```python
import uuid

from playwright.sync_api import expect

from tests.e2e.utils import (
    click_execute,
    click_try_it_out,
    fill_request_body,
    get_post_endpoint,
    open_swagger,
    screenshot,
)


def create_test_user(page, prefix: str) -> tuple[str, str]:
    email = (
        f"swagger-{prefix}-{uuid.uuid4().hex[:8]}"
        "@example.com"
    )
    password = "123456"

    response = page.request.post(
        "http://api:8000/users/",
        data={
            "name": f"Swagger {prefix} User",
            "email": email,
            "password": password,
            "full_name": f"Swagger {prefix} User",
        },
    )

    assert response.status == 201, (
        f"Failed to create test user: "
        f"{response.status} "
        f"{response.text()}"
    )

    return email, password


def create_test_post(
    page,
    email: str,
    password: str,
    title: str,
    content: str,
) -> tuple[str, int]:
    login_response = page.request.post(
        "http://api:8000/auth/login",
        form={
            "username": email,
            "password": password,
        },
    )

    assert login_response.status == 200, (
        f"Login failed: "
        f"{login_response.status} "
        f"{login_response.text()}"
    )

    token = login_response.json()["access_token"]

    post_response = page.request.post(
        "http://api:8000/posts/",
        headers={
            "Authorization": f"Bearer {token}",
        },
        data={
            "title": title,
            "content": content,
        },
    )

    assert post_response.status == 201, (
        f"Failed to create test post: "
        f"{post_response.status} "
        f"{post_response.text()}"
    )

    post_id = post_response.json()["id"]

    return token, post_id

def authorize_swagger(
    page,
    email: str,
    password: str,
) -> None:
    authorize_button = page.get_by_role(
        "button",
        name="Authorize",
    )

    expect(authorize_button).to_be_visible()
    authorize_button.click()

    dialog = page.locator(".modal-ux")

    expect(dialog).to_be_visible()

    username_input = dialog.get_by_role(
        "textbox",
        name="username:",
    )

    password_input = dialog.get_by_role(
        "textbox",
        name="password:",
    )

    username_input.fill(email)
    password_input.fill(password)

    apply_button = dialog.get_by_role(
        "button",
        name="Apply given OAuth2 credentials",
    )

    expect(apply_button).to_be_enabled()
    apply_button.click()

    page.evaluate("""
        () => {
            document.querySelectorAll(
                '.modal-ux, .dialog-ux, .backdrop-ux'
            ).forEach(element => {
                element.remove();
            });
        }
    """)

    authorization_button = page.get_by_role(
        "button",
        name="authorization button unlocked",
    ).first

    expect(authorization_button).to_be_visible()



def fill_post_id(endpoint, post_id: int) -> None:
    post_id_input = endpoint.get_by_role(
        "textbox",
        name="post_id",
    )

    expect(post_id_input).to_be_visible()
    post_id_input.fill(str(post_id))


def test_swagger_create_post(page):
    email, password = create_test_user(
        page,
        "post",
    )

    open_swagger(page)

    authorize_swagger(
        page,
        email,
        password,
    )

    endpoint = get_post_endpoint(
        page,
        "/posts/",
    )

    endpoint.locator(".opblock-summary").click()

    click_try_it_out(endpoint)

    fill_request_body(
        endpoint,
        """{
            "title": "Swagger E2E Post",
            "content": "Post created through Swagger UI E2E test"
}""",
    )

    click_execute(endpoint)

    response_section = endpoint.locator(
        ".responses-inner"
    )

    expect(response_section).to_contain_text("201")
    expect(response_section).to_contain_text(
        "Swagger E2E Post"
    )
    expect(response_section).to_contain_text(
        "Post created through Swagger UI E2E test"
    )
    expect(response_section).to_contain_text(email)

    screenshot(
            page,
            "swagger/06_create_post_success.png",
        )


def test_swagger_get_posts(page):
    email, password = create_test_user(
        page,
        "get-posts",
    )

    create_test_post(
        page,
        email,
        password,
        "Swagger GET Posts Test",
        "Post for GET /posts/ E2E test",
    )

    open_swagger(page)

    endpoint = (
        page.locator(".opblock-get")
        .filter(has_text="/posts/")
        .first
    )

    expect(endpoint).to_be_visible()

    endpoint.locator(".opblock-summary").click()

    click_try_it_out(endpoint)
    click_execute(endpoint)

    response_section = endpoint.locator(
        ".responses-inner"
    )

    expect(response_section).to_contain_text("200")
    expect(response_section).to_contain_text(
        "Swagger GET Posts Test"
    )
    expect(response_section).to_contain_text(
        "Post for GET /posts/ E2E test"
    )
    expect(response_section).to_contain_text(email)

    screenshot(
        page,
        "swagger/07_get_posts_success.png",
    )


def test_swagger_get_post_by_id(page):
    email, password = create_test_user(
        page,
        "get-post",
    )

    _, post_id = create_test_post(
        page,
        email,
        password,
        "Swagger GET Post By ID",
        "Post for GET /posts/{post_id} E2E test",
    )

    open_swagger(page)

    endpoint = (
        page.locator(".opblock-get")
        .filter(has_text="/posts/{post_id}")
        .first
    )

    expect(endpoint).to_be_visible()

    endpoint.locator(".opblock-summary").click()

    click_try_it_out(endpoint)

    fill_post_id(
        endpoint,
        post_id,
    )

    click_execute(endpoint)

    response_section = endpoint.locator(
        ".responses-inner"
    )

    expect(response_section).to_contain_text("200")
    expect(response_section).to_contain_text(
        "Swagger GET Post By ID"
    )
    expect(response_section).to_contain_text(
        "Post for GET /posts/{post_id} E2E test"
    )
    expect(response_section).to_contain_text(email)

    screenshot(
        page,
        "swagger/08_get_post_by_id_success.png",
    )


def test_swagger_update_post(page):
    email, password = create_test_user(
        page,
        "update-post",
    )

    _, post_id = create_test_post(
        page,
        email,
        password,
        "Original Post Title",
        "Original post content",
    )

    open_swagger(page)

    authorize_swagger(
        page,
        email,
        password,
    )

    endpoint = (
        page.locator(".opblock-put")
        .filter(has_text="/posts/{post_id}")
        .first
    )

    expect(endpoint).to_be_visible()

    endpoint.locator(".opblock-summary").click()

    click_try_it_out(endpoint)

    fill_post_id(
        endpoint,
        post_id,
    )

    fill_request_body(
        endpoint,
        """{
  "title": "Updated Post Title",
  "content": "Updated post content"
}""",
    )

    click_execute(endpoint)

    response_section = endpoint.locator(
        ".responses-inner"
    )

    expect(response_section).to_contain_text("200")
    expect(response_section).to_contain_text(
        "Updated Post Title"
    )
    expect(response_section).to_contain_text(
        "Updated post content"
    )
    expect(response_section).to_contain_text(email)

    screenshot(
        page,
        "swagger/09_update_post_success.png",
    )
```


---

## `tests/e2e/test_swagger_users.py`

```python
from playwright.sync_api import expect

from tests.e2e.utils import (
    click_execute,
    click_try_it_out,
    fill_request_body,
    get_post_endpoint,
    open_swagger,
    screenshot,
)


def test_swagger_create_user(page):
    open_swagger(page)

    endpoint = get_post_endpoint(
        page,
        "/users/",
    )

    endpoint.click()

    click_try_it_out(endpoint)

    fill_request_body(
        endpoint,
        """{
  "name": "Swagger E2E User",
  "email": "swagger-e2e@example.com",
  "password": "123456",
  "full_name": "Swagger E2E User"
}""",
    )

    click_execute(endpoint)

    response_section = endpoint.locator(
        ".responses-inner"
    )

    expect(response_section).to_contain_text("201")
    expect(response_section).to_contain_text(
        "swagger-e2e@example.com"
    )
    expect(response_section).to_contain_text(
        "Swagger E2E User"
    )

    screenshot(
        page,
        "swagger/03_create_user_success.png",
    )
```


---

## `tests/e2e/utils.py`

```python
from pathlib import Path

from playwright.sync_api import Locator, Page, expect


SCREENSHOT_DIR = Path("tests/screenshots/automation")


def open_swagger(page: Page) -> None:
    page.goto("http://api:8000/docs")

    expect(page).to_have_title(
        "FastAPI User Management - Swagger UI"
    )


def get_post_endpoint(
    page: Page,
    path: str,
) -> Locator:
    endpoint = (
        page.locator(".opblock-post")
        .filter(has_text=path)
        .first
    )

    expect(endpoint).to_be_visible()

    return endpoint


def click_try_it_out(endpoint: Locator) -> None:
    endpoint.get_by_role(
        "button",
        name="Try it out",
    ).click()


def click_execute(endpoint: Locator) -> None:
    endpoint.get_by_role(
        "button",
        name="Execute",
    ).click()


def fill_request_body(
    endpoint: Locator,
    body: str,
) -> None:
    request_body = endpoint.locator("textarea")

    expect(request_body).to_be_visible()

    request_body.fill(body)


def fill_form_field(
    endpoint: Locator,
    field_name: str,
    value: str,
) -> None:
    field = endpoint.get_by_role(
        "textbox",
        name=field_name,
    )

    expect(field).to_be_visible()

    field.fill(value)


def screenshot(
    page: Page,
    filename: str,
) -> None:
    path = SCREENSHOT_DIR / filename

    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    page.screenshot(
        path=path,
        full_page=True,
    )
```


---

## `tests/integration/__init__.py`

```python

```


---

## `tests/integration/conftest.py`

```python
import os
from collections.abc import Generator
from pathlib import Path

import pytest
from alembic import command
from alembic.config import Config
from sqlalchemy import Engine, create_engine, text
from sqlalchemy.engine import make_url
from sqlalchemy.orm import Session

from app.core.config import settings


PROJECT_ROOT = Path(__file__).resolve().parents[2]

ALEMBIC_INI = PROJECT_ROOT / "alembic.ini"

TEST_DATABASE_NAME = "fastapi_test_db"


def build_alembic_config() -> Config:
    config = Config(
        str(ALEMBIC_INI)
    )

    config.set_main_option(
        "script_location",
        str(PROJECT_ROOT / "alembic"),
    )

    return config


@pytest.fixture(scope="session")
def postgres_test_database() -> Generator[
    str,
    None,
    None,
]:
    base_url = make_url(
        settings.DATABASE_URL
    )

    if (
        base_url.get_backend_name()
        != "postgresql"
    ):
        raise RuntimeError(
            "Integration tests require PostgreSQL."
        )

    admin_url = base_url.set(
        database="postgres"
    )

    test_url = base_url.set(
        database=TEST_DATABASE_NAME
    )

    test_database_url = (
        test_url.render_as_string(
            hide_password=False
        )
    )

    admin_engine = create_engine(
        admin_url,
        isolation_level="AUTOCOMMIT",
        pool_pre_ping=True,
    )

    with admin_engine.connect() as connection:
        connection.execute(
            text(
                """
                SELECT pg_terminate_backend(pid)
                FROM pg_stat_activity
                WHERE datname = :database_name
                  AND pid <> pg_backend_pid()
                """
            ),
            {
                "database_name":
                    TEST_DATABASE_NAME
            },
        )

        connection.exec_driver_sql(
            f'DROP DATABASE IF EXISTS '
            f'"{TEST_DATABASE_NAME}"'
        )

        connection.exec_driver_sql(
            f'CREATE DATABASE '
            f'"{TEST_DATABASE_NAME}"'
        )

    previous_database_url = os.environ.get(
        "DATABASE_URL"
    )

    os.environ[
        "DATABASE_URL"
    ] = test_database_url

    try:
        alembic_config = (
            build_alembic_config()
        )

        command.upgrade(
            alembic_config,
            "head",
        )

        yield test_database_url

    finally:
        if previous_database_url is None:
            os.environ.pop(
                "DATABASE_URL",
                None,
            )
        else:
            os.environ[
                "DATABASE_URL"
            ] = previous_database_url

        with admin_engine.connect() as connection:
            connection.execute(
                text(
                    """
                    SELECT pg_terminate_backend(pid)
                    FROM pg_stat_activity
                    WHERE datname = :database_name
                      AND pid <> pg_backend_pid()
                    """
                ),
                {
                    "database_name":
                        TEST_DATABASE_NAME
                },
            )

            connection.exec_driver_sql(
                f'DROP DATABASE IF EXISTS '
                f'"{TEST_DATABASE_NAME}"'
            )

        admin_engine.dispose()


@pytest.fixture(scope="session")
def pg_engine(
    postgres_test_database: str,
) -> Generator[
    Engine,
    None,
    None,
]:
    engine = create_engine(
        postgres_test_database,
        pool_pre_ping=True,
    )

    try:
        yield engine
    finally:
        engine.dispose()


@pytest.fixture(scope="function")
def pg_session(
    pg_engine: Engine,
) -> Generator[
    Session,
    None,
    None,
]:
    session = Session(
        bind=pg_engine
    )

    try:
        yield session

    finally:
        session.rollback()
        session.close()
```


---

## `tests/integration/test_migrations.py`

```python
from pathlib import Path

import pytest
from alembic.config import Config
from alembic.script import ScriptDirectory
from sqlalchemy import Engine, inspect, text


pytestmark = pytest.mark.integration


PROJECT_ROOT = Path(
    __file__
).resolve().parents[2]


def get_script_heads() -> set[str]:
    config = Config(
        str(
            PROJECT_ROOT
            / "alembic.ini"
        )
    )

    config.set_main_option(
        "script_location",
        str(
            PROJECT_ROOT
            / "alembic"
        ),
    )

    script = ScriptDirectory.from_config(
        config
    )

    return set(
        script.get_heads()
    )


def test_alembic_database_is_at_head(
    pg_engine: Engine,
):
    with pg_engine.connect() as connection:
        rows = connection.execute(
            text(
                """
                SELECT version_num
                FROM alembic_version
                """
            )
        )

        database_heads = {
            row[0]
            for row in rows
        }

    assert (
        database_heads
        == get_script_heads()
    )


def test_expected_tables_exist(
    pg_engine: Engine,
):
    inspector = inspect(
        pg_engine
    )

    tables = set(
        inspector.get_table_names()
    )

    assert "users" in tables
    assert "posts" in tables
    assert "alembic_version" in tables


def test_user_role_schema_constraints(
    pg_engine: Engine,
):
    inspector = inspect(
        pg_engine
    )

    columns = {
        column["name"]: column
        for column
        in inspector.get_columns(
            "users"
        )
    }

    role_column = columns[
        "role"
    ]

    assert (
        role_column["nullable"]
        is False
    )

    assert "user" in str(
        role_column["default"]
    ).lower()

    constraints = (
        inspector
        .get_check_constraints(
            "users"
        )
    )

    role_constraint = next(
        (
            constraint
            for constraint
            in constraints
            if (
                constraint["name"]
                == "ck_users_role_allowed"
            )
        ),
        None,
    )

    assert role_constraint is not None

    sql_text = str(
        role_constraint["sqltext"]
    ).lower()

    assert "user" in sql_text
    assert "admin" in sql_text

def test_user_lifecycle_columns_exist(
    pg_engine,
):
    inspector = inspect(
        pg_engine
    )

    columns = {
        column["name"]: column
        for column
        in inspector.get_columns(
            "users"
        )
    }

    assert "is_active" in columns
    assert "created_at" in columns
    assert "updated_at" in columns
    assert "last_login_at" in columns

    assert (
        columns["is_active"]["nullable"]
        is False
    )

    assert (
        columns["created_at"]["nullable"]
        is False
    )

    assert (
        columns["updated_at"]["nullable"]
        is False
    )


def test_post_lifecycle_schema_exists(
    pg_engine,
):
    inspector = inspect(
        pg_engine
    )

    columns = {
        column["name"]: column
        for column
        in inspector.get_columns(
            "posts"
        )
    }

    assert "status" in columns
    assert "created_at" in columns
    assert "updated_at" in columns

    assert (
        columns["status"]["nullable"]
        is False
    )

    assert (
        columns["created_at"]["nullable"]
        is False
    )

    assert (
        columns["updated_at"]["nullable"]
        is False
    )

    constraints = (
        inspector.get_check_constraints(
            "posts"
        )
    )

    status_constraint = next(
        (
            constraint
            for constraint
            in constraints
            if (
                constraint["name"]
                == "ck_posts_status_allowed"
            )
        ),
        None,
    )

    assert status_constraint is not None

    sql_text = str(
        status_constraint["sqltext"]
    ).lower()

    assert "draft" in sql_text
    assert "published" in sql_text
    assert "archived" in sql_text
```


---

## `tests/integration/test_postgres_behavior.py`

```python
import pytest
from sqlalchemy import select, text
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models import Post, User


pytestmark = pytest.mark.integration


def make_user(
    email: str,
    name: str = "Integration User",
    role: str = "user",
) -> User:
    return User(
        name=name,
        email=email,
        role=role,
        password="integration-test-hash",
        full_name=name,
    )


def test_duplicate_email_constraint(
    pg_session: Session,
):
    first_user = make_user(
        email="duplicate-pg@example.com",
        name="First User",
    )

    pg_session.add(
        first_user
    )

    pg_session.flush()

    second_user = make_user(
        email="duplicate-pg@example.com",
        name="Second User",
    )

    pg_session.add(
        second_user
    )

    with pytest.raises(
        IntegrityError
    ):
        pg_session.flush()

    pg_session.rollback()


def test_invalid_role_check_constraint(
    pg_session: Session,
):
    user = make_user(
        email="invalid-role-pg@example.com",
        role="superadmin",
    )

    pg_session.add(
        user
    )

    with pytest.raises(
        IntegrityError
    ):
        pg_session.flush()

    pg_session.rollback()


def test_role_not_null_constraint(
    pg_session: Session,
):
    with pytest.raises(
        IntegrityError
    ):
        pg_session.execute(
            text(
                """
                INSERT INTO users (
                    name,
                    email,
                    role,
                    password,
                    full_name
                )
                VALUES (
                    :name,
                    :email,
                    NULL,
                    :password,
                    :full_name
                )
                """
            ),
            {
                "name": "Null Role User",
                "email":
                    "null-role-pg@example.com",
                "password":
                    "integration-test-hash",
                "full_name":
                    "Null Role User",
            },
        )

    pg_session.rollback()


def test_post_user_foreign_key_constraint(
    pg_session: Session,
):
    post = Post(
        title="Invalid Owner Post",
        content="Integration test",
        user_id=999999999,
    )

    pg_session.add(
        post
    )

    with pytest.raises(
        IntegrityError
    ):
        pg_session.flush()

    pg_session.rollback()


def test_ilike_is_case_insensitive(
    pg_session: Session,
):
    user = make_user(
        email="mixed-case@example.com",
        name="MiXeDCaseUser",
    )

    pg_session.add(
        user
    )

    pg_session.flush()

    statement = select(
        User
    ).where(
        User.name.ilike(
            "%mixedcaseuser%"
        )
    )

    result = pg_session.scalars(
        statement
    ).all()

    assert len(result) == 1

    assert (
        result[0].email
        == "mixed-case@example.com"
    )

def test_invalid_post_status_constraint(
    pg_session: Session,
):
    user = make_user(
        email="post-status-pg@example.com",
    )

    pg_session.add(user)
    pg_session.flush()

    post = Post(
        title="Invalid Status",
        content="Content",
        user_id=user.id,
        status="deleted",
    )

    pg_session.add(post)

    with pytest.raises(
        IntegrityError
    ):
        pg_session.flush()

    pg_session.rollback()
```


---

## `tests/swagger/test_auth_swagger.py`

```python

```


---

## `tests/swagger/test_posts_swagger.py`

```python

```


---

## `tests/swagger/test_users_swagger.py`

```python

```


---

## `tests/swagger/utils.py`

```python

```


---

## `tests/unit/test_query_efficiency.py`

```python
from collections.abc import Callable

from sqlalchemy import event
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from app.models import Post, User
from app.repositories.post_repository import (
    PostRepository,
)
from app.repositories.user_repository import (
    UserRepository,
)


def count_select_queries(
    db_session: Session,
    operation: Callable,
) -> int:
    engine = db_session.get_bind()

    if not isinstance(
        engine,
        Engine,
    ):
        raise RuntimeError(
            "Expected Session to be bound "
            "to an Engine"
        )

    statements: list[str] = []

    def before_cursor_execute(
        connection,
        cursor,
        statement,
        parameters,
        context,
        executemany,
    ):
        normalized = (
            statement
            .lstrip()
            .upper()
        )

        if normalized.startswith(
            "SELECT"
        ):
            statements.append(
                statement
            )

    event.listen(
        engine,
        "before_cursor_execute",
        before_cursor_execute,
    )

    try:
        operation()

    finally:
        event.remove(
            engine,
            "before_cursor_execute",
            before_cursor_execute,
        )

    return len(statements)


def seed_users_and_posts(
    db_session: Session,
) -> None:
    users = []

    for index in range(3):
        user = User(
            name=(
                f"Query User {index}"
            ),
            email=(
                f"query-user-{index}"
                "@example.com"
            ),
            role="user",
            password="test-hash",
            full_name=(
                f"Query User {index}"
            ),
        )

        db_session.add(user)
        users.append(user)

    db_session.flush()

    for index, user in enumerate(
        users
    ):
        db_session.add(
            Post(
                title=(
                    f"Query Post {index}"
                ),
                content="Content",
                user_id=user.id,
            )
        )

    db_session.commit()

    db_session.expunge_all()


def test_user_list_uses_two_select_queries(
    db_session,
):
    seed_users_and_posts(
        db_session
    )

    repository = UserRepository(
        db_session
    )

    query_count = (
        count_select_queries(
            db_session,
            lambda: repository.get_all(
                limit=10,
                offset=0,
            ),
        )
    )

    # SELECT users
    # +
    # SELECT posts WHERE user_id IN (...)
    assert query_count == 2


def test_post_list_uses_one_select_query(
    db_session,
):
    seed_users_and_posts(
        db_session
    )

    repository = PostRepository(
        db_session
    )

    query_count = (
        count_select_queries(
            db_session,
            lambda: repository.get_all(
                limit=10,
                offset=0,
            ),
        )
    )

    # Post.owner is many-to-one,
    # so joinedload can load everything
    # in one SELECT.
    assert query_count == 1
```


---

## `tests/unit/test_service_exceptions.py`

```python
import pytest

from app.core.exceptions import (
    PermissionDeniedError,
    ResourceNotFoundError,
)
from app.models import Post, User
from app.schemas.post import PostUpdate
from app.services.post_service import PostService
from app.services.user_service import UserService


def test_user_service_not_found(
    db_session,
):
    service = UserService(
        db_session
    )

    with pytest.raises(
        ResourceNotFoundError
    ) as exc_info:
        service.get_user(
            999999
        )

    assert (
        exc_info.value.message
        == "User not found"
    )


def test_post_service_not_found(
    db_session,
):
    service = PostService(
        db_session
    )

    with pytest.raises(
        ResourceNotFoundError
    ) as exc_info:
        service.get_post(
            999999
        )

    assert (
        exc_info.value.message
        == "Post not found"
    )


def test_post_service_rejects_non_owner(
    db_session,
):
    owner = User(
        name="Owner",
        email="owner-service@example.com",
        role="user",
        password="hashed-password",
        full_name="Owner",
    )

    other_user = User(
        name="Other User",
        email="other-service@example.com",
        role="user",
        password="hashed-password",
        full_name="Other User",
    )

    db_session.add_all(
        [
            owner,
            other_user,
        ]
    )

    db_session.commit()

    post = Post(
        title="Owned Post",
        content="Content",
        user_id=owner.id,
    )

    db_session.add(post)
    db_session.commit()
    db_session.refresh(post)

    service = PostService(
        db_session
    )

    update_data = PostUpdate(
        title="Updated Post",
        content="Updated Content",
    )

    with pytest.raises(
        PermissionDeniedError
    ) as exc_info:
        service.update_post(
            post.id,
            update_data,
            other_user.id,
        )

    assert (
        exc_info.value.message
        == "You do not own this post"
    )
```


---

## `tests/unit/test_user_integrity.py`

```python
import pytest
from sqlalchemy.exc import IntegrityError

from app.core.exceptions import ConflictError
from app.core.security import hash_password
from app.models import User
from app.schemas.user import UserCreate
from app.services.user_service import UserService


def test_user_default_role_is_user(
    db_session,
):
    user = User(
        name="Default Role User",
        email="default-role@example.com",
        password=hash_password(
            "123456"
        ),
        full_name="Default Role User",
    )

    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)

    assert user.role == "user"


def test_database_rejects_invalid_role(
    db_session,
):
    user = User(
        name="Invalid Role User",
        email="invalid-role-db@example.com",
        role="superadmin",
        password=hash_password(
            "123456"
        ),
        full_name="Invalid Role User",
    )

    db_session.add(user)

    with pytest.raises(
        IntegrityError
    ):
        db_session.commit()

    db_session.rollback()


def test_database_unique_constraint_rejects_duplicate_email(
    db_session,
):
    first_user = User(
        name="First User",
        email="duplicate-db@example.com",
        role="user",
        password=hash_password(
            "123456"
        ),
        full_name="First User",
    )

    second_user = User(
        name="Second User",
        email="duplicate-db@example.com",
        role="user",
        password=hash_password(
            "123456"
        ),
        full_name="Second User",
    )

    db_session.add(first_user)
    db_session.commit()

    db_session.add(second_user)

    with pytest.raises(
        IntegrityError
    ):
        db_session.commit()

    db_session.rollback()


def test_service_converts_unique_race_to_conflict(
    db_session,
    monkeypatch,
):
    existing_user = User(
        name="Existing User",
        email="race@example.com",
        role="user",
        password=hash_password(
            "123456"
        ),
        full_name="Existing User",
    )

    db_session.add(existing_user)
    db_session.commit()

    service = UserService(
        db_session
    )

    monkeypatch.setattr(
        service.repository,
        "get_by_email",
        lambda email: None,
    )

    user_data = UserCreate(
        name="Race User",
        email="race@example.com",
        password="123456",
        full_name="Race User",
    )

    with pytest.raises(
        ConflictError
    ) as exc_info:
        service.create_user(
            user_data
        )

    assert (
        exc_info.value.message
        == "Email already exists"
    )
```
