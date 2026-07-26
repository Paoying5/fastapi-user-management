<h1 align="center">
🚀 FastAPI User Management
</h1>

<p align="center">
A learning project built with <strong>FastAPI</strong>, <strong>SQLAlchemy ORM</strong>, <strong>PostgreSQL</strong>, <strong>Docker</strong>, and <strong>JWT Authentication</strong>.
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-009688?logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue?logo=postgresql)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red)
![Docker](https://img.shields.io/badge/Docker-Container-2496ED?logo=docker)
![JWT](https://img.shields.io/badge/JWT-Authentication-black)
![License](https://img.shields.io/badge/License-MIT-green)

</p>

---

# 📖 Project Overview

This project is part of my backend learning journey using **FastAPI** and **PostgreSQL**.

The goal is not only to build a CRUD application, but also to understand how a real backend system is structured, how authentication works, and how SQLAlchemy communicates with PostgreSQL.

This repository will continue to grow into a more practical and enterprise-oriented backend project.

---

# ✨ Features

## 👤 User Management

- Create User
- Get All Users
- Get User by ID
- Update User
- Delete User

---

## 📝 Post Management

- Create Post
- Get All Posts
- Get Post by ID
- Get Current User's Posts (`/posts/me`)
- Update only your own post
- Relationship between User and Post

---

## 🔐 Authentication

- JWT Authentication
- OAuth2 Password Flow
- Login API
- Current User API (`/auth/me`)
- Protected Endpoints
- Password Hashing with BCrypt

---

## 🗄 Database

- PostgreSQL
- SQLAlchemy ORM
- One-to-Many Relationship
- Foreign Key
- Joined Loading (`joinedload`)
- Password Encryption

---

## 🔍 SQL Practice

During this project I also practiced SQL concepts behind SQLAlchemy:

- SELECT
- INSERT
- UPDATE
- DELETE
- WHERE
- ORDER BY
- LIMIT
- Relationships
- Foreign Keys

More SQL features will be implemented in future updates.

---

# 🏗 Project Structure

```text
fastapi-user-management/

├── app/
│   ├── core/
│   ├── routers/
│   ├── utils/
│   ├── crud.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── main.py
│
├── tests/
│   └── screenshots/
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

---

# ⚙️ Tech Stack

| Technology | Description |
|------------|-------------|
| Python | Main Programming Language |
| FastAPI | Backend Framework |
| PostgreSQL | Relational Database |
| SQLAlchemy ORM | Database ORM |
| Docker | Containerization |
| JWT | Authentication |
| Uvicorn | ASGI Server |
| Pydantic v2 | Data Validation |

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

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Start Docker

```bash
docker compose up --build
```

---

## Run FastAPI

```bash
uvicorn app.main:app --reload
```

---

# 📚 API Documentation

After starting the server:

Swagger UI

```
http://127.0.0.1:8000/docs
```

OpenAPI

```
http://127.0.0.1:8000/openapi.json
```

---

# 📷 API Testing

Swagger API testing screenshots are available in:

```
tests/screenshots/
```

## Authentication

![](tests/screenshots/Authentication/Authentication%20Post%20Auth%20Login.png)

---

## Users API

![](tests/screenshots/User/Test%20Get%20User.png)

---

## Posts API

![](tests/screenshots/Post/Get%20Posts.png)

---

# 📈 Learning Progress

Completed:

- ✅ FastAPI Basics
- ✅ APIRouter
- ✅ Dependency Injection
- ✅ Pydantic Schema
- ✅ CRUD Operations
- ✅ SQLAlchemy ORM
- ✅ PostgreSQL
- ✅ Docker
- ✅ JWT Authentication
- ✅ Password Hashing
- ✅ User Authorization
- ✅ One-to-Many Relationship
- ✅ Git & GitHub
- ✅ Swagger API Testing

Currently Learning:

- 🔄 Pagination
- 🔄 Search
- 🔄 Advanced SQLAlchemy Query
- 🔄 JOIN
- 🔄 Aggregate Functions
- 🔄 Alembic Migration

Future Goals:

- Redis
- Celery
- CI/CD
- Unit Testing
- Nginx
- Deployment
- Clean Architecture
- Enterprise Backend Design

---

# 🎯 Learning Objectives

This project focuses on understanding:

- Backend API Development
- Database Design
- Authentication & Authorization
- SQL Fundamentals
- SQLAlchemy ORM
- Docker Workflow
- RESTful API Design
- Clean Project Structure

---

# 👨‍💻 Author

**Phạm Nguyễn Nhật Trường**

Final-year Information Technology Student

GitHub

https://github.com/Paoying5

---

# ⭐ Notes

This project is built for learning purposes.

I continuously improve this repository as I learn new backend technologies and best practices. My long-term goal is to evolve it into a more practical, production-oriented backend system inspired by real enterprise applications.
