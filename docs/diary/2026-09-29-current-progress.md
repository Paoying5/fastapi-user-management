# Hoàn thiện Authentication và kiểm tra project

## 📝 Công việc đã làm

Trong ngày đầu tiên của tuần, tôi tiếp tục kiểm tra phần authentication của project **FastAPI User Management**.

Tôi tập trung vào phần **password security**, đặc biệt là các hàm:
* `hash_password()`
* `verify_password()`
* `create_access_token()`

Project đang sử dụng `pwdlib` với **Argon2** để hash password và `python-jose` để tạo **JWT**.

Tôi chạy thử trực tiếp các hàm hash và verify trong container để kiểm tra:
- [x] Password đúng có verify thành công không.
- [x] Password sai có bị từ chối không.
- [x] Password có được lưu dưới dạng hash hay không.

> **Kết quả:** Quá trình password hashing và verification hoạt động chính xác.

Tôi cũng kiểm tra lại cách tạo access token và cập nhật phần xử lý thời gian sang `datetime` có timezone **UTC**.

---

## 🐳 Docker

Trong quá trình chạy `docker-compose`, tôi gặp một số cảnh báo (*warning*):
```text
The "UID" variable is not set.
The "GID" variable is not set.
```

**Cách xử lý:**
1. Kiểm tra lại cấu hình Docker Compose configuration.
2. Kiểm tra cách container API được khởi chạy.

Sau khi điều chỉnh cấu hình, API vẫn hoạt động bình thường và không ảnh hưởng đến dữ liệu **PostgreSQL** hiện tại.

---

## 🚀 Kết quả

Kiểm tra trạng thái hoạt động (*Health check*) của API:

```bash
curl http://localhost:8000/health
```

Kết quả trả về:
```json
{
  "status": "healthy",
  "api": "running",
  "database": "connected"
}
```

Qua phần này, tôi hiểu rõ hơn về cách kiểm tra một backend service đang chạy, cũng như cách kiểm tra nhanh kết nối giữa API với database.
