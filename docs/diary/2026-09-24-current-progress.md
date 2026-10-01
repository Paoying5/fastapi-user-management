# 📅 Development Diary — 2026-09-24

## Chủ đề
**Phân tích sự phân mảnh giữa `crud/` và `repositories/` trước khi tiến hành Refactor.**

---

## 1. Vấn đề phát hiện
Khi rà soát lại toàn bộ cây thư mục mã nguồn để chuẩn bị cho giai đoạn tối ưu hóa, tôi nhận thấy dự án đang rơi vào tình trạng **Split Responsibility (Phân mảnh trách nhiệm)** ở tầng truy cập dữ liệu:
* Thư mục `app/crud/` cũ (từ giai đoạn phát triển ban đầu) và thư mục `app/repositories/` mới đang cùng tồn tại song song.
* Một số hàm ở Router vẫn gọi gián tiếp qua cơ chế cũ, trong khi các tính năng nâng cao lại dùng cơ chế Class Injection của tầng Repository.
* `app/main.py` vẫn giữ lệnh cấu hình thô:
  ```python
  Base.metadata.create_all(bind=engine)
  ```
  Điều này gây xung đột vùng xám với lịch sử di cư (Migration Chain) của **Alembic** (`e7d9b8aad922_initial_schema.py`).

---

## 2. Giải pháp kiến trúc đề xuất
Tôi quyết định thiết lập một kế hoạch refactor nghiêm túc để ép toàn bộ luồng request chạy qua một trục duy nhất:
```text
Router (HTTP) ➔ Service (Business/Orchestration) ➔ Repository (Data Access) ➔ PostgreSQL
```
* **Hành động 1:** Chuyển dịch toàn bộ logic database còn sót lại từ `crud/` sang các hàm nghiệp vụ của `UserRepository` và `PostRepository`.
* **Hành động 2:** Vô hiệu hóa hoàn toàn lệnh `create_all()` tại file khởi chạy để giao trọn quyền quản trị Schema cho hệ thống Migration.

---

## 3. Bài học rút ra
Tách folder chỉ là hình thức bên ngoài. Để đạt được Clean Architecture thực sự, cấu trúc dữ liệu đi vào và đi ra giữa các lớp ranh giới phải có sự nhất quán và không được chồng chéo trách nhiệm lên nhau.
