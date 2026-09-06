# FastAPI User Management — Development Diary
## 2026-08-30 → 2026-09-06

Bộ diary này nối tiếp `docs/diary/2026-08-30-current-progress.md` và ghi lại tiến trình đến hết ngày 06/09/2026.

## Files

```text
2026-08-30-current-progress.md
2026-08-31-current-progress.md
2026-09-01-current-progress.md
2026-09-02-current-progress.md
2026-09-03-current-progress.md
2026-09-04-current-progress.md
2026-09-05-current-progress.md
2026-09-06-current-progress.md
```

## Lưu ý về tính chính xác lịch sử

Các diary từ **30/08 đến 05/09** là bản **tái dựng liên tục từ project context và các trao đổi đã có**, vì các file diary riêng của những ngày này không có sẵn trong nguồn Library mà tôi có thể đọc tại thời điểm tạo gói.

Vì vậy chúng được viết để **nối mạch học tập và kỹ thuật**, không nên hiểu là commit history theo từng giờ.

File **2026-09-06-current-progress.md** được dựa trên diary 06/09 hiện có và kết quả test cuối ngày.

## Điểm tiếp tục

Tại cuối ngày 06/09:

```text
POST /users/
      ↓
POST /auth/login
      ↓
Authorize
      ↓
POST /posts/
      ↓
GET /posts/{post_id}
      ↓
PATCH /posts/{post_id}
      ↓
DELETE /posts/{post_id}
      ↓
Screenshot evidence
```

E2E hiện đạt:

```text
3 passed, 2 warnings
```
