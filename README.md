<h1 align="center">
🚀 FastAPI User Management
</h1>

<p align="center">
A backend learning project built with <strong>FastAPI</strong>, <strong>SQLAlchemy ORM</strong>, <strong>PostgreSQL</strong>, <strong>Docker</strong>, and <strong>JWT Authentication</strong>.
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-009688?logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue?logo=postgresql)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red)
![Docker](https://img.shields.io/badge/Docker-Container-2496ED?logo=docker)
![JWT](https://img.shields.io/badge/JWT-Authentication-black)
![Linux](https://img.shields.io/badge/Linux-Bash-orange?logo=linux)
![License](https://img.shields.io/badge/License-MIT-green)

</p>

---

# 📖 Project Overview

FastAPI User Management is a backend learning project focused on building a practical REST API system.

The project was created to understand how a modern backend application is structured, including:

* API design
* Database modeling
* Authentication and authorization
* ORM communication
* Containerized development workflow
* Linux automation scripts

The project continues to evolve toward a more production-oriented backend architecture.

---

# ✨ Features

## 👤 User Management

Implemented:

* Create User
* Get All Users
* Get User By ID
* Update User
* Delete User

---

## 📝 Post Management

Implemented:

* Create Post
* Get All Posts
* Get Post By ID
* Get Current User Posts
* Update Own Post
* User - Post Relationship

Database relationship:

```
User (1) -------- (*) Post
```

---

# 🔐 Authentication & Security

Implemented:

* JWT Authentication
* OAuth2 Password Flow
* Login API
* Current User API
* Protected Routes
* Password Hashing with BCrypt

Authentication flow:

```
User
 |
 | Login
 v
FastAPI
 |
 | Generate JWT
 v
Access Token
 |
 | Bearer Token
 v
Protected Endpoint
```

---

# 🗄 Database

Database:

* PostgreSQL 16
* SQLAlchemy ORM

Implemented concepts:

* Table Modeling
* Primary Key
* Foreign Key
* One-to-Many Relationship
* Query Filtering
* Ordering
* Pagination preparation
* Joined Loading

Example:

```
users

id
name
email
role
password


posts

id
title
content
user_id
```

---

# 🏗 Project Architecture

```
Client

   |
   |
   v

FastAPI Router

   |
   |
   v

CRUD Layer

   |
   |
   v

SQLAlchemy ORM

   |
   |
   v

PostgreSQL Database
```

Application layers:

```
app/

├── routers
│   API endpoints

├── schemas
│   Request / Response validation

├── models
│   Database models

├── crud
│   Database operations

├── core
│   Configuration and security

└── utils
    Helper functions
```

---

# 📂 Project Structure

```
fastapi-user-management/

├── app/
│   ├── core/
│   │   ├── config.py
│   │   └── security.py
│   │
│   ├── routers/
│   │   ├── auth.py
│   │   ├── user.py
│   │   └── post.py
│   │
│   ├── utils/
│   │   └── response.py
│   │
│   ├── crud.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── main.py
│
├── scripts/
│   └── menu.sh
│
├── tests/
│   └── screenshots/
│
├── notebook/
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── .env
└── README.md
```

---

# ⚙️ Tech Stack

| Technology     | Purpose                    |
| -------------- | -------------------------- |
| Python 3.12    | Programming Language       |
| FastAPI        | Backend Framework          |
| PostgreSQL 16  | Relational Database        |
| SQLAlchemy     | ORM                        |
| Pydantic v2    | Data Validation            |
| Docker         | Containerization           |
| Docker Compose | Multi-container Management |
| JWT            | Authentication             |
| Uvicorn        | ASGI Server                |
| Bash Script    | Development Automation     |

---

# 🐳 Docker Development Workflow

This project uses Docker Compose to simplify environment setup.

Instead of manually running:

```bash
pip install -r requirements.txt

uvicorn app.main:app --reload
```

the application can run through containers.

Services:

```
docker-compose.yml


api

|
|
FastAPI Container


postgres

|
|
PostgreSQL Container
```

---

# 🚀 Getting Started

## Clone Repository

### HTTPS

```bash
git clone https://github.com/Paoying5/fastapi-user-management.git
```

### SSH

```bash
git clone git@github.com:Paoying5/fastapi-user-management.git
```

---

## Enter Project

```bash
cd fastapi-user-management
```

---

# Option 1: Using Automation Menu (Recommended)

Give permission:

```bash
chmod +x scripts/menu.sh
```

Run:

```bash
./scripts/menu.sh
```

The menu provides shortcuts for:

```
1. Start Containers
2. Stop Containers
3. Restart Containers
4. Rebuild Containers

5. Application Shell
6. PostgreSQL Shell
7. View Logs

8. Reset Database

9. Alembic Migration

10. Docker Utilities

0. Exit
```

---

# Option 2: Using Docker Compose

Build and start:

```bash
docker compose up --build -d
```

Check containers:

```bash
docker compose ps
```

---

# 🌐 API Documentation

After starting the application:

Swagger UI:

```
http://127.0.0.1:8000/docs
```

OpenAPI:

```
http://127.0.0.1:8000/openapi.json
```

---

# 🐘 PostgreSQL Access

Open PostgreSQL shell:

```bash
docker compose exec postgres psql -U admin -d fastapi_db
```

Database information:

```
Database:
fastapi_db

User:
admin

Port:
5433
```

---

# 📜 Automation Scripts

The project contains Bash scripts to simplify repetitive development commands.

Location:

```
scripts/
```

Current:

```
scripts/

└── menu.sh
```

Purpose:

* Reduce repetitive Docker commands
* Provide developer-friendly workflow
* Simplify project operation

Future scripts:

* Git automation
* Database migration helper
* Backup scripts
* Deployment scripts

---

# 📷 API Testing Screenshots

Swagger API testing results:

```
tests/screenshots/
```

Examples:

## Authentication

![Authentication](tests/screenshots/Authentication/Authentication%20Post%20Auth%20Login.png)

## Users

![Users](tests/screenshots/User/Test%20Get%20User.png)

## Posts

![Posts](tests/screenshots/Post/Get%20Posts.png)

---

# 📚 SQL Practice

During development, SQL concepts were practiced through SQLAlchemy:

* SELECT
* INSERT
* UPDATE
* DELETE
* WHERE
* ORDER BY
* LIMIT
* Foreign Key
* Relationship Query
* JOIN preparation

---

# 📈 Learning Progress

Completed:

* ✅ FastAPI Fundamentals
* ✅ APIRouter
* ✅ Dependency Injection
* ✅ Pydantic Schema
* ✅ CRUD Operations
* ✅ SQLAlchemy ORM
* ✅ PostgreSQL
* ✅ Docker
* ✅ Docker Compose
* ✅ JWT Authentication
* ✅ Password Hashing
* ✅ Authorization
* ✅ One-to-Many Relationship
* ✅ Git & GitHub
* ✅ Linux Terminal Workflow
* ✅ Bash Automation Script

Currently Learning:

* 🔄 Pagination
* 🔄 Search
* 🔄 Advanced SQLAlchemy Query
* 🔄 JOIN
* 🔄 Aggregate Functions
* 🔄 Alembic Migration
* 🔄 Unit Testing

Future Goals:

* Redis
* Celery
* CI/CD
* Nginx
* Deployment
* Clean Architecture
* Enterprise Backend Design

---

# 🎯 Learning Objectives

This project focuses on:

* Backend API Development
* Database Design
* Authentication System
* RESTful API Design
* Docker Workflow
* Linux Development Environment
* Software Project Organization

---

# 👨‍💻 Author

**Phạm Nguyễn Nhật Trường**

Final-year Information Technology Student

GitHub:

https://github.com/Paoying5

---

# ⭐ Notes

This project is built for learning purposes.

The repository documents my backend development journey, including daily learning notes, implementation experiments, and improvements toward a more practical backend system.

The goal is to gradually transform this project into a production-oriented backend application following real-world engineering practices.
