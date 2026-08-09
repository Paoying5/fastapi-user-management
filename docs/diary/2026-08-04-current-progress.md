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
