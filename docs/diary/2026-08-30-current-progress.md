# 📅 Development Diary — 2026-08-30

## Chủ đề
**Debugging có kiểm soát và chuẩn hóa cách thực hành.**

Tôi tiếp tục xây dựng lại quy trình thực hành theo từng checkpoint nhỏ thay vì sửa nhiều phần cùng lúc.

### Quy trình kiểm chứng

```text
Root / Health
    ↓
OpenAPI
    ↓
Create User
    ↓
Login
    ↓
Lưu access token
    ↓
/auth/me
    ↓
Protected User API
    ↓
PATCH / PUT / DELETE
    ↓
Post API
    ↓
pytest
    ↓
Database / Alembic verification
```

Mỗi lần test chỉ nên chứng minh một mắt xích. Nếu một bước fail thì dừng ở đó, đọc status code + response + server log rồi mới sửa.

### Insight

> Quy trình debugging tốt giúp giảm việc “sửa quá trời sửa” và giúp tôi biết chính xác thay đổi nào đã tạo ra kết quả nào.

