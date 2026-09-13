# Diary – 11/09/2026

Hôm nay em tiếp tục rà lại phần Post và E2E.

Em không muốn sửa API Post lung tung khi chưa chắc lỗi nằm ở API hay ở browser test nên tập trung tách hai vấn đề này ra.

Flow em muốn test là:

Create User
→ Login
→ Authorize
→ POST /posts/
→ GET /posts/{post_id}
→ PATCH /posts/{post_id}
→ DELETE /posts/{post_id}

Em kiểm tra lại helper trong tests/e2e/utils.py, đặc biệt là phần tìm endpoint và các thao tác Try it out / Execute.

Locator của /posts/ có thể tìm được endpoint, nhưng vấn đề vẫn nằm ở bước sau Authorize.

**Tình trạng:** Flow Post chưa chạy xuyên suốt được.
