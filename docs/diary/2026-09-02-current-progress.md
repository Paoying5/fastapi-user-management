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
