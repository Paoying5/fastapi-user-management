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