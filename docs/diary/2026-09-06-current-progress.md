# 📅 Development Diary — 2026-09-06

## Chủ đề
**Playwright E2E, Swagger UI và Docker environment persistence.**

Hôm nay tiếp tục phần Testing của project FastAPI User Management, tập trung vào việc chạy E2E test bằng Playwright trên Firefox và đảm bảo môi trường Playwright không bị mất sau khi `docker compose down`.

---

## 1. Playwright E2E

Project hiện có:

```text
tests/
├── api/
├── e2e/
│   ├── __init__.py
│   ├── test_swagger_capture.py
│   └── utils.py
├── screenshots/
└── reports/
```

Đã thêm `tests/__init__.py` và `tests/e2e/__init__.py`.

---

## 2. Swagger UI

E2E test sử dụng Firefox để mở:

```text
http://api:8000/docs
```

Đã kiểm tra Swagger UI, OpenAPI document, API title và các endpoint chính `/health`, `/auth/login`, `/users/`, `/posts/`. Swagger UI cũng có thể tìm và thao tác với POST `/users/`.

Helper dùng chung được tách vào `tests/e2e/utils.py`:

```text
open_swagger()
get_post_endpoint()
click_try_it_out()
click_execute()
fill_request_body()
screenshot()
```

---

## 3. Screenshot evidence

```text
tests/screenshots/
├── 01_swagger_home.png
├── 02_swagger_endpoints.png
└── 03_swagger_create_user_success.png
```

Hai screenshot đầu được kiểm tra và xác nhận giao diện giống Swagger UI khi mở thủ công bằng Firefox tại `http://127.0.0.1:8000/docs#/`.

Screenshot thứ ba ghi lại kết quả thành công của POST `/users/`.

---

## 4. Firefox bị mất sau khi recreate container

Ban đầu Playwright báo:

```text
BrowserType.launch:
Executable doesn't exist at
/root/.cache/ms-playwright/firefox-1538/firefox/firefox
```

Firefox trước đó được cài thủ công bằng:

```bash
docker compose exec api playwright install firefox
```

Browser nằm trong container đang chạy. Sau `docker compose down`, container cũ bị remove nên browser binary cũng mất.

---

## 5. Đưa Firefox vào Dockerfile

Để môi trường E2E reproducible, thêm:

```dockerfile
RUN playwright install --with-deps firefox
```

`--with-deps` cần thiết vì Firefox còn cần các system libraries để chạy.

---

## 6. Kiểm tra Docker image

Đã chạy:

```bash
docker compose up --build -d
docker compose down
docker compose up -d
```

Sau đó:

```bash
docker compose exec api playwright install --list
```

Kết quả:

```text
Playwright version: 1.62.0

Browsers:
    /root/.cache/ms-playwright/ffmpeg-1011
    /root/.cache/ms-playwright/firefox-1538
```

Điều này xác nhận Firefox nằm trong môi trường container được tạo từ Docker image.

---

## 7. E2E test cuối ngày

Đã chạy:

```bash
docker compose exec -e PYTHONPATH=/app api pytest -q tests/e2e --browser firefox
```

Kết quả:

```text
collected 3 items
tests/e2e/test_swagger_capture.py ... [100%]

3 passed, 2 warnings in 6.70s
```

Tests:

```text
✅ test_swagger_health
✅ test_swagger_openapi
✅ test_swagger_create_user
```

2 warnings là deprecation warning từ Starlette/AnyIO và Passlib/crypt; không phải test failure.

---

## 8. Trạng thái cuối ngày

```text
FastAPI
   ↓
Docker Compose
   ↓
PostgreSQL
   ↓
Alembic
   ↓
Pytest API
   ↓
Playwright E2E
   ↓
Firefox
   ↓
Swagger UI
   ↓
Screenshot evidence
```

Các phần quan trọng đang hoạt động:

- ✅ FastAPI
- ✅ PostgreSQL
- ✅ Docker Compose
- ✅ Alembic
- ✅ API tests
- ✅ Swagger UI
- ✅ Playwright
- ✅ Firefox
- ✅ Automated screenshot
- ✅ E2E test
- ✅ Docker image chứa Firefox
- ✅ Firefox không còn phụ thuộc vào việc cài thủ công trong container hiện tại

---

## 9. Điểm dừng hôm nay

```text
Swagger UI
    ↓
POST /users/
    ↓
Playwright
    ↓
Firefox
    ↓
3 E2E tests PASS
```

Chưa tiếp tục sang toàn bộ workflow authentication và Posts.

Phần tiếp theo:

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
      ↓
Screenshot evidence
```

---

## 📌 Commands đã xác nhận hoạt động

```bash
docker compose up --build -d
docker compose down
docker compose up -d
docker compose exec api playwright install --list
docker compose exec -e PYTHONPATH=/app api pytest -q tests/e2e --browser firefox
```

Kết quả cuối ngày:

```text
3 passed, 2 warnings
```

---

## ❤️ Ghi chú

> **Environment cũng là một phần của project.**

Không chỉ source code cần đúng. Browser, system dependencies, Python packages và Docker image cũng phải được quản lý để test có thể chạy ổn định sau khi container được tạo lại.

Bài học này nối tiếp nguyên tắc lớn của project: **tách code chỉ là bước đầu; điều khó hơn là giữ source code, dependency, migration, database schema, test và runtime environment đồng bộ.**
