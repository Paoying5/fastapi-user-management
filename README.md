 <h1 align="center">FastAPI User Management & Analytics Dashboard</h1>

<p align="center">
  A backend development project built with FastAPI and PostgreSQL, featuring SQL analytics and an online dashboard built with Next.js.
</p>

<p align="center">
  <a href="fastapi-user-management-dashboard-three.vercel.app">
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
  <a href="fastapi-user-management-dashboard-three.vercel.app">
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
  <a href="fastapi-user-management-dashboard-three.vercel.app">
    <img src="https://img.shields.io/badge/Visit%20Dashboard-paoying--data.vercel.app-black?style=for-the-badge&logo=vercel" alt="Visit the online dashboard">
  </a>
</p>

**Live URL:** [https://paoying-data.vercel.app](fastapi-user-management-dashboard-three.vercel.app)

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
- Live Dashboard: [paoying-data.vercel.app](fastapi-user-management-dashboard-three.vercel.app)

---

<p align="center">
  <strong>Built with FastAPI, PostgreSQL, Next.js, and a focus on practical backend and analytics development.</strong>
</p>
