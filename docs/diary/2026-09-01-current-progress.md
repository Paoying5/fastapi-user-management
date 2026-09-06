# 📅 Development Diary — 2026-09-01

## Chủ đề
**Authentication, dependency injection và request flow.**

---

## 1. Authentication flow

```text
POST /auth/login
      ↓
Authenticate user
      ↓
Create JWT
      ↓
Bearer token
      ↓
Protected endpoint
```

---

## 2. Current user

`get_current_user()` đọc Bearer token, decode JWT, lấy `sub`, tìm user theo email và từ chối token/user không hợp lệ.

---

## 3. Dependency Injection

Các service được tạo thông qua dependency:

```text
get_db()
   ↓
get_user_service()
get_post_service()
get_auth_service()
```

Router không tự tạo database session hoặc service bằng logic thủ công.

---

## 4. Ownership

```text
JWT
 ↓
get_current_user()
 ↓
current_user.id
 ↓
PostService
 ↓
ownership check
```

Các endpoint Post protected phải kiểm tra ownership.

---

## 5. Bài học

Authentication không chỉ là tạo token; cần kiểm tra toàn bộ đường đi của token từ request đến business logic và database.
