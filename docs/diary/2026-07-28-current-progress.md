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