# 🚀 FastAPI User Management — Learning Journey

> **Một tài liệu duy nhất dành cho mentor:** nếu chị chỉ muốn xem nhanh quá trình học, kiến trúc, những gì đã làm, những lỗi đã gặp và những gì tôi đang học tiếp, chỉ cần mở file này.
>
> **Khoảng thời gian:** 28/07/2026 → 09/08/2026
>
> Nhật ký 02/08–08/08 được tổng hợp lại từ source code, migration, test và các trao đổi trong quá trình học. Vì đây là bản tổng hợp lại sau quá trình refactor, một số ngày phản ánh **milestone học tập** hơn là một danh sách commit theo giờ.

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
- Git workflow
- Debugging theo log và database state

Điểm quan trọng nhất của project không phải là “code càng nhiều càng tốt”, mà là hiểu **một request đi qua hệ thống như thế nào**.

---

# 🗺 2. Hành trình học tập

## 28/07 — Nền tảng project

Project đã có các chức năng backend chính:

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

📓 [Development Log 01 — 28/07](./2026-07-28-current-progress.md)

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

Điều tôi hiểu được là SQLAlchemy không thay thế SQL. Nó là cách xây dựng query bằng Python nhưng cuối cùng PostgreSQL vẫn thực thi SQL.

📓 [Development Log 02 — 29/07](./2026-07-29-current-progress.md)

---

## 30/07 — Docker và Alembic

Tôi học sâu hơn về:

- Docker image/container/network/volume
- Docker BuildKit
- `.dockerignore`
- `requirements-dev.txt`
- healthcheck
- Alembic
- migration history
- `upgrade()` / `downgrade()`

Một bài học quan trọng: `Base.metadata.create_all()` không phải là cách quản lý schema migration lâu dài. Alembic được đưa vào để version-control database schema.

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

Tôi học được Repository không nên chứa HTTP logic, response hoặc business rule.

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

Đây cũng là lúc tôi nhận ra rằng refactor architecture không chỉ là “tách file”. Các dependency/import cũ phải được dọn và request flow phải được kiểm tra lại.

📓 [Development Log — 01/08](./2026-08-1-current-progress.md)

---

## 02/08 → 04/08 — Architecture, Service, Model và Schema

Tôi củng cố kiến trúc nhiều tầng:

```text
Router
   ↓
Service
   ↓
Repository / CRUD
   ↓
SQLAlchemy
   ↓
PostgreSQL
```

Đồng thời học rõ hơn sự khác nhau giữa:

- SQLAlchemy Model
- Pydantic Schema
- UserCreate
- UserUpdate
- UserPatch
- UserResponse

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

Project có các nhóm test:

```text
tests/api
tests/swagger
tests/e2e
```

Tôi học cách đọc status code, response body và server log khi test fail.

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

Healthcheck chỉ chứng minh endpoint health hoạt động, không chứng minh toàn bộ business API đúng.

📓 [Diary — 06/08](./2026-08-06-current-progress.md)

---

## 07/08 — `full_name` và Alembic

User model/schema được bổ sung `full_name`.

Migration mới:

```text
5614567ad165_add_full_name
```

kế thừa:

```text
e122a64acbc0
```

Đây là bước rất hữu ích để hiểu rằng:

```text
Model change
      ≠
Migration exists
      ≠
Database changed correctly
```

📓 [Diary — 07/08](./2026-08-07-current-progress.md)

---

## 08/08 — Debugging database mismatch

Một lỗi thực tế xuất hiện:

```text
500 Internal Server Error
```

Log chỉ ra:

```text
psycopg2.errors.UndefinedColumn:
column users.full_name does not exist
```

SQLAlchemy đang query `users.full_name`, trong khi PostgreSQL table thực tế chưa có column đó.

Đây là một trong những bài học thực tế nhất của project: **source code, migration history và database schema phải đồng bộ với nhau.**

📓 [Diary — 08/08](./2026-08-08-current-progress.md)

---

# 🏗 3. Kiến trúc hiện tại

Project hiện được tổ chức thành các khu vực:

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
```

Ngoài ra:

```text
alembic/
tests/
scripts/
Dockerfile
docker-compose.yml
```

### Vai trò chính

| Layer | Vai trò |
|---|---|
| `routers/` | HTTP endpoints, request/response |
| `schemas/` | Pydantic validation + API contract |
| `models/` | SQLAlchemy ORM models |
| `services/` | Business logic / orchestration |
| `repositories/` | Data access abstraction |
| `crud/` | Database operations còn tồn tại trong code hiện tại |
| `core/` | Configuration, security, exceptions, logging |
| `utils/` | Helper / response / pagination / validation |
| `alembic/` | Database migration history |
| `tests/` | API, Swagger và E2E tests |

---

# 🔐 4. Những chức năng đã học/thực hành

## User

- Create
- Read all
- Read by ID
- Update
- Patch
- Delete
- Email validation
- Password hashing
- Role

## Authentication

- JWT
- OAuth2 Password Flow
- Login
- Protected endpoints
- Current user
- Password hashing

## Post

- CRUD
- Foreign key
- User–Post relationship
- Current user's posts

## Query

- filtering
- `ILIKE`
- `AND`
- `OR`
- `IN`
- `BETWEEN`
- `COUNT`
- ordering
- relationship loading

---

# 🐳 5. Docker workflow

Các thành phần chính:

```text
FastAPI container
       │
       │ Docker network
       ↓
PostgreSQL container
```

Một số lệnh đã thực hành:

```bash
docker compose up
docker compose up --build
docker compose down
docker compose ps
docker compose logs api
docker compose exec api ...
```

Tôi cũng học cách phân biệt lỗi Docker infrastructure với lỗi application/database.

---

# 🗄 6. Database và Alembic

Database sử dụng PostgreSQL 16.

Migration chain hiện có:

```text
e122a64acbc0
      ↓
5614567ad165
```

Trong quá trình học đã gặp một case rất quan trọng: migration `5614567ad165_add_full_name.py` hiện tại trong source archive có `upgrade()`/`downgrade()` để `pass`, trong khi model đã có `full_name`.

Đây chính là lý do database thực tế có thể không có column `full_name` dù application code đã tham chiếu đến nó.

**Tôi ghi lại điều này ở đây có chủ đích:** project chưa được coi là “hoàn hảo”. Mentor có thể nhìn thấy cả lỗi và cách tôi học cách tìm lỗi.

---

# 🧪 7. Testing

Project có:

```text
tests/api/
tests/swagger/
tests/e2e/
```

Ví dụ test API:

```text
GET /users
POST /users
GET /health
```

Một test hiện đã phát hiện lỗi thật:

```text
STATUS = 500
```

thay vì:

```text
200
```

và traceback giúp xác định root cause là database schema mismatch.

Đây là một kết quả học tập tốt: test không chỉ dùng để “chứng minh code đúng”, mà còn giúp **tìm ra code và database đang không đồng bộ**.

---

# 🧠 8. Những bài học lớn nhất

## 1. Clean architecture không phải là nhiều folder

Tách thành:

```text
routers/
services/
repositories/
crud/
```

chưa có nghĩa architecture sạch.

Các layer phải có trách nhiệm rõ ràng và dependency phải nhất quán.

---

## 2. Model và database phải đồng bộ

Nếu Model có:

```python
full_name
```

nhưng database không có:

```sql
full_name
```

thì request có thể trả `500`.

---

## 3. Migration phải là code thực thi được

File migration tồn tại nhưng `upgrade()` là `pass` thì schema không thay đổi.

---

## 4. Docker healthy không có nghĩa application hoàn hảo

Healthcheck chỉ kiểm tra một phần rất nhỏ của hệ thống.

---

## 5. Test giúp học debugging

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

# ⚠️ 9. Trạng thái hiện tại và những điểm chưa hoàn thiện

Tôi muốn giữ phần này rõ ràng để mentor có thể đánh giá đúng quá trình học.

### Đang cần tiếp tục xử lý

- Đồng bộ `User.full_name` với PostgreSQL bằng migration thực sự.
- Dọn các import/code cũ còn sót sau quá trình refactor.
- Chọn một data-access architecture nhất quán thay vì cùng tồn tại `crud/` và `repositories/` nếu không có lý do rõ ràng.
- Hoàn thiện Service Layer và cho Router gọi Service nhất quán.
- Hoàn thiện test coverage cho CRUD, auth và posts.
- Kiểm tra lại toàn bộ migration từ database sạch.
- Dọn warning về `UID` / `GID` trong Docker Compose nếu chúng không được cấu hình.

Đây không phải danh sách “thất bại”. Đây là **backlog học tập** sau khi project đã được kiểm tra kỹ hơn.

---

# 📚 10. Tôi đã học được gì từ project này?

Nếu tóm tắt thành một câu:

> **Tôi đang học cách biến một API “chạy được” thành một hệ thống mà tôi có thể giải thích được request flow, database flow, migration flow, testing flow và debugging flow.**

Cụ thể hơn, tôi đã đi qua các bước:

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

---

# 🎯 11. Next Steps

Thứ tự ưu tiên tôi đề xuất cho chính mình:

### 1. Fix database migration

Đảm bảo migration `full_name` thực sự thay đổi database.

### 2. Test từ database sạch

Không dựa vào database cũ đã được thao tác thủ công.

### 3. Chọn architecture cuối cùng

Quyết định rõ:

```text
Router
 ↓
Service
 ↓
Repository
 ↓
Database
```

và loại bỏ code cũ không còn sử dụng.

### 4. Chạy toàn bộ test

Không chỉ một test `GET /users`.

### 5. Review lại project tree

Kiểm tra import, dependency và duplicate logic.

### 6. Sau đó mới tiếp tục feature mới

Tôi muốn ưu tiên **ổn định và hiểu code** trước khi thêm nhiều tính năng.

---

# 👩‍🏫 12. Mentor có thể xem project theo cách nhanh nhất

Nếu chỉ có vài phút, hãy đọc theo thứ tự:

1. **File này** — tổng quan toàn bộ hành trình.
2. `app/routers/` — API layer.
3. `app/services/` — business logic.
4. `app/repositories/` + `app/crud/` — xem quá trình refactor và phần đang cần thống nhất.
5. `app/models/` + `app/schemas/` — database/API contract.
6. `alembic/versions/` — database evolution.
7. `tests/` — cách tôi kiểm tra hệ thống.
8. `docs/diary/` — nhật ký chi tiết theo ngày.

---

# 🔗 13. Diary Index

| Ngày | Nội dung |
|---|---|
| [28/07](./2026-07-28-current-progress.md) | Project baseline và các feature ban đầu |
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
Hiểu kiến trúc
 ↓
Refactor
 ↓
Test lại
 ↓
Rút kinh nghiệm
```

Đó chính là phần giá trị nhất tôi nhận được từ project FastAPI này.
