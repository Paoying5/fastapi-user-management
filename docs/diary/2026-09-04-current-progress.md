# 📅 Development Diary — 2026-09-04

## Chủ đề
**Hoàn thiện API test cho Posts và xử lý test assumption.**

---

## 1. Post tests

Bộ test Posts được mở rộng để kiểm tra:

- create post
- unauthorized request
- get posts
- search
- get my posts
- get post by ID
- not found
- update
- patch
- delete
- ownership forbidden
- invalid title

Tổng cộng:

```text
12 tests
```

---

## 2. Test assumption

Một test giả định thứ tự các post trong response, trong khi repository chưa cam kết thứ tự đó.

Test được sửa để kiểm tra requirement thực tế, không phụ thuộc vào thứ tự không được quy định.

---

## 3. Kết quả

```text
tests/api/test_posts.py
12 passed
```

Các nhóm API test trước đó cũng pass. Tổng API tests:

```text
22 passed
```

Có 2 deprecation warnings từ dependency, nhưng không phải test failure.

---

## 4. Bài học

Cần phân biệt implementation bug và test assumption bug. Không nên sửa production code chỉ để thỏa mãn một assumption không nằm trong requirement.
