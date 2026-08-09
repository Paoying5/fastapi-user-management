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
