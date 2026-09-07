# PROJECT CONTEXT

**Project root:** `/home/truongp/Documents/fastapi-user-management`  
**Total included files:** 109

## Project Structure

- `.dockerignore`
- `.gitignore`
- `Dockerfile`
- `LICENSE`
- `README.md`
- `alembic.ini`
- `alembic/env.py`
- `alembic/versions/e7d9b8aad922_initial_schema.py`
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
- `docs/diary/2026-08-02-current-progress.md`
- `docs/diary/2026-08-03-current-progress.md`
- `docs/diary/2026-08-04-current-progress.md`
- `docs/diary/2026-08-05-current-progress.md`
- `docs/diary/2026-08-06-current-progress.md`
- `docs/diary/2026-08-07-current-progress.md`
- `docs/diary/2026-08-08-current-progress.md`
- `docs/diary/2026-08-09-current-progress.md`
- `docs/diary/2026-08-09-project-summary.md`
- `docs/diary/2026-08-1-current-progress.md`
- `docs/diary/2026-08-10-current-progress.md`
- `docs/diary/2026-08-10-to-2026-08-28-retrospective-gap.md`
- `docs/diary/2026-08-11-current-progress.md`
- `docs/diary/2026-08-12-current-progress.md`
- `docs/diary/2026-08-13-current-progress.md`
- `docs/diary/2026-08-14-current-progress.md`
- `docs/diary/2026-08-15-current-progress.md`
- `docs/diary/2026-08-16-current-progress.md`
- `docs/diary/2026-08-17-current-progress.md`
- `docs/diary/2026-08-18-current-progress.md`
- `docs/diary/2026-08-19-current-progress.md`
- `docs/diary/2026-08-20-current-progress.md`
- `docs/diary/2026-08-21-current-progress.md`
- `docs/diary/2026-08-22-current-progress.md`
- `docs/diary/2026-08-23-current-progress.md`
- `docs/diary/2026-08-24-current-progress.md`
- `docs/diary/2026-08-25-current-progress.md`
- `docs/diary/2026-08-26-current-progress.md`
- `docs/diary/2026-08-27-current-progress.md`
- `docs/diary/2026-08-28-current-progress.md`
- `docs/diary/2026-08-29-current-progress.md`
- `docs/diary/2026-08-30-current-progress.md`
- `docs/diary/2026-08-31-current-progress.md`
- `docs/diary/2026-09-01-current-progress.md`
- `docs/diary/2026-09-02-current-progress.md`
- `docs/diary/2026-09-03-current-progress.md`
- `docs/diary/2026-09-04-current-progress.md`
- `docs/diary/2026-09-05-current-progress.md`
- `docs/diary/2026-09-06-current-progress.md`
- `docs/diary/README.md`
- `export_project.py`
- `pytest.ini`
- `requirements-dev.txt`
- `requirements.txt`
- `scripts/menu.sh`
- `test_connection.py`
- `tests/__init__.py`
- `tests/api/test_auth.py`
- `tests/api/test_create_user.py`
- `tests/api/test_health.py`
- `tests/api/test_posts.py`
- `tests/api/test_users.py`
- `tests/conftest.py`
- `tests/e2e/__init__.py`
- `tests/e2e/test_swagger_auth.py`
- `tests/e2e/test_swagger_home.py`
- `tests/e2e/test_swagger_posts.py`
- `tests/e2e/test_swagger_users.py`
- `tests/e2e/utils.py`
- `tests/swagger/test_auth_swagger.py`
- `tests/swagger/test_posts_swagger.py`
- `tests/swagger/test_users_swagger.py`
- `tests/swagger/utils.py`

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
```


---

## `Dockerfile`

```dockerfile
FROM python:3.12-slim

WORKDIR /app

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

```


---

## `app/core/logging.py`

```python

```


---

## `app/core/security.py`

```python
from passlib.context import CryptContext
from datetime import datetime
from datetime import timedelta
from datetime import timezone

from jose import jwt

from app.core.config import settings

pwd_context = CryptContext(
        schemes=["bcrypt"], 
        deprecated="auto"
)

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(
    plain_password: str,
    hashed_password: str
) -> bool:

    return pwd_context.verify(
        plain_password,
        hashed_password
    )

def create_access_token(data: dict) -> str:

    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(

        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES

    )

    to_encode.update(

        {

            "exp": expire

        }

    )

    encoded_jwt = jwt.encode(

        to_encode,

        settings.SECRET_KEY,

        algorithm=settings.ALGORITHM

    )

    return encoded_jwt
```


---

## `app/database.py`

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.core.config import settings


engine = create_engine(
    settings.DATABASE_URL,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
```


---

## `app/dependencies.py`

```python
from collections.abc import Generator

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from app.core.config import settings
from app.database import SessionLocal
from app.models import User
from app.services.auth_service import AuthService
from app.services.post_service import PostService
from app.services.user_service import UserService


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_user_service(db: Session = Depends(get_db)) -> UserService:
    return UserService(db)


def get_post_service(db: Session = Depends(get_db)) -> PostService:
    return PostService(db)


def get_auth_service(db: Session = Depends(get_db)) -> AuthService:
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

        email = payload.get("sub")

        if not isinstance(email, str):
            raise credentials_exception

    except JWTError as exc:
        raise credentials_exception from exc

    user = service.get_user_by_email(email)

    if user is None:
        raise credentials_exception

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
from fastapi import FastAPI

from app.routers import auth, health, post, user


app = FastAPI(
    title="FastAPI User Management",
    version="0.2.0",
    description=(
        "User and post management API built with "
        "FastAPI, SQLAlchemy, PostgreSQL and JWT."
    ),
)


# Register routers
app.include_router(health.router)
app.include_router(auth.router)
app.include_router(user.router)
app.include_router(post.router)


@app.get("/", tags=["Default"])
def root():
    return {
        "message": "FastAPI User Management is running",
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
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.database import Base


class Post(Base):
    __tablename__ = "posts"

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

    owner = relationship(
        "User",
        back_populates="posts",
    )
```


---

## `app/models/user.py`

```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class User(Base):
    __tablename__ = "users"

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
        nullable=True,
    )

    password = Column(
        String(255),
        nullable=False,
    )

    posts = relationship(
        "Post",
        back_populates="owner",
        cascade="all, delete-orphan",
    )

    full_name = Column(
    String(100),
    nullable=True,
)
```


---

## `app/repositories/__init__.py`

```python

```


---

## `app/repositories/post_repository.py`

```python
from sqlalchemy import desc, select
from sqlalchemy.orm import Session, joinedload

from app.models.post import Post


class PostRepository:
    """Persistence operations for Post entities only."""

    def __init__(self, db: Session):
        self.db = db

    def get_all(
        self,
        limit: int = 10,
        offset: int = 0,
        search: str = "",
    ) -> list[Post]:

        statement = (
            select(Post)
            .options(joinedload(Post.owner))
        )

        if search:
            statement = statement.where(
                Post.title.ilike(
                    f"%{search}%"
                )
            )

        statement = (
            statement
            .order_by(desc(Post.id))
            .offset(offset)
            .limit(limit)
        )

        return list(
            self.db.scalars(statement).unique().all()
        )

    def get_by_id(
        self,
        post_id: int,
    ) -> Post | None:

        statement = (
            select(Post)
            .options(joinedload(Post.owner))
            .where(Post.id == post_id)
        )

        return self.db.scalars(
            statement
        ).unique().first()

    def get_by_user_id(
        self,
        user_id: int,
    ) -> list[Post]:

        statement = (
            select(Post)
            .options(joinedload(Post.owner))
            .where(Post.user_id == user_id)
            .order_by(desc(Post.id))
        )

        return list(
            self.db.scalars(statement).unique().all()
        )

    def add(self, post: Post) -> Post:
        self.db.add(post)
        self.db.flush()
        self.db.refresh(post)
        return post

    def update(self, post: Post) -> Post:
        self.db.flush()
        self.db.refresh(post)
        return post

    def delete(self, post: Post) -> None:
        self.db.delete(post)
        self.db.flush()
```


---

## `app/repositories/user_repository.py`

```python
from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload

from app.models.user import User


class UserRepository:
    """Persistence operations for User entities only."""

    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[User]:
        statement = (
            select(User)
            .options(joinedload(User.posts))
            .order_by(User.id.asc())
        )

        return list(
            self.db.scalars(statement).unique().all()
        )

    def get_by_id(
        self,
        user_id: int,
    ) -> User | None:

        statement = (
            select(User)
            .options(joinedload(User.posts))
            .where(User.id == user_id)
        )

        return self.db.scalars(
            statement
        ).unique().first()

    def get_by_email(
        self,
        email: str,
    ) -> User | None:

        statement = select(User).where(
            User.email == email
        )

        return self.db.scalars(statement).first()

    def add(self, user: User) -> User:
        self.db.add(user)
        self.db.flush()
        self.db.refresh(user)
        return user

    def update(self, user: User) -> User:
        self.db.flush()
        self.db.refresh(user)
        return user

    def delete(self, user: User) -> None:
        self.db.delete(user)
        self.db.flush()
```


---

## `app/routers/__init__.py`

```python

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
from fastapi import APIRouter, Depends, Query, status

from app.dependencies import get_current_user, get_post_service
from app.models import User
from app.schemas import MessageResponse, PostCreate, PostPatch, PostResponse, PostUpdate
from app.services.post_service import PostService


router = APIRouter(prefix="/posts", tags=["Posts"])


@router.post("/", response_model=PostResponse, status_code=status.HTTP_201_CREATED)
def create_post(
    post_data: PostCreate,
    service: PostService = Depends(get_post_service),
    current_user: User = Depends(get_current_user),
):
    return service.create_post(post_data, current_user.id)


@router.get("/", response_model=list[PostResponse])
def get_posts(
    limit: int = Query(default=10, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    search: str = Query(default="", max_length=100),
    service: PostService = Depends(get_post_service),
):
    return service.get_posts(limit, offset, search)


@router.get("/me", response_model=list[PostResponse])
def get_my_posts(
    service: PostService = Depends(get_post_service),
    current_user: User = Depends(get_current_user),
):
    return service.get_my_posts(current_user.id)


@router.get("/{post_id}", response_model=PostResponse)
def get_post(post_id: int, service: PostService = Depends(get_post_service)):
    post = service.get_post(post_id)
    if post is None:
        from fastapi import HTTPException
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return post


@router.put("/{post_id}", response_model=PostResponse)
def update_post(
    post_id: int,
    post_data: PostUpdate,
    service: PostService = Depends(get_post_service),
    current_user: User = Depends(get_current_user),
):
    return service.update_post(post_id, post_data, current_user.id)


@router.patch("/{post_id}", response_model=PostResponse)
def patch_post(
    post_id: int,
    post_data: PostPatch,
    service: PostService = Depends(get_post_service),
    current_user: User = Depends(get_current_user),
):
    return service.patch_post(post_id, post_data, current_user.id)


@router.delete("/{post_id}", response_model=MessageResponse)
def delete_post(
    post_id: int,
    service: PostService = Depends(get_post_service),
    current_user: User = Depends(get_current_user),
):
    service.delete_post(post_id, current_user.id)
    return MessageResponse(message="Post deleted successfully")
```


---

## `app/routers/user.py`

```python
from app.models.user import User
from fastapi import APIRouter, Depends, HTTPException, status

from app.dependencies import get_admin_user, get_user_service
from app.schemas import APIResponse, UserCreate, UserPatch, UserResponse, UserUpdate
from app.services.user_service import UserService
from app.utils.response import response



router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=APIResponse, summary="Get all users")
def get_users(service: UserService = Depends(get_user_service), admin: User = Depends(get_admin_user)):
    users = service.get_users()
    data = [UserResponse.model_validate(user).model_dump() for user in users]
    return response("Users retrieved successfully", data)


@router.get("/{user_id}", response_model=APIResponse, summary="Get user by ID")
def get_user(user_id: int, service: UserService = Depends(get_user_service), admin: User = Depends(get_admin_user)):
    user = service.get_user(user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return response("User found", UserResponse.model_validate(user).model_dump())


@router.post("/", response_model=APIResponse, status_code=status.HTTP_201_CREATED, summary="Create user")
def create_user(user: UserCreate, service: UserService = Depends(get_user_service)):
    db_user = service.create_user(user)
    return response("User created successfully", UserResponse.model_validate(db_user).model_dump())


@router.put("/{user_id}", response_model=APIResponse, summary="Replace user")
def update_user(
    user_id: int,
    user: UserUpdate,
    service: UserService = Depends(get_user_service),
    admin: User = Depends(get_admin_user)
):
    updated_user = service.update_user(user_id, user)
    if updated_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return response("User updated successfully", UserResponse.model_validate(updated_user).model_dump())


@router.patch("/{user_id}", response_model=APIResponse, summary="Partially update user")
def patch_user(
    user_id: int,
    user_data: UserPatch,
    service: UserService = Depends(get_user_service),
    admin: User = Depends(get_admin_user)
):
    updated_user = service.patch_user(user_id, user_data)
    if updated_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return response("User partially updated successfully", UserResponse.model_validate(updated_user).model_dump())


@router.delete("/{user_id}", response_model=APIResponse, summary="Delete user")
def delete_user(user_id: int, service: UserService = Depends(get_user_service), admin: User = Depends(get_admin_user)):
    deleted = service.delete_user(user_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return response("User deleted successfully", None)
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
from typing import Any

from pydantic import BaseModel


class APIResponse(BaseModel):
    status: str
    message: str
    data: Any | None = None


class MessageResponse(BaseModel):
    message: str
```


---

## `app/schemas/post.py`

```python
from pydantic import BaseModel, ConfigDict, Field


class PostCreate(BaseModel):
    title: str = Field(
        min_length=2,
        max_length=255,
    )

    content: str | None = None


class PostUpdate(BaseModel):
    title: str = Field(
        min_length=2,
        max_length=255,
    )

    content: str | None = None


class PostPatch(BaseModel):
    title: str | None = Field(
        default=None,
        min_length=2,
        max_length=255,
    )

    content: str | None = None


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
    owner: UserSimple

    model_config = ConfigDict(
        from_attributes=True,
    )
```


---

## `app/schemas/user.py`

```python
from pydantic import BaseModel, ConfigDict, EmailStr, Field

from app.schemas.post import PostSimple


class UserCreate(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=100,
    )

    email: EmailStr

    password: str = Field(
        min_length=6,
        max_length=128,
    )

    # Không nên cho client tự tạo admin.
    # Service sẽ quyết định role mặc định.
    full_name: str | None = Field(
        default=None,
        max_length=100,
    )


class UserUpdate(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=100,
    )

    email: EmailStr

    role: str = Field(
        min_length=2,
        max_length=30,
    )

    full_name: str | None = Field(
        default=None,
        max_length=100,
    )


class UserPatch(BaseModel):
    name: str | None = Field(
        default=None,
        min_length=2,
        max_length=100,
    )

    email: EmailStr | None = None

    role: str | None = Field(
        default=None,
        min_length=2,
        max_length=30,
    )

    full_name: str | None = Field(
        default=None,
        max_length=100,
    )


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: str
    full_name: str | None = None

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
from sqlalchemy.orm import Session

from app.core.security import (
    create_access_token,
    verify_password,
)
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.auth import Token


class AuthService:
    """Authentication business rules."""

    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def authenticate_user(
        self,
        email: str,
        password: str,
    ) -> User | None:

        email = email.strip().lower()

        user = self.repository.get_by_email(email)

        if user is None:
            return None

        if not verify_password(
            password,
            user.password,
        ):
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

        return Token(
            access_token=create_access_token(
                {"sub": user.email}
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
```


---

## `app/services/post_service.py`

```python
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.post import Post
from app.repositories.post_repository import PostRepository
from app.schemas.post import PostCreate, PostPatch, PostUpdate


class PostService:
    """Business rules for posts, including ownership checks and transactions."""

    def __init__(self, db: Session):
        self.db = db
        self.repository = PostRepository(db)

    def create_post(self, post_data: PostCreate, user_id: int) -> Post:
        post = Post(
            title=post_data.title,
            content=post_data.content,
            user_id=user_id,
        )
        try:
            post = self.repository.add(post)
            self.db.commit()
            return self.repository.get_by_id(post.id)
        except Exception:
            self.db.rollback()
            raise

    def get_posts(self, limit: int = 10, offset: int = 0, search: str = "") -> list[Post]:
        return self.repository.get_all(limit, offset, search)

    def get_my_posts(self, user_id: int) -> list[Post]:
        return self.repository.get_by_user_id(user_id)

    def get_post(self, post_id: int) -> Post | None:
        return self.repository.get_by_id(post_id)

    def update_post(self, post_id: int, post_data: PostUpdate, user_id: int) -> Post:
        post = self._get_owned_post(post_id, user_id)
        post.title = post_data.title
        post.content = post_data.content
        return self._commit_update(post)

    def patch_post(self, post_id: int, post_data: PostPatch, user_id: int) -> Post:
        post = self._get_owned_post(post_id, user_id)
        for field_name, value in post_data.model_dump(exclude_unset=True).items():
            setattr(post, field_name, value)
        return self._commit_update(post)

    def delete_post(self, post_id: int, user_id: int) -> None:
        post = self._get_owned_post(post_id, user_id)
        try:
            self.repository.delete(post)
            self.db.commit()
        except Exception:
            self.db.rollback()
            raise

    def _get_owned_post(self, post_id: int, user_id: int) -> Post:
        post = self.repository.get_by_id(post_id)
        if post is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Post not found",
            )
        if post.user_id != user_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not own this post",
            )
        return post

    def _commit_update(self, post: Post) -> Post:
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
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserPatch, UserUpdate


class UserService:
    """Business rules for users. No direct SQL queries live here."""

    def __init__(self, db: Session):
        self.db = db
        self.repository = UserRepository(db)

    def get_users(self) -> list[User]:
        return self.repository.get_all()

    def get_user(self, user_id: int) -> User | None:
        return self.repository.get_by_id(user_id)

    def create_user(self, user_data: UserCreate) -> User:
        email = str(user_data.email).strip().lower()
        if self.repository.get_by_email(email) is not None:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already exists",
            )

        user = User(
            name=user_data.name,
            email=email,
            role="user",
            password=hash_password(user_data.password),
            full_name=user_data.full_name,
        )
        try:
            user = self.repository.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except Exception:
            self.db.rollback()
            raise

    def update_user(self, user_id: int, user_data: UserUpdate) -> User | None:
        user = self.repository.get_by_id(user_id)
        if user is None:
            return None

        email = str(user_data.email).strip().lower()
        if user.email != email and self.repository.get_by_email(email) is not None:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already exists",
            )

        user.name = user_data.name
        user.email = email
        user.role = user_data.role
        user.full_name = user_data.full_name
        return self._commit_update(user)

    def patch_user(self, user_id: int, user_data: UserPatch) -> User | None:
        user = self.repository.get_by_id(user_id)
        if user is None:
            return None

        update_data = user_data.model_dump(exclude_unset=True)
        if "email" in update_data and update_data["email"] is not None:
            email = str(update_data["email"]).strip().lower()
            if user.email != email and self.repository.get_by_email(email) is not None:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="Email already exists",
                )
            update_data["email"] = email

        for field_name, value in update_data.items():
            setattr(user, field_name, value)
        return self._commit_update(user)

    def delete_user(self, user_id: int) -> bool:
        user = self.repository.get_by_id(user_id)
        if user is None:
            return False
        try:
            self.repository.delete(user)
            self.db.commit()
            return True
        except Exception:
            self.db.rollback()
            raise

    def _commit_update(self, user: User) -> User:
        try:
            user = self.repository.update(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except Exception:
            self.db.rollback()
            raise
```


---

## `app/utils/helpers.py`

```python

```


---

## `app/utils/pagination.py`

```python

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

    user: "${UID}:${GID}"

    container_name: fastapi-api

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

## `docs/diary/2026-08-09-current-progress.md`

```markdown
# 📅 Development Diary — 2026-08-09

## Chủ đề
**Project Summary và nhìn lại toàn bộ hệ thống.**

Hôm nay tôi tạm dừng việc thêm feature để nhìn project như một hệ thống hoàn chỉnh.

Tôi tổng hợp lại request flow, architecture, database, Alembic, testing, Docker và những vấn đề còn tồn tại. Một nhận thức quan trọng là clean architecture không nằm ở số lượng folder; điều quan trọng là responsibility và dependency giữa các layer phải rõ ràng.

Tôi cũng giữ lại các lỗi đã gặp thay vì che chúng đi, vì debugging là một phần của quá trình học.

### Insight

> Một API “chạy được” chưa đồng nghĩa với một hệ thống mà tôi thực sự hiểu.

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

📓 [Development Log — 01/08](./2026-08-1-current-progress.md)

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
| [01/08](./2026-08-1-current-progress.md) | Repository thực hành sâu hơn |
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

## `docs/diary/2026-08-1-current-progress.md`

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

```python
@router.get("/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
```

Điều này hoạt động nhưng Router đang làm quá nhiều việc.

Router vừa:

- nhận HTTP Request
- truy vấn Database
- xử lý business logic
- trả Response

Khi project lớn lên thì Router sẽ rất dài và khó bảo trì.

---

# 2. Repository Pattern

Đã chuyển toàn bộ code thao tác Database sang

```
app/crud/user.py
```

Router chỉ còn nhiệm vụ:

- nhận Request
- gọi Repository
- trả Response

Ví dụ

```python
user = user_crud.get_user(db, user_id)
```

thay vì

```python
db.query(User)
```

---

# 3. CRUD đã được tách hoàn toàn

Đã thực hành:

### get_users()

```python
def get_users(...)
```

---

### get_user()

```python
def get_user(...)
```

---

### create_user()

```python
def create_user(...)
```

---

### update_user()

```python
def update_user(...)
```

---

### patch_user()

```python
def patch_user(...)
```

---

### delete_user()

```python
def delete_user(...)
```

---

# 4. Router trở nên rất ngắn

Router chỉ còn

```python
request
↓

repository

↓

response
```

Đây chính là mục tiêu của Repository Pattern.

---

# 5. PATCH

Đã thực hành endpoint

```
PATCH /users/{id}
```

với

```python
UserPatch
```

và

```python
exclude_unset=True
```

để chỉ cập nhật những field được gửi lên.

Ví dụ

```json
{
    "name": "New Name"
}
```

chỉ cập nhật

```
name
```

không ghi đè

```
email
age
...
```

---

# 6. PUT vs PATCH

Đã hiểu sự khác nhau.

PUT

```
Update toàn bộ Resource
```

PATCH

```
Update một phần Resource
```

---

# 7. Router không còn viết SQLAlchemy

Đây là thay đổi quan trọng nhất.

Router

❌ không còn

```python
db.query(...)
```

mà chỉ gọi

```python
user_crud....
```

---

# 8. Response vẫn giữ chuẩn

Toàn bộ endpoint đều trả về

```python
APIResponse
```

và

```python
response(...)
```

để Response luôn thống nhất.

---

# 9. HTTPException

Đã thực hành

```python
raise HTTPException(
    status_code=404,
    detail="User not found"
)
```

Repository trả về

```python
None
```

Router quyết định trả lỗi.

Điều này giúp Repository không phụ thuộc FastAPI.

---

# 10. Điều học được

Không phải Router càng nhiều code càng tốt.

Ngược lại.

Router càng mỏng càng đúng.

Business Logic

↓

Repository

HTTP

↓

Router

---

# 11. Kiến thức mới

Đã hiểu:

- Repository Pattern
- Separation of Concerns
- Single Responsibility Principle
- PATCH
- exclude_unset
- CRUD Layer
- HTTP Layer
- Database Layer

---

# 12. Cấu trúc project hiện tại

```
app/

    core/

    crud/

        user.py

    database.py

    dependencies.py

    models/

    routers/

        user.py

    schemas/

    utils/

        response.py
```

---

# 13. Những gì đã thực hành

✔ CRUD

✔ SQLAlchemy ORM

✔ Pydantic v2

✔ APIResponse

✔ Response Wrapper

✔ Dependency Injection

✔ Repository Pattern

✔ PATCH

✔ PUT

✔ Alembic

✔ Docker

✔ PostgreSQL

---

# 🇺🇸 English

## Today's Topic

Implemented the Repository Pattern in the FastAPI project.

The goal was not to add new features but to organize the project using a professional backend architecture.

---

## What was accomplished

- Moved all database operations into the Repository layer.
- Routers now only handle HTTP requests and responses.
- CRUD logic is centralized in `app/crud/user.py`.
- Added support for partial updates using PATCH.
- Used `exclude_unset=True` for safe partial updates.
- Kept API responses consistent through the response wrapper.
- Continued using Dependency Injection with SQLAlchemy sessions.
- Preserved clean separation between HTTP logic and database logic.

---

## Key Concepts Learned

- Repository Pattern
- Separation of Concerns
- Single Responsibility Principle
- Partial Update (PATCH)
- Full Update (PUT)
- CRUD Layer
- HTTP Layer
- Database Layer
- Clean FastAPI Architecture

---

## Current Project Structure

```
app/

    core/

    crud/

        user.py

    database.py

    dependencies.py

    models/

    routers/

        user.py

    schemas/

    utils/

        response.py
```

---

## Technologies Practiced

- FastAPI
- SQLAlchemy ORM
- PostgreSQL
- Docker
- Alembic
- Pydantic v2
- Repository Pattern
- Dependency Injection
- REST API Design
- PATCH & PUT Endpoints

---

# ✅ Current Status

The project now follows a much cleaner architecture than the initial version.

The Router layer is responsible only for HTTP communication.

The Repository layer manages all database operations.

This separation significantly improves readability, maintainability, testing, and scalability.

The project is now ready to move toward the next architectural layer, where business logic will be separated from the data access layer.
```


---

## `docs/diary/2026-08-10-current-progress.md`

```markdown
# 📅 Development Diary — 2026-08-10

> **Retrospective entry:** Không còn log nguyên bản đủ để xác nhận chính xác hoạt động trong ngày này.

Khoảng thời gian **10/08/2026 → 28/08/2026** được ghi nhận chung tại:

[Retrospective Learning Record](./2026-08-10-to-2026-08-28-retrospective-gap.md)

Tôi không muốn tự dựng một lịch sử giả cho ngày này.

### Bài học về documentation

```text
đã làm
≠
đã hiểu
≠
đã kiểm chứng
```

Từ đây diary sẽ được ghi dựa trên mục tiêu, thao tác thực tế, kết quả, lỗi, root cause và next step.
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

## `docs/diary/2026-08-11-current-progress.md`

```markdown
# 📅 Development Diary — 2026-08-11

> **Retrospective entry:** Không còn log nguyên bản đủ để xác nhận chính xác hoạt động trong ngày này.

Khoảng thời gian **10/08/2026 → 28/08/2026** được ghi nhận chung tại:

[Retrospective Learning Record](./2026-08-10-to-2026-08-28-retrospective-gap.md)

Tôi không muốn tự dựng một lịch sử giả cho ngày này.

### Bài học về documentation

```text
đã làm
≠
đã hiểu
≠
đã kiểm chứng
```

Từ đây diary sẽ được ghi dựa trên mục tiêu, thao tác thực tế, kết quả, lỗi, root cause và next step.
```


---

## `docs/diary/2026-08-12-current-progress.md`

```markdown
# 📅 Development Diary — 2026-08-12

> **Retrospective entry:** Không còn log nguyên bản đủ để xác nhận chính xác hoạt động trong ngày này.

Khoảng thời gian **10/08/2026 → 28/08/2026** được ghi nhận chung tại:

[Retrospective Learning Record](./2026-08-10-to-2026-08-28-retrospective-gap.md)

Tôi không muốn tự dựng một lịch sử giả cho ngày này.

### Bài học về documentation

```text
đã làm
≠
đã hiểu
≠
đã kiểm chứng
```

Từ đây diary sẽ được ghi dựa trên mục tiêu, thao tác thực tế, kết quả, lỗi, root cause và next step.
```


---

## `docs/diary/2026-08-13-current-progress.md`

```markdown
# 📅 Development Diary — 2026-08-13

> **Retrospective entry:** Không còn log nguyên bản đủ để xác nhận chính xác hoạt động trong ngày này.

Khoảng thời gian **10/08/2026 → 28/08/2026** được ghi nhận chung tại:

[Retrospective Learning Record](./2026-08-10-to-2026-08-28-retrospective-gap.md)

Tôi không muốn tự dựng một lịch sử giả cho ngày này.

### Bài học về documentation

```text
đã làm
≠
đã hiểu
≠
đã kiểm chứng
```

Từ đây diary sẽ được ghi dựa trên mục tiêu, thao tác thực tế, kết quả, lỗi, root cause và next step.
```


---

## `docs/diary/2026-08-14-current-progress.md`

```markdown
# 📅 Development Diary — 2026-08-14

> **Retrospective entry:** Không còn log nguyên bản đủ để xác nhận chính xác hoạt động trong ngày này.

Khoảng thời gian **10/08/2026 → 28/08/2026** được ghi nhận chung tại:

[Retrospective Learning Record](./2026-08-10-to-2026-08-28-retrospective-gap.md)

Tôi không muốn tự dựng một lịch sử giả cho ngày này.

### Bài học về documentation

```text
đã làm
≠
đã hiểu
≠
đã kiểm chứng
```

Từ đây diary sẽ được ghi dựa trên mục tiêu, thao tác thực tế, kết quả, lỗi, root cause và next step.
```


---

## `docs/diary/2026-08-15-current-progress.md`

```markdown
# 📅 Development Diary — 2026-08-15

> **Retrospective entry:** Không còn log nguyên bản đủ để xác nhận chính xác hoạt động trong ngày này.

Khoảng thời gian **10/08/2026 → 28/08/2026** được ghi nhận chung tại:

[Retrospective Learning Record](./2026-08-10-to-2026-08-28-retrospective-gap.md)

Tôi không muốn tự dựng một lịch sử giả cho ngày này.

### Bài học về documentation

```text
đã làm
≠
đã hiểu
≠
đã kiểm chứng
```

Từ đây diary sẽ được ghi dựa trên mục tiêu, thao tác thực tế, kết quả, lỗi, root cause và next step.
```


---

## `docs/diary/2026-08-16-current-progress.md`

```markdown
# 📅 Development Diary — 2026-08-16

> **Retrospective entry:** Không còn log nguyên bản đủ để xác nhận chính xác hoạt động trong ngày này.

Khoảng thời gian **10/08/2026 → 28/08/2026** được ghi nhận chung tại:

[Retrospective Learning Record](./2026-08-10-to-2026-08-28-retrospective-gap.md)

Tôi không muốn tự dựng một lịch sử giả cho ngày này.

### Bài học về documentation

```text
đã làm
≠
đã hiểu
≠
đã kiểm chứng
```

Từ đây diary sẽ được ghi dựa trên mục tiêu, thao tác thực tế, kết quả, lỗi, root cause và next step.
```


---

## `docs/diary/2026-08-17-current-progress.md`

```markdown
# 📅 Development Diary — 2026-08-17

> **Retrospective entry:** Không còn log nguyên bản đủ để xác nhận chính xác hoạt động trong ngày này.

Khoảng thời gian **10/08/2026 → 28/08/2026** được ghi nhận chung tại:

[Retrospective Learning Record](./2026-08-10-to-2026-08-28-retrospective-gap.md)

Tôi không muốn tự dựng một lịch sử giả cho ngày này.

### Bài học về documentation

```text
đã làm
≠
đã hiểu
≠
đã kiểm chứng
```

Từ đây diary sẽ được ghi dựa trên mục tiêu, thao tác thực tế, kết quả, lỗi, root cause và next step.
```


---

## `docs/diary/2026-08-18-current-progress.md`

```markdown
# 📅 Development Diary — 2026-08-18

> **Retrospective entry:** Không còn log nguyên bản đủ để xác nhận chính xác hoạt động trong ngày này.

Khoảng thời gian **10/08/2026 → 28/08/2026** được ghi nhận chung tại:

[Retrospective Learning Record](./2026-08-10-to-2026-08-28-retrospective-gap.md)

Tôi không muốn tự dựng một lịch sử giả cho ngày này.

### Bài học về documentation

```text
đã làm
≠
đã hiểu
≠
đã kiểm chứng
```

Từ đây diary sẽ được ghi dựa trên mục tiêu, thao tác thực tế, kết quả, lỗi, root cause và next step.
```


---

## `docs/diary/2026-08-19-current-progress.md`

```markdown
# 📅 Development Diary — 2026-08-19

> **Retrospective entry:** Không còn log nguyên bản đủ để xác nhận chính xác hoạt động trong ngày này.

Khoảng thời gian **10/08/2026 → 28/08/2026** được ghi nhận chung tại:

[Retrospective Learning Record](./2026-08-10-to-2026-08-28-retrospective-gap.md)

Tôi không muốn tự dựng một lịch sử giả cho ngày này.

### Bài học về documentation

```text
đã làm
≠
đã hiểu
≠
đã kiểm chứng
```

Từ đây diary sẽ được ghi dựa trên mục tiêu, thao tác thực tế, kết quả, lỗi, root cause và next step.
```


---

## `docs/diary/2026-08-20-current-progress.md`

```markdown
# 📅 Development Diary — 2026-08-20

> **Retrospective entry:** Không còn log nguyên bản đủ để xác nhận chính xác hoạt động trong ngày này.

Khoảng thời gian **10/08/2026 → 28/08/2026** được ghi nhận chung tại:

[Retrospective Learning Record](./2026-08-10-to-2026-08-28-retrospective-gap.md)

Tôi không muốn tự dựng một lịch sử giả cho ngày này.

### Bài học về documentation

```text
đã làm
≠
đã hiểu
≠
đã kiểm chứng
```

Từ đây diary sẽ được ghi dựa trên mục tiêu, thao tác thực tế, kết quả, lỗi, root cause và next step.
```


---

## `docs/diary/2026-08-21-current-progress.md`

```markdown
# 📅 Development Diary — 2026-08-21

> **Retrospective entry:** Không còn log nguyên bản đủ để xác nhận chính xác hoạt động trong ngày này.

Khoảng thời gian **10/08/2026 → 28/08/2026** được ghi nhận chung tại:

[Retrospective Learning Record](./2026-08-10-to-2026-08-28-retrospective-gap.md)

Tôi không muốn tự dựng một lịch sử giả cho ngày này.

### Bài học về documentation

```text
đã làm
≠
đã hiểu
≠
đã kiểm chứng
```

Từ đây diary sẽ được ghi dựa trên mục tiêu, thao tác thực tế, kết quả, lỗi, root cause và next step.
```


---

## `docs/diary/2026-08-22-current-progress.md`

```markdown
# 📅 Development Diary — 2026-08-22

> **Retrospective entry:** Không còn log nguyên bản đủ để xác nhận chính xác hoạt động trong ngày này.

Khoảng thời gian **10/08/2026 → 28/08/2026** được ghi nhận chung tại:

[Retrospective Learning Record](./2026-08-10-to-2026-08-28-retrospective-gap.md)

Tôi không muốn tự dựng một lịch sử giả cho ngày này.

### Bài học về documentation

```text
đã làm
≠
đã hiểu
≠
đã kiểm chứng
```

Từ đây diary sẽ được ghi dựa trên mục tiêu, thao tác thực tế, kết quả, lỗi, root cause và next step.
```


---

## `docs/diary/2026-08-23-current-progress.md`

```markdown
# 📅 Development Diary — 2026-08-23

> **Retrospective entry:** Không còn log nguyên bản đủ để xác nhận chính xác hoạt động trong ngày này.

Khoảng thời gian **10/08/2026 → 28/08/2026** được ghi nhận chung tại:

[Retrospective Learning Record](./2026-08-10-to-2026-08-28-retrospective-gap.md)

Tôi không muốn tự dựng một lịch sử giả cho ngày này.

### Bài học về documentation

```text
đã làm
≠
đã hiểu
≠
đã kiểm chứng
```

Từ đây diary sẽ được ghi dựa trên mục tiêu, thao tác thực tế, kết quả, lỗi, root cause và next step.
```


---

## `docs/diary/2026-08-24-current-progress.md`

```markdown
# 📅 Development Diary — 2026-08-24

> **Retrospective entry:** Không còn log nguyên bản đủ để xác nhận chính xác hoạt động trong ngày này.

Khoảng thời gian **10/08/2026 → 28/08/2026** được ghi nhận chung tại:

[Retrospective Learning Record](./2026-08-10-to-2026-08-28-retrospective-gap.md)

Tôi không muốn tự dựng một lịch sử giả cho ngày này.

### Bài học về documentation

```text
đã làm
≠
đã hiểu
≠
đã kiểm chứng
```

Từ đây diary sẽ được ghi dựa trên mục tiêu, thao tác thực tế, kết quả, lỗi, root cause và next step.
```


---

## `docs/diary/2026-08-25-current-progress.md`

```markdown
# 📅 Development Diary — 2026-08-25

> **Retrospective entry:** Không còn log nguyên bản đủ để xác nhận chính xác hoạt động trong ngày này.

Khoảng thời gian **10/08/2026 → 28/08/2026** được ghi nhận chung tại:

[Retrospective Learning Record](./2026-08-10-to-2026-08-28-retrospective-gap.md)

Tôi không muốn tự dựng một lịch sử giả cho ngày này.

### Bài học về documentation

```text
đã làm
≠
đã hiểu
≠
đã kiểm chứng
```

Từ đây diary sẽ được ghi dựa trên mục tiêu, thao tác thực tế, kết quả, lỗi, root cause và next step.
```


---

## `docs/diary/2026-08-26-current-progress.md`

```markdown
# 📅 Development Diary — 2026-08-26

> **Retrospective entry:** Không còn log nguyên bản đủ để xác nhận chính xác hoạt động trong ngày này.

Khoảng thời gian **10/08/2026 → 28/08/2026** được ghi nhận chung tại:

[Retrospective Learning Record](./2026-08-10-to-2026-08-28-retrospective-gap.md)

Tôi không muốn tự dựng một lịch sử giả cho ngày này.

### Bài học về documentation

```text
đã làm
≠
đã hiểu
≠
đã kiểm chứng
```

Từ đây diary sẽ được ghi dựa trên mục tiêu, thao tác thực tế, kết quả, lỗi, root cause và next step.
```


---

## `docs/diary/2026-08-27-current-progress.md`

```markdown
# 📅 Development Diary — 2026-08-27

> **Retrospective entry:** Không còn log nguyên bản đủ để xác nhận chính xác hoạt động trong ngày này.

Khoảng thời gian **10/08/2026 → 28/08/2026** được ghi nhận chung tại:

[Retrospective Learning Record](./2026-08-10-to-2026-08-28-retrospective-gap.md)

Tôi không muốn tự dựng một lịch sử giả cho ngày này.

### Bài học về documentation

```text
đã làm
≠
đã hiểu
≠
đã kiểm chứng
```

Từ đây diary sẽ được ghi dựa trên mục tiêu, thao tác thực tế, kết quả, lỗi, root cause và next step.
```


---

## `docs/diary/2026-08-28-current-progress.md`

```markdown
# 📅 Development Diary — 2026-08-28

> **Retrospective entry:** Không còn log nguyên bản đủ để xác nhận chính xác hoạt động trong ngày này.

Khoảng thời gian **10/08/2026 → 28/08/2026** được ghi nhận chung tại:

[Retrospective Learning Record](./2026-08-10-to-2026-08-28-retrospective-gap.md)

Tôi không muốn tự dựng một lịch sử giả cho ngày này.

### Bài học về documentation

```text
đã làm
≠
đã hiểu
≠
đã kiểm chứng
```

Từ đây diary sẽ được ghi dựa trên mục tiêu, thao tác thực tế, kết quả, lỗi, root cause và next step.
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

## `docs/diary/README.md`

```markdown
# FastAPI User Management — Development Diary
## 2026-08-30 → 2026-09-06

Bộ diary này nối tiếp `docs/diary/2026-08-30-current-progress.md` và ghi lại tiến trình đến hết ngày 06/09/2026.

## Files

```text
2026-08-30-current-progress.md
2026-08-31-current-progress.md
2026-09-01-current-progress.md
2026-09-02-current-progress.md
2026-09-03-current-progress.md
2026-09-04-current-progress.md
2026-09-05-current-progress.md
2026-09-06-current-progress.md
```

## Lưu ý về tính chính xác lịch sử

Các diary từ **30/08 đến 05/09** là bản **tái dựng liên tục từ project context và các trao đổi đã có**, vì các file diary riêng của những ngày này không có sẵn trong nguồn Library mà tôi có thể đọc tại thời điểm tạo gói.

Vì vậy chúng được viết để **nối mạch học tập và kỹ thuật**, không nên hiểu là commit history theo từng giờ.

File **2026-09-06-current-progress.md** được dựa trên diary 06/09 hiện có và kết quả test cuối ngày.

## Điểm tiếp tục

Tại cuối ngày 06/09:

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

E2E hiện đạt:

```text
3 passed, 2 warnings
```
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

## `pytest.ini`

```ini
[pytest]
python_files = test_*.py

python_classes = Test*

python_functions = test_*

addopts =
    -v
    --tb=short
    --html=tests/reports/report.html
    --self-contained-html

testpaths =
    tests
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
fastapi==0.116.1
uvicorn==0.35.0

sqlalchemy==2.0.43
psycopg2-binary==2.9.10

pydantic==2.11.7
email-validator==2.2.0

passlib[bcrypt]==1.7.4
bcrypt==4.1.3
pydantic-settings==2.10.1
python-jose[cryptography]==3.5.0
requests==2.32.4
python-dotenv==1.1.1
python-multipart==0.0.32
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

## `tests/api/test_auth.py`

```python
def test_login_success(client):
    create_response = client.post(
        "/users/",
        json={
            "name": "loginuser",
            "email": "login@example.com",
            "password": "123456",
            "full_name": "Login User",
        },
    )

    assert create_response.status_code == 201

    response = client.post(
        "/auth/login",
        data={
            "username": "login@example.com",
            "password": "123456",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_login_wrong_password(client):
    client.post(
        "/users/",
        json={
            "name": "loginuser",
            "email": "wrong-password@example.com",
            "password": "123456",
            "full_name": "Wrong Password",
        },
    )

    response = client.post(
        "/auth/login",
        data={
            "username": "wrong-password@example.com",
            "password": "wrong-password",
        },
    )

    assert response.status_code == 401


def test_login_unknown_user(client):
    response = client.post(
        "/auth/login",
        data={
            "username": "notfound@example.com",
            "password": "123456",
        },
    )

    assert response.status_code == 401
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

## `tests/api/test_users.py`

```python
def test_get_users(auth_client):
    response = auth_client.get("/users/")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "success"
    assert isinstance(data["data"], list)


def test_get_users_unauthorized(client):
    response = client.get("/users/")

    assert response.status_code == 401

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
    assert data["data"]["name"] == "testuser"
    assert data["data"]["email"] == "testuser@example.com"
    assert data["data"]["role"] == "user"
    assert data["data"]["full_name"] == "Test User"

    assert "password" not in data["data"]


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

    assert first_response.status_code == 201

    second_response = client.post(
        "/users/",
        json=payload,
    )

    assert second_response.status_code == 409
    assert second_response.json()["detail"] == "Email already exists"


def test_create_user_invalid_password(client):
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
```


---

## `tests/conftest.py`

```python
import pytest

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from app.core.security import hash_password
from app.models import User
from app.database import Base
from app.dependencies import get_db
from app.main import app


SQLALCHEMY_DATABASE_URL = "sqlite://"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


@pytest.fixture(scope="function")
def db_session():
    Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()

    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def client(db_session):
    def override_get_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()


@pytest.fixture
def auth_client(client):
    response = client.post(
        "/users/",
        json={
            "name": "pytestuser",
            "email": "pytest-auth@example.com",
            "password": "123456",
            "full_name": "Pytest Auth User",
        },
    )

    assert response.status_code == 201

    login_response = client.post(
        "/auth/login",
        data={
            "username": "pytest-auth@example.com",
            "password": "123456",
        },
    )

    assert login_response.status_code == 200

    token = login_response.json()["access_token"]

    client.headers.update(
        {
            "Authorization": f"Bearer {token}",
        }
    )

    return client

@pytest.fixture(scope="function")
def auth_client(client, db_session):
    admin = User(
        name="testadmin",
        email="testadmin@example.com",
        role="admin",
        password=hash_password("123456"),
        full_name="Test Admin",
    )

    db_session.add(admin)
    db_session.commit()

    response = client.post(
        "/auth/login",
        data={
            "username": "testadmin@example.com",
            "password": "123456",
        },
    )

    assert response.status_code == 200

    token = response.json()["access_token"]

    client.headers.update({
        "Authorization": f"Bearer {token}"
    })

    yield client

    client.headers.pop("Authorization", None)
```


---

## `tests/e2e/__init__.py`

```python

```


---

## `tests/e2e/test_swagger_auth.py`

```python

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
    field = endpoint.locator(
        f'input[name="{field_name}"]'
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
