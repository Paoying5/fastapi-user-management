# 📅 Development Diary — 2026-08-03

## Chủ đề
**Service Layer và business logic.**

---

## Mục tiêu học tập

Tìm hiểu vì sao một project có Repository nhưng vẫn có thể cần Service Layer.

Repository không nên biết:

- FastAPI
- HTTPException
- HTTP status code
- API response
- Business rule

Service là nơi phù hợp hơn cho các quy tắc như:

- Chuẩn hóa email.
- Kiểm tra email đã tồn tại.
- Quyết định khi nào trả về lỗi business.
- Điều phối nhiều thao tác repository.

---

## Một flow tôi cần ghi nhớ

```text
UserCreate
   ↓
Router
   ↓
User Service
   ↓
Validate business rule
   ↓
Repository
   ↓
User Model
   ↓
PostgreSQL
```

---

## PUT và PATCH

Tôi tiếp tục củng cố sự khác nhau giữa:

### PUT
Thay thế resource theo schema đầy đủ.

### PATCH
Chỉ thay đổi những field được gửi lên.

Với PATCH, ý tưởng quan trọng là:

```python
model_dump(exclude_unset=True)
```

để tránh vô tình ghi đè những field người dùng không gửi.

---

## Bài học

Service Layer không phải là nơi “ném tất cả code vào cho dài project”.

Một tầng mới chỉ có giá trị khi nó giúp trách nhiệm rõ ràng hơn.
