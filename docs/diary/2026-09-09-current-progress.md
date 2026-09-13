# Diary – 09/09/2026

Hôm nay em chuyển sang phần Swagger UI + Playwright.

Mục tiêu là dùng browser để test giống cách người dùng thao tác trên Swagger:

Open Swagger → chọn endpoint → Try it out → nhập dữ liệu → Execute

Em bắt đầu làm test cho Post vì phần Post cần user đã đăng nhập và có token.

Trong lúc làm em gặp khá nhiều vấn đề với locator của Swagger. Có lúc locator tìm đúng endpoint nhưng Playwright vẫn không click được.

Em phải đọc lại log của Playwright để xem element nào đang nằm phía trên và đang chặn thao tác.

**Tình trạng:** Bắt đầu bị kẹt ở phần E2E, chưa đi được nhanh như dự kiến.
