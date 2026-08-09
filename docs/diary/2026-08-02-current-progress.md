# 📅 Development Diary — 2026-08-02

## Chủ đề
**Tiếp tục refactor kiến trúc và làm rõ trách nhiệm giữa các tầng.**

> Nhật ký giai đoạn 02/08–08/08 được tổng hợp lại từ trạng thái source code, migration, test và các vấn đề đã được trao đổi trong quá trình học. Mục tiêu là ghi lại hành trình học tập một cách trung thực, không biến project thành một “perfect project” giả định.

---

## Hôm nay tôi tập trung vào điều gì?

Sau khi thực hành Repository Pattern, tôi bắt đầu nhận ra rằng việc tách file/tách folder không tự động làm code tốt hơn. Điều quan trọng hơn là phải hiểu **mỗi tầng chịu trách nhiệm gì**.

Luồng kiến trúc tôi hướng tới:

```text
Router
  ↓
Service
  ↓
Repository / Data Access
  ↓
SQLAlchemy
  ↓
PostgreSQL
```

---

## Điều tôi học được

- Router nên tập trung vào HTTP request/response.
- Service phù hợp với business logic và orchestration.
- Repository phù hợp với database access.
- Schema dùng để validate dữ liệu vào/ra.
- Model đại diện cho database entity.

Điểm quan trọng nhất tôi nhận ra: **refactor architecture phải đi kèm kiểm tra import, dependency và flow thực tế**, nếu không rất dễ tạo ra code cũ và code mới cùng tồn tại.

---

## Bài học thực tế

Không nên chỉ nhìn cây thư mục rồi kết luận rằng architecture đã đúng. Cần kiểm tra cả đường đi của một request:

```text
HTTP request
→ Router
→ Service
→ Repository
→ Database
→ Model
→ Schema
→ HTTP response
```

Đây là cách tôi bắt đầu kiểm tra project có thực sự “đi đúng đường ray” hay chưa.

---

## Ghi chú

Tôi bắt đầu quan tâm nhiều hơn đến **tính nhất quán của toàn project** thay vì chỉ làm cho từng endpoint chạy được.
