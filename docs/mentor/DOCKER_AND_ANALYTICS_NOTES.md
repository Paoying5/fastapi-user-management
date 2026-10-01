# FastAPI User Management --- Docker, Testing và Analytics Notes

## 1. Trạng thái đã xác nhận

-   Docker Compose khởi động được API và PostgreSQL.
-   Firefox chạy được trong container API.
-   Playwright E2E: **9 passed** với `tests/e2e --browser firefox`.
-   API health endpoint trước đó trả về
    `{"status":"healthy","api":"running","database":"connected"}`.
-   PostgreSQL dùng named volume `postgres_data`. Không xóa volume khi
    chỉ restart/rebuild ứng dụng.

> `security_opt: - seccomp:unconfined` đã giúp Firefox tạo user
> namespace trong môi trường local. Cấu hình này làm giảm mức cô lập bảo
> mật; chỉ dùng cho development/E2E đáng tin cậy, không dùng làm cấu
> hình production.

## 2. Các lệnh Docker thường dùng

Chạy tại thư mục gốc dự án, nơi có `docker-compose.yml`:

``` bash
docker compose ps
docker compose up -d
docker compose up --build -d
docker compose logs -f api
docker compose logs -f postgres
curl http://localhost:8000/health
docker compose exec api sh
docker compose exec api id
docker compose down
```

`docker compose down` thông thường giữ named volume. Tránh
`docker compose down -v` nếu muốn giữ dữ liệu PostgreSQL.

## 3. Kiểm tra Firefox / Playwright

``` bash
docker compose exec api playwright --version
docker compose exec api python -c "from playwright.sync_api import sync_playwright; p=sync_playwright().start(); b=p.firefox.launch(headless=True); print('Firefox launch OK'); b.close(); p.stop()"
docker compose exec api sh -c 'unshare -Ur true; echo exit_code=$?'
```

Nếu Firefox báo `Firefox launch OK`, browser khởi chạy được. Nếu gặp
`CanCreateUserNamespace() clone() failure: EPERM`, kiểm tra Docker
security trước khi cài lại browser hoặc sửa code.

## 4. Chạy kiểm thử

### API tests

``` bash
docker compose exec -e PYTHONPATH=/app api pytest -q tests/api
```

### E2E tests với Firefox

``` bash
docker compose exec \
  -e PYTHONPATH=/app \
  api pytest -q tests/e2e \
  --browser firefox
```

### Toàn bộ API + E2E và coverage

``` bash
docker compose exec \
  -e PYTHONPATH=/app \
  api pytest -q \
  tests/api tests/e2e \
  --browser firefox \
  --cov=app \
  --cov-report=term-missing \
  --cov-report=html
```

Đọc số test pass/fail và coverage ở terminal. Báo cáo HTML được tạo tại
`htmlcov/`; với bind mount `.:/app`, thư mục này cũng xuất hiện trên máy
host.

Nếu test lỗi: 1. Đọc lỗi đầu tiên có ý nghĩa. 2. Nếu lỗi tại browser
fixture, kiểm tra Firefox launch độc lập. 3. Nếu lỗi DB, kiểm tra
`docker compose ps` và log PostgreSQL. 4. Nếu lỗi import, xác nhận có
`PYTHONPATH=/app`. 5. Chạy lại test liên quan trước, rồi chạy toàn bộ
suite.

## 5. Lộ trình NumPy, Pandas và Matplotlib

Thực hành trước trong notebook hoặc script riêng với dữ liệu dự án. Khi
đã hiểu kết quả, mới chuyển hàm ổn định vào `analytics/` và tích hợp API
nếu hữu ích.

### Bước 1 --- Pandas: khám phá dữ liệu

-   Dùng `head()`, `shape`, `columns`, `dtypes`, `info()`.
-   Kiểm tra thiếu dữ liệu bằng `isna().sum()`.
-   Lọc/sắp xếp bằng `loc`, boolean filtering và `sort_values()`.
-   Đếm bằng `value_counts()` và `groupby()`.

Câu hỏi: có bao nhiêu user; số user theo role/gender; bao nhiêu bài viết
mỗi user; ai có nhiều bài viết nhất?

### Bước 2 --- NumPy: thống kê

Thực hành `np.mean()`, `np.median()`, `np.min()`, `np.max()`, `np.std()`
trên tuổi hoặc số bài viết/user. Ghi rõ xử lý giá trị thiếu và việc
`np.std()` mặc định dùng population standard deviation (`ddof=0`);
`ddof=1` dùng sample standard deviation.

### Bước 3 --- Pandas: biến đổi và kết hợp

-   Tạo cột tuổi từ `birth_year`.
-   Phân nhóm tuổi bằng `pd.cut()` và ghi rõ biên nhóm.
-   Kết hợp users và post counts bằng `merge()`.
-   Tổng hợp theo role bằng `groupby()`.

Kiểm tra DataFrame rỗng, birth year thiếu, user không có bài viết và
user có nhiều bài viết.

### Bước 4 --- Matplotlib: trực quan hóa

-   Bar chart: user theo role/gender/age group.
-   Histogram: phân phối tuổi.
-   Bar chart: top users theo số bài viết.

Thêm tiêu đề, nhãn trục, đơn vị nếu có, và ghi chú cách xử lý dữ liệu
thiếu.

### Bước 5 --- Tổ chức và tích hợp

-   Giữ bài thử trong `notebook/` hoặc script học riêng.
-   Chuyển hàm đã hiểu và kiểm tra vào `analytics/`.
-   Giữ router mỏng; tránh đặt toàn bộ logic phân tích trong router.
-   Chỉ tạo endpoint analytics khi có mục đích cụ thể.

## 6. Nhật ký mỗi buổi học

``` text
Ngày:
Mục tiêu:
Dữ liệu sử dụng:
Câu hỏi cần trả lời:
Các hàm/thao tác đã học:
Kết quả:
Điều đã hiểu:
Lỗi gặp phải và cách xử lý:
Việc tiếp theo:
```

## 7. Quy trình làm việc gợi ý

1.  `docker compose up -d`
2.  `docker compose ps` và `curl http://localhost:8000/health`
3.  Thực hành Pandas/NumPy/Matplotlib.
4.  Chạy test liên quan sau khi sửa code.
5.  Lưu ghi chú và trạng thái test/coverage.
6.  Dừng bằng `docker compose down` nếu cần, không thêm `-v` khi cần giữ
    DB.
