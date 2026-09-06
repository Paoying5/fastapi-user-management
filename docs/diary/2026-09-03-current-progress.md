# 📅 Development Diary — 2026-09-03

## Chủ đề
**API testing bằng pytest.**

---

## 1. Test structure

```text
tests/
├── api/
├── e2e/
├── screenshots/
└── reports/
```

Bắt đầu chuyển trọng tâm từ manual Swagger testing sang automated testing.

---

## 2. API tests

Các nhóm được kiểm tra:

```text
test_users.py
test_auth.py
test_create_user.py
test_health.py
test_posts.py
```

Tập trung vào status code, response body, validation, authentication, authorization, ownership và CRUD behavior.

---

## 3. Post API

Kiểm tra các endpoint create, list, search, current-user posts, get by ID, update, patch và delete.

Ownership được kiểm tra để user không thể sửa/xóa post của user khác.

---

## 4. Bài học

Test cần kiểm tra behavior thực tế của API, không chỉ kiểm tra `200 OK`.
