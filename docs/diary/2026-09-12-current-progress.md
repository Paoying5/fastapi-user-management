# Diary – 12/09/2026

Hôm nay em tiếp tục thử chạy test trong Docker.

Em muốn đảm bảo test chạy trong đúng môi trường project chứ không chỉ chạy riêng ở máy local.

Em chạy pytest với Firefox trong container và kiểm tra lại log.

Có một số warning liên quan đến UID và GID, nhưng em đang cố tách warning này ra khỏi lỗi chính để không sửa nhầm vấn đề.

Lỗi chính vẫn là Swagger Authorize chưa đóng overlay đúng cách. Vì vậy khi Playwright chuyển sang POST /posts/ thì thao tác click bị chặn.

Em có thử thêm bước wait nhưng cảm giác chỉ wait lâu hơn không giải quyết được nguyên nhân thật sự.

**Tình trạng:** Vẫn bị kẹt ở Authorize → Post.
