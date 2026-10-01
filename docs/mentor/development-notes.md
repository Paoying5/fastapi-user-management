# Development Notes — FastAPI User Management

## 1. Mục đích

Tài liệu này ghi lại các lệnh thường dùng để chạy dự án FastAPI bằng Docker Compose, kiểm tra PostgreSQL, chạy test và xử lý lỗi Firefox khi chạy E2E test.

## 2. Khởi động dự án

Mở Terminal tại thư mục gốc `fastapi-user-management`.

Khởi động container:

`docker compose up -d`

Nếu vừa thay đổi Dockerfile hoặc cấu hình cần build lại:

`docker compose up --build -d`

Kiểm tra trạng thái container:

`docker compose ps`

Kiểm tra API:

`curl http://localhost:8000/health`

Kết quả mong đợi là API báo `healthy` và database báo `connected`.

## 3. Các lệnh Docker thường dùng

- `docker compose logs api` — xem log API.
- `docker compose logs -f api` — theo dõi log API liên tục.
- `docker compose logs postgres` — xem log PostgreSQL.
- `docker compose exec api sh` — mở shell trong container API.
- `docker compose exec api id` — xem user đang chạy trong container.
- `docker compose down` — dừng và xóa container/network của Compose.
- `docker compose up --build -d` — build image và chạy lại container.

**Lưu ý:** Không dùng `docker compose down -v` nếu không có chủ đích xóa volume. Volume `postgres_data` chứa dữ liệu PostgreSQL của dự án.

## 4. Chạy kiểm thử

Chạy toàn bộ API tests:

`docker compose exec -e PYTHONPATH=/app api pytest -q tests/api`

Chạy E2E tests với Firefox:

`docker compose exec -e PYTHONPATH=/app api pytest -q tests/e2e --browser firefox`

Chạy toàn bộ API và E2E tests kèm coverage:

`docker compose exec -e PYTHONPATH=/app api pytest -q tests/api tests/e2e --browser firefox --cov=app --cov-report=term-missing --cov-report=html`

- `-q`: output ngắn gọn.
- `--browser firefox`: chọn Firefox cho E2E.
- `--cov=app`: đo coverage cho package `app`.
- `--cov-report=term-missing`: hiển thị coverage và các dòng chưa được kiểm thử.
- `--cov-report=html`: tạo báo cáo HTML trong `htmlcov/`.

## 5. Lỗi Firefox sandbox trong Docker

### Hiện tượng

Firefox không khởi động khi chạy Playwright. Log có thông báo:

`Sandbox: CanCreateUserNamespace() clone() failure: EPERM`

Lệnh kiểm tra namespace trong container mặc định cũng trả về `Operation not permitted`.

### Nguyên nhân đã xác minh

Container mặc định bị chặn thao tác tạo user namespace. Khi thử một container tạm với `seccomp=unconfined`, lệnh `unshare -Ur true` chạy thành công. Sau khi cấu hình `seccomp:unconfined` cho service API trong môi trường phát triển, Firefox khởi động thành công và 9 E2E tests đã PASS.

### Cấu hình hiện tại

Service `api` dùng `security_opt` với `seccomp:unconfined`. Cấu hình này làm giảm mức bảo vệ seccomp của container, vì vậy chỉ nên dùng trong môi trường local development/E2E đã kiểm soát, không mặc định đưa vào production.

Container API hiện chạy bằng root vì cấu hình `user: "${UID}:${GID}"` đã được bỏ để kiểm tra và xử lý lỗi. Cần xem xét lại quyền chạy container và cách tách cấu hình E2E/dev khỏi cấu hình production trước khi triển khai.

### Kiểm tra Firefox

`docker compose exec api python -c "from playwright.sync_api import sync_playwright; p=sync_playwright().start(); b=p.firefox.launch(headless=True); print('Firefox launch OK'); b.close(); p.stop()"`

Kết quả đã quan sát: `Firefox launch OK`.

Kiểm tra namespace:

`docker compose exec api sh -c 'unshare -Ur true; echo exit_code=$?'`

Sau khi áp dụng cấu hình hiện tại, kết quả đã quan sát: `exit_code=0`.

## 6. Kết quả E2E gần nhất

Ngày ghi nhận: 2026-10-02

Lệnh chạy:

`docker compose exec -e PYTHONPATH=/app api pytest -q tests/e2e --browser firefox`

Kết quả: **9 passed in 26.45s**.

Đây là kết quả E2E; cần chạy lại toàn bộ API và E2E tests để xác nhận trạng thái hiện tại của toàn dự án.

## 7. Quy trình sau khi thay đổi code hoặc cấu hình

1. Xác định file đã thay đổi và lý do.
2. Nếu thay đổi Dockerfile hoặc cấu hình Compose, build/chạy lại container khi cần.
3. Kiểm tra `docker compose ps` và `/health`.
4. Chạy test phù hợp với phần vừa thay đổi.
5. Chạy toàn bộ test và coverage trước khi chốt một mốc hoàn thành.
6. Cập nhật tài liệu này nếu có lệnh, cấu hình hoặc cách xử lý lỗi mới.

## 8. Ghi chú học NumPy, Pandas và Matplotlib

Mục tiêu tiếp theo là học và thực hành phân tích dữ liệu dựa trên dữ liệu users và posts của chính dự án.

- **Pandas:** tạo DataFrame, lọc dữ liệu, `value_counts`, `groupby`, `merge`, xử lý giá trị thiếu.
- **NumPy:** tính mean, median, min, max và standard deviation.
- **Matplotlib:** trực quan hóa số lượng users, phân bố độ tuổi và số posts theo user/role.

Nên thực hành từng chủ đề trong notebook trước, sau đó chuyển các hàm đã hiểu rõ vào thư mục `analytics/` và tích hợp vào FastAPI khi có mục đích cụ thể.

Không cần tạo dữ liệu giả khổng lồ ngay từ đầu. Hãy bắt đầu với dữ liệu users/posts hiện có và kiểm tra các trường hợp DataFrame rỗng hoặc dữ liệu thiếu.

