# 📅 Development Diary — 2026-08-07

## Chủ đề
**Alembic migration và thay đổi schema `full_name`.**

---

## Thay đổi model

User model được bổ sung field:

```text
full_name
```

Schema cũng được bổ sung để API có thể nhận/đại diện field này.

---

## Migration được tạo

Project có migration:

```text
5614567ad165_add_full_name.py
```

Migration này kế thừa:

```text
e122a64acbc0
```

và revision chain trở thành:

```text
e122a64acbc0
        ↓
5614567ad165
```

---

## Điều tôi học được

Một migration file tồn tại chưa có nghĩa migration đã thay đổi database.

Cần phân biệt:

```text
Model changed
      ≠
Migration file exists
      ≠
Database schema changed
```

Phải kiểm tra migration `upgrade()` thực sự có operation tương ứng và kiểm tra schema PostgreSQL sau khi upgrade.

---

## Bài học debugging

Đây là một điểm rất quan trọng trong quá trình học của tôi: **Alembic phải được kiểm tra cả lịch sử migration lẫn trạng thái schema thực tế.**

Không nên chỉ nhìn:

```text
alembic current
```

rồi kết luận database đã đúng.
