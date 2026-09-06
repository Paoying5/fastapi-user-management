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
