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