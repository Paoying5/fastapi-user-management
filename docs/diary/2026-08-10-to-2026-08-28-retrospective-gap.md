# 📚 Retrospective Learning Record — 2026-08-10 → 2026-08-28

> **Lưu ý về tính trung thực:** Khoảng thời gian này không còn log nhật ký nguyên bản theo từng ngày trong project context hiện tại. Vì vậy tôi **không dựng một lịch sử giả**. Tài liệu này ghi nhận khoảng trống và những gì có thể xác nhận từ trạng thái project về sau.

## Vì sao có khoảng trống?

Sau bản tổng hợp ngày 09/08, diary không được cập nhật đều. Project vẫn tiếp tục được thay đổi/refactor, nhưng record hiện có không đủ để xác định chính xác ngày nào thực hiện thay đổi nào.

## Những gì có thể xác nhận

Ở trạng thái project được ghi nhận về sau, kiến trúc đã có:

```text
app/
├── core/
├── models/
├── repositories/
├── routers/
├── schemas/
├── services/
└── utils/
```

Ngoài ra có:

```text
alembic/
tests/
scripts/
Dockerfile
docker-compose.yml
pytest.ini
```

Điều này cho thấy project đã phát triển từ cấu trúc ban đầu sang architecture có nhiều layer hơn.

## Những vấn đề tôi tiếp tục phải kiểm chứng

- Router → Service → Repository có thực sự nhất quán không?
- Có code cũ hoặc duplicate responsibility sau refactor không?
- SQLAlchemy Model và Pydantic Schema có đồng bộ không?
- Alembic migration có phản ánh đúng database schema không?
- Docker healthy có đồng nghĩa business API đúng không?
- pytest đang kiểm tra behavior thực tế đến mức nào?
- Authentication và authorization có được kiểm chứng độc lập không?

## Bài học

Việc bỏ diary một thời gian cho tôi thấy documentation cũng là một phần của engineering workflow.

Từ đây tôi muốn ghi:

```text
Ngày
↓
Mục tiêu
↓
Thực hành
↓
Kết quả
↓
Lỗi
↓
Root cause
↓
Insight
↓
Next step
```

Nếu thiếu log, tôi sẽ ghi rõ **không có log nguyên bản**, thay vì biến suy đoán thành lịch sử.
