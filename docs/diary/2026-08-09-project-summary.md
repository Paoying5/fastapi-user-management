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
