# Diary – 08/09/2026

Hôm nay em tiếp tục kiểm tra phần User và Auth.

Em thử lại flow tạo user rồi login để lấy access token. Sau đó kiểm tra việc dùng Bearer token cho các endpoint cần authentication.

Phần này giúp em hiểu rõ hơn là API login trả token chưa có nghĩa là toàn bộ flow authentication đã ổn. Khi sang endpoint protected thì còn liên quan đến dependency lấy current user, token và quyền của user.

Em cũng xem lại test cũ và chỉnh lại một số phần để test dễ đọc hơn.

Sau đó em bắt đầu nghĩ đến việc đưa flow này vào E2E thay vì chỉ test từng API riêng lẻ.

**Tình trạng:** Vẫn làm được từng phần nhưng khi nối thành một flow thì bắt đầu phát sinh vấn đề.
