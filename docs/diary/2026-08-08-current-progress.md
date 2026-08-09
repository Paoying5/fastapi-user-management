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
