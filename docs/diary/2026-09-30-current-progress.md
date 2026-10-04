# Debug Playwright Firefox trong Docker

## 📝 Công việc đã làm

Hôm nay tôi tập trung vào việc chạy **E2E test** bằng **Playwright** với trình duyệt **Firefox** bên trong Docker.

Ban đầu, API vẫn chạy bình thường nhưng Firefox không thể khởi động bên trong container. Lỗi gặp phải như sau:

```text
Sandbox: CanCreateUserNamespace() clone() failure: EPERM
```

**Phân tích ban đầu:**
* Tôi đã kiểm tra lại quá trình cài đặt Playwright và Firefox nhưng nhận ra vấn đề không nằm ở việc cài thiếu package.
* Nguyên nhân gốc rễ liên quan đến **sandbox** và **Linux user namespace** bên trong Docker container.

---

## 🔍 Quá trình Debug

Tôi tiến hành kiểm tra việc tạo user namespace bên trong container và phát hiện **Docker security profile** đang ngăn chặn thao tác này.

**Giải pháp xử lý:**
Sau khi tìm hiểu và thử nghiệm, tôi đã bổ sung cấu hình `security_opt` vào container API trong môi trường development hiện tại:

```yaml
security_opt:
  - seccomp:unconfined
```

**Kết quả sau cấu hình:**
* Tiến hành rebuild và restart lại container, Firefox đã có thể khởi động thành công.
* Tôi đã kiểm tra trực tiếp việc launch Firefox trước khi chạy toàn bộ E2E test.
* **Kết quả:** `Firefox launch OK`

---

## 💡 Bài học kinh nghiệm

Qua lỗi này, tôi rút ra được bài học rằng khi một chương trình chạy tốt ở máy local nhưng thất bại trong Docker, nguyên nhân có thể nằm ở:
* **Permission** (Quyền truy cập)
* **Sandbox** (Cơ chế cô lập)
* **Security profile** (Cấu hình bảo mật)
* **Container configuration** (Cấu hình container)

> 📌 **Lưu ý quan trọng:** Cấu hình `seccomp:unconfined` hiện tại chỉ được áp dụng để phục vụ môi trường **development / E2E test** và **không** được xem là cấu hình mặc định khi triển khai lên môi trường **production** để đảm bảo tính an toàn hệ thống.
