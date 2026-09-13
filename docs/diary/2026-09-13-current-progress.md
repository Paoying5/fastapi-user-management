# Diary – 13/09/2026

Hôm nay em chạy lại test E2E:

tests/e2e/test_swagger_posts.py

Test được chạy trong Docker bằng Firefox.

Kết quả hiện tại:

1 failed, 2 warnings

Lỗi xảy ra ở bước kiểm tra backdrop của Swagger:

expect(backdrop).to_be_hidden()

Nhưng thực tế .backdrop-ux vẫn đang visible.

Sau đó nếu tiếp tục click endpoint thì overlay có thể chặn pointer event.

Qua lỗi này em thấy vấn đề hiện tại chưa chắc nằm ở Post API hay database mà nhiều khả năng nằm ở trạng thái của Swagger UI sau khi Authorize.

Em đã thử hướng wait nhưng chưa fix dứt điểm được.

Hiện tại em chưa muốn đi tiếp thêm feature vì nếu flow User → Auth → Authorize → Post chưa ổn thì test các bước GET/PATCH/DELETE phía sau cũng khó kiểm tra chính xác.

**Tình trạng cuối tuần:** Vẫn đang kẹt ở E2E Swagger Authorize → Post. Chưa hoàn thành flow Post như kế hoạch.
