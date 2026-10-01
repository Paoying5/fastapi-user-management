# 📅 Development Diary — 2026-09-28

## Chủ đề
**Kế hoạch ngày làm việc tiếp theo: Viết bộ test phân trang và thiết lập Endpoint Analytics.**

---

## 1. Trạng thái xuất phát điểm (Baseline)
Hệ thống hiện tại đang dừng ở trạng thái cực kỳ ổn định:
* Tầng `crud` lai căng đã được xóa bỏ hoàn toàn.
* Toàn bộ **31/31 kiểm thử tự động** (API + E2E Playwright Swagger) đều đạt trạng thái **PASSED 100%**.
* Tính năng phân trang đầu cuối cho danh sách người dùng đã chạy ổn định trên môi trường thực tế nhưng **chưa có ca kiểm thử tự động (`pytest`) nào bao phủ**.

---

## 2. Kế hoạch hành động chi tiết cho ngày mai

### 📌 Nhiệm vụ 1: Bổ sung Test Coverage cho tính năng Phân trang User
Tôi sẽ mở file `tests/api/test_users.py` và viết thêm 3 ca kiểm thử mới:
1. `test_get_users_pagination`: Tạo hàng loạt user giả lập bằng vòng lặp, sau đó gọi API với các cặp tham số `limit=2&offset=0` và `limit=2&offset=2` để đối chiếu tính chính xác của dữ liệu trả về dựa trên ID tăng dần.
2. `test_get_users_search_by_name`: Kiểm tra tính năng tìm kiếm tài khoản theo từ khóa tên.
3. `test_get_users_search_by_email`: Kiểm tra tính năng lọc tài khoản theo đuôi email.

### 📌 Nhiệm vụ 2: Đưa tầng xử lý số liệu Analytics lên Web API
Hiện tại gói phân tích dữ liệu chuyên sâu nâng cao của dự án (`analytics/charts.py`, `analytics/user_analysis.py`) mới chỉ chạy độc lập dưới dạng file kịch bản cục bộ hoặc nhúng thô ở một router đơn sơ.
* Tôi sẽ tiến hành tích hợp toàn diện các hàm tính toán thống kê (Tính độ lệch chuẩn độ tuổi `age_std`, tìm trung vị tuổi `age_median`, đếm số lượng bài viết trung bình của từng vai trò quản trị) để tạo thành một endpoint API chính thức có đường dẫn:
  ```text
  GET /analytics/users/summary
  ```
  Endpoint này sẽ được cấu hình bảo mật cao, chỉ cho phép những tài khoản có quyền `admin` truy cập để xem báo cáo tổng quan hệ thống.
### ⚠️ Ghi chú Debug lỗi hệ thống ngày 27/09:
* **Hiện tượng:** Xung đột plugin `pytest-html` gây crash lỗi `pytest_sessionfinish` khi khởi tạo lại container sạch.
* **Bài học/Giải pháp:** Phải chạy `mkdir -p tests/reports && chmod 777 tests/reports` trên máy host để cấp quyền ghi tệp báo cáo cho Docker, hoặc thêm cờ `-p no:html` khi cần quét nhanh kiểm thử.
