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