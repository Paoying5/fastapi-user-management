# 📅 Development Diary — 2026-09-05

## Chủ đề
**Playwright E2E và automated screenshot evidence cho Swagger UI.**

---

## 1. Playwright

Bắt đầu sử dụng Playwright để kiểm tra Swagger UI bằng Firefox.

```text
Firefox
   ↓
Swagger UI
   ↓
API endpoint
   ↓
Response
   ↓
Screenshot evidence
```

---

## 2. E2E test

Tạo:

```text
tests/e2e/test_swagger_capture.py
tests/e2e/utils.py
```

Thêm:

```text
tests/__init__.py
tests/e2e/__init__.py
```

---

## 3. Helper

Các thao tác chung:

```text
open_swagger()
get_post_endpoint()
click_try_it_out()
click_execute()
fill_request_body()
screenshot()
```

Mục tiêu là giảm code lặp và giữ test dễ đọc.

---

## 4. Screenshot evidence

```text
tests/screenshots/
├── 01_swagger_home.png
├── 02_swagger_endpoints.png
└── 03_swagger_create_user_success.png
```

Hai screenshot đầu được kiểm tra và xác nhận giao diện giống Swagger UI khi mở thủ công bằng Firefox.

---

## 5. POST /users/

```text
Open Swagger
    ↓
POST /users/
    ↓
Try it out
    ↓
Fill request body
    ↓
Execute
    ↓
Check 201
    ↓
Check response body
    ↓
Screenshot
```

---

## 6. Điểm dừng

Workflow tiếp theo:

```text
POST /users/
    ↓
POST /auth/login
    ↓
Authorize
    ↓
POST /posts/
    ↓
GET /posts/{post_id}
    ↓
PATCH /posts/{post_id}
    ↓
DELETE /posts/{post_id}
```

Authentication và Posts E2E chưa hoàn thiện.
