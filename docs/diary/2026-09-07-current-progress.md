# Diary – 07/09/2026

Hôm nay em tiếp tục rà lại project FastAPI User Management. Sau khi đã làm xong phần API cơ bản thì em không muốn thêm feature mới ngay mà quay lại kiểm tra những phần cũ.

Em chủ yếu xem lại User, Auth, Post và cách các phần này liên quan với nhau.

Flow em đang hướng tới là:

Create User → Login → lấy JWT → Authorize → Post

Lúc đọc lại code em thấy các phần liên quan với nhau khá nhiều nên khi test một phần bị lỗi thì phải quay lại kiểm tra cả những bước trước.

Em bắt đầu tập trung nhiều hơn vào phần testing thay vì chỉ kiểm tra API bằng Swagger thủ công.

**Tình trạng:** Chưa có lỗi mới rõ ràng nhưng bắt đầu bị chậm vì phải rà lại nhiều phần.
