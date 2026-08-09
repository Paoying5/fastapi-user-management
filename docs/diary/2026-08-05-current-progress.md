# 📅 Development Diary — 2026-08-05

## Chủ đề
**Testing và kiểm tra API theo hướng thực tế.**

---

## Vì sao cần test?

Sau khi refactor nhiều tầng, tôi nhận ra rằng code “nhìn có vẻ đúng” chưa đủ.

Một thay đổi ở:

- model
- schema
- repository
- service
- router
- database

đều có thể làm endpoint khác hỏng theo.

Vì vậy tôi bắt đầu coi test như một cách kiểm tra toàn bộ đường đi của request.

---

## Các loại test trong project

Project hiện có các nhóm:

```text
tests/
├── api/
├── swagger/
└── e2e/
```

Có test cho:

- health endpoint
- create user
- get users
- authentication
- posts
- Swagger-related checks
- end-to-end Swagger capture

---

## Cách kiểm tra

Một request test đi theo hướng:

```text
pytest
  ↓
HTTP request
  ↓
FastAPI
  ↓
Database
  ↓
HTTP response
  ↓
assert
```

Điều này giúp tôi hiểu rằng test API không chỉ kiểm tra một function Python đơn lẻ mà có thể kiểm tra cả integration giữa nhiều thành phần.

---

## Bài học

Khi test fail, không nên lập tức sửa assertion.

Cần xem:

1. request thực sự gửi gì?
2. endpoint nào được gọi?
3. status code là gì?
4. response body là gì?
5. log server nói gì?
6. database schema có khớp model không?

Đây trở thành một thói quen debugging quan trọng.
