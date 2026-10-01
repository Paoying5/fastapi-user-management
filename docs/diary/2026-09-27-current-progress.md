# 📅 Development Diary — 2026-09-27

## Chủ đề
**Thiết kế và tích hợp Server-Side Pagination & Search cho bảng dữ liệu Users.**

---

## 1. Mục tiêu nghiệp vụ
Hiện tại endpoint `GET /users/` đang lấy ra toàn bộ danh sách người dùng trong hệ thống mà không có sự kiểm soát về dung lượng. Nếu số lượng tài khoản lên tới hàng vạn, việc này sẽ gây nghẽn băng thông truyền tải dữ liệu và tràn bộ nhớ đệm của API. 

Mục tiêu hôm nay là áp dụng bộ lọc phân trang chủ động (Pagination) và tìm kiếm không phân biệt hoa thường (Case-Insensitive Search) theo đúng mô hình 3 lớp.

---

## 2. Mã nguồn triển khai chi tiết

### 🔹 Lớp Dữ liệu (`app/repositories/user_repository.py`)
Nâng cấp hàm `get_all` để nhận tham số lọc, sử dụng cấu trúc toán tử logic toán tử `OR` (`|`) để tìm kiếm song song cả tên hoặc email:
```python
def get_all(self, limit: int = 10, offset: int = 0, search: str = "") -> list[User]:
    statement = select(User).options(joinedload(User.posts))
    
    if search:
        statement = statement.where(
            User.name.ilike(f"%{search}%") | 
            User.email.ilike(f"%{search}%")
        )
        
    statement = statement.order_by(asc(User.id)).offset(offset).limit(limit)
    return list(self.db.scalars(statement).unique().all())
```

### 🔹 Lớp Nghiệp vụ (`app/services/user_service.py`)
Mở rộng hàm chuyển tiếp tham số điều phối dữ liệu từ tầng trên xuống kho lưu trữ:
```python
def get_users(self, limit: int = 10, offset: int = 0, search: str = "") -> list[User]:
    return self.repository.get_all(limit=limit, offset=offset, search=search)
```

### 🔹 Lớp Giao tiếp (`app/routers/user.py`)
Định nghĩa Query Parameter kèm điều kiện ràng buộc dữ liệu đầu vào thông qua đối tượng `Query` của FastAPI:
```python
@router.get("/", response_model=APIResponse, summary="Get all users")
def get_users(
    limit: int = Query(default=10, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    search: str = Query(default="", max_length=100),
    service: UserService = Depends(get_user_service),
    admin: User = Depends(get_admin_user)
):
    users = service.get_users(limit=limit, offset=offset, search=search)
    data = [UserResponse.model_validate(user).model_dump() for user in users]
    return response("Users retrieved successfully", data)
```

---

## 3. Tình trạng cuối ngày
Tính năng đã được tích hợp thành công lên hệ thống thực thi runtime. Kiểm tra Swagger UI cho thấy các tham số đầu vào hiển thị tường minh và chính xác. Tiến hành thực hiện lệnh lưu vết Git an toàn trước khi đăng xuất hệ thống:
```bash
git add .
git commit -m "feat: add pagination and search queries to get all users endpoint"
```
