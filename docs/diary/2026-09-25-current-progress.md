# 📅 Development Diary — 2026-09-25

## Chủ đề
**Thực hiện Refactor hạ tầng dữ liệu và bàn giao toàn quyền cho Alembic.**

---

## 1. Các hạng mục đã thực hiện

### 🔹 Cập nhật `app/main.py`
Tôi đã mở tệp khởi chạy ứng dụng và tiến hành **xóa bỏ hoàn toàn** dòng lệnh cấu hình tự động sinh bảng:
```python
# ĐÃ XÓA: Base.metadata.create_all(bind=engine)
```
Từ thời điểm này, toàn bộ vòng đời của cơ sở dữ liệu (PostgreSQL 16) sẽ được kiểm soát nghiêm ngặt thông qua lệnh di cư:
```bash
docker compose exec api alembic upgrade head
```

### 🔹 Làm sạch dự án
Để đảm bảo mã nguồn không còn tài liệu hay tàn dư gây nhiễu, tôi tiến hành xóa sổ hoàn toàn thư mục cũ bằng lệnh hệ thống trên máy host:
```bash
rm -rf app/crud/
```

### 🔹 Tối ưu hóa môi trường Test (`pytest.ini`)
Trong các đợt chạy test trước, màn hình console bị tràn ngập các dòng thông báo màu vàng `DeprecationWarning` từ thư viện `starlette`. Tôi đã bổ sung cấu hình bộ lọc cảnh báo vào `pytest.ini` để làm sạch báo cáo đầu ra:
```ini
filterwarnings =
    ignore::DeprecationWarning:starlette.*
```

---

## 2. Kết quả đạt được
* Kiến trúc dự án trở nên đồng nhất, gọn gàng theo chuẩn Layered Architecture.
* Không còn rủi ro ghi đè hoặc tự động sửa đổi bảng ngoài ý muốn từ SQLAlchemy ORM khi chạy ứng dụng trên môi trường Production.
