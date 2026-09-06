# 📅 Development Diary — 2026-08-31

## Chủ đề
**Hoàn thiện User schema, password handling và response model.**

---

## 1. User schema

Tiếp tục kiểm tra `UserCreate`, `UserUpdate`, `UserPatch` và `UserResponse`.

`full_name` được bổ sung để hỗ trợ tạo và cập nhật đầy đủ thông tin user.

---

## 2. Password

Nguyên tắc:

```text
UserCreate.password
        ↓
Password hashing
        ↓
User.password
        ↓
Database
```

Password không được đưa vào `UserResponse`.

---

## 3. PUT và PATCH

PUT cập nhật resource theo schema đầy đủ. PATCH chỉ cập nhật field được gửi lên.

Ý tưởng quan trọng:

```python
model_dump(exclude_unset=True)
```

để tránh ghi đè field không được gửi.

---

## 4. Bài học

Schema là boundary kiểm soát dữ liệu đi vào và đi ra khỏi API, không chỉ đơn thuần là khai báo kiểu dữ liệu.
