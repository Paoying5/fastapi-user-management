# 📅 Development Diary — 2026-08-29

## Chủ đề
**Kiểm chứng runtime thực tế: authentication và API flow.**

Sau một khoảng thời gian không ghi diary đều đặn, tôi quay lại kiểm chứng project bằng runtime thực tế thay vì chỉ nhìn source code.

### Kết quả đã ghi nhận

- `GET /` → `200 OK`.
- OpenAPI load được các endpoint `/health`, `/auth/login`, `/auth/me`, `/users/`, `/users/{user_id}`, `/posts/`, `/posts/me`, `/posts/{post_id}`.
- `POST /users/` → `201 Created`.
- `POST /auth/login` → `200 OK` và trả JWT.
- Protected endpoints với `$TOKEN` → `401 Could not validate credentials`.

Sau khi kiểm tra terminal, tôi phát hiện `$TOKEN` đang rỗng (`echo "$TOKEN"` không in ra gì). Vì vậy chưa thể kết luận JWT implementation bị lỗi; trước tiên phải lưu access token thật vào biến shell rồi test lại.

### Một vấn đề khác cần điều tra

Request tạo user gửi `role="admin"` nhưng response trả `role="user"`.

Đây là một điểm cần xác định xem là business/security rule có chủ đích hay bug.

### Insight

> Khi debugging, phải kiểm tra runtime state trước khi sửa code và phải phân biệt authentication với authorization.

