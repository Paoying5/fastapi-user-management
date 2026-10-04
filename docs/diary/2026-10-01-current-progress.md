# Chạy lại toàn bộ test và kiểm tra database

## 🧪 Quá trình Testing

Sau khi xử lý thành công vấn đề với Playwright Firefox, tôi tiến hành chạy lại toàn bộ API test và E2E test bằng lệnh sau:

```bash
docker compose exec \
  -e PYTHONPATH=/app \
  api pytest -q \
  tests/api tests/e2e \
  --browser firefox \
  --cov=app \
  --cov-report=term-missing \
  --cov-report=html
```

**Kết quả kiểm thử:**
* **Tổng số:** `31 passed`
  * bao gồm **22 API tests** và **9 E2E tests**.
* **Mức độ bao phủ (Coverage):** Đạt khoảng **79%**.

Tôi cũng đã khởi tạo **HTML coverage report** để xem chi tiết những phần code nào đã được test và những phần nào còn đang bị thiếu sót.

---

## 🗄️ Cấu trúc PostgreSQL và Alembic

Tôi đã thực hiện kiểm tra lại database và quá trình migration:
* **Alembic current state:** Đang ở revision `e7d9b8aad922 (head)`.
* **Quản lý Schema:** Project hiện tại đã **không còn** sử dụng `create_all()` trong file `main.py` để tự tạo schema tự động khi application khởi động. Việc quản lý và cập nhật database schema hoàn toàn được thực hiện thông qua **Alembic migration**.
* **Dữ liệu:** Tôi đã xác nhận lại PostgreSQL container và đảm bảo toàn bộ dữ liệu vẫn được lưu trữ an toàn, độc lập trong **Docker volume**.

---

## 💡 Bài học kinh nghiệm

* **Phân biệt kiểm thử:** Hiểu rõ hơn sự khác nhau giữa **API test** (tập trung vào từng API/chức năng cụ thể) và **E2E test** (kiểm tra toàn bộ luồng hoạt động thực tế gần nhất với cách người dùng cuối sử dụng hệ thống).
* **Bản chất của Test Coverage:** Hiểu thêm rằng *coverage* là một chỉ số tốt giúp đo lường mức độ mã nguồn được kiểm thử, tuy nhiên coverage đạt tỷ lệ cao không đồng nghĩa với việc project chắc chắn hoàn toàn sạch bug.
