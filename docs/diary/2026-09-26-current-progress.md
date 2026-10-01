# 📅 Development Diary — 2026-09-26

## Chủ đề
**Xử lý cảnh báo môi trường Docker Linux (UID/GID) và tối ưu hóa tốc độ Test.**

---

## 1. Vấn đề rào cản môi trường
Mỗi khi tôi thực hiện các lệnh gọi kiểm thử hoặc vận hành container, hệ thống liên tục đưa ra cảnh báo:
```text
WARN[0000] The "UID" variable is not set. Defaulting to a blank string.
WARN[0000] The "GID" variable is not set. Defaulting to a blank string.
```
Nguyên nhân do Docker Compose cố gắng map quyền sở hữu tệp tin (`user: "${UID}:${GID}"` trong `docker-compose.yml`) giữa máy Host chạy Linux Ubuntu và môi trường ảo hóa bên trong Container nhưng hai biến này chưa được khởi tạo ở môi trường cục bộ.

---

## 2. Giải pháp khắc phục
Tôi đã tiến hành nạp trực tiếp mã định danh định danh User (UID) và Group (GID) của tài khoản hệ điều hành hiện tại vào tệp cấu hình ẩn `.env`:
```bash
echo "UID=\$(id -u)" >> .env
echo "GID=\$(id -g)" >> .env
```
Sau đó tiến hành khởi động lại toàn bộ các dịch vụ để áp dụng:
```bash
docker compose down && docker compose up -d
```

---

## 3. Bước nhảy vọt về hiệu năng kiểm thử
Sau khi dọn sạch các cảnh báo môi trường và cấu hình ẩn Warning Starlette, tôi thực hiện chạy bộ thử nghiệm giả lập E2E trên trình duyệt Firefox:
```bash
docker compose exec api pytest tests/e2e -v --browser firefox
```
* **Kết quả:** **PASSED 100% (9/9 tests E2E thành công)**.
* **Thời gian thực thi:** Giảm mạnh từ **95.70 giây xuống còn 20.75 giây** (Nhanh gấp 4.5 lần). Việc giải phóng các cảnh báo nghẽn luồng và làm sạch cache giúp Playwright tương tác với phần tử Swagger UI mượt mà hơn rất nhiều.
