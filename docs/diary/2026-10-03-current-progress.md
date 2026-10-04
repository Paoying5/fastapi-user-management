# Học Pandas: Filter, Sort và GroupBy

## 📂 Thao tác với DataFrame

Hôm nay tôi tiếp tục làm việc với file `practice/pandas_lesson2.py` để thực hành các cách trích xuất dữ liệu từ DataFrame.

* **Chọn một column:**
  ```python
  df["name"]
  ```
* **Chọn nhiều column:**
  ```python
  df[["name", "email", "role"]]
  ```

Tôi cũng thử trích xuất đồng thời `df[["name", "full_name"]]` để quan sát và đối chiếu mối quan hệ giữa hai trường dữ liệu này.

---

## 🔍 Kỹ thuật Filter (Lọc dữ liệu)

Tôi thực hành lọc dữ liệu người dùng dựa trên các điều kiện cụ thể:

* **Lọc theo role:**
  ```python
  df[df["role"] == "user"]
  ```
* **Lọc những user có tên chứa chuỗi "Swagger"** (không phân biệt hoa thường và bỏ qua giá trị rỗng):
  ```python
  df[df["name"].str.contains("Swagger", case=False, na=False)]
  ```

> 📊 **Kết quả:** Hệ thống lọc ra được **91 Swagger users**.

---

## 🔀 Kỹ thuật Sort (Sắp xếp dữ liệu)

Tôi thực hành sắp xếp dữ liệu theo các chiều hướng khác nhau:
* Sắp xếp theo tên tăng dần: `df.sort_values("name")`
* Sắp xếp theo tên giảm dần: `df.sort_values("name", ascending=False)`
* Sắp xếp theo ID giảm dần và dùng `.head(10)` để lấy ra 10 bản ghi đầu tiên:
  ```python
  df.sort_values("id", ascending=False).head(10)
  ```

💡 **Bài học rút ra:** Hàm `sort_values()` chỉ thay đổi thứ tự hiển thị của các hàng (*rows*) trong DataFrame chứ không làm biến đổi bản chất dữ liệu. Ngoài ra, việc xếp ngược ID chỉ là một mẹo đơn giản để xem nhanh các bản ghi. Để xác định chính xác người dùng nào được tạo gần đây nhất, cấu trúc database chuẩn bắt buộc phải có trường mốc thời gian như `created_at`.

---

## 👥 Kỹ thuật GroupBy (Gom nhóm dữ liệu)

Khi bắt đầu gọi lệnh `df.groupby("role")`, kết quả trả về chỉ là một đối tượng `DataFrameGroupBy` ẩn. Để thu được số liệu thực tế, tôi kết hợp thêm các hàm tổng hợp (*aggregation*):

* **Đếm số lượng phần tử theo nhóm:**
  ```python
  df.groupby("role").size()
  # Kết quả trả về: user    93
  ```
* **Đếm số lượng theo cột định danh:**
  ```python
  df.groupby("role")["id"].count()
  ```
* **Chuyển đổi kết quả gom nhóm ngược lại thành một DataFrame hoàn chỉnh:**
  ```python
  df.groupby("role").size().reset_index(name="user_count")
  ```

---

## 💡 Bài học kinh nghiệm

Tôi bắt đầu nhận thấy sự tương đồng rất lớn và có tính hệ thống giữa ngôn ngữ truy vấn **SQL** và thư viện **Pandas**:

| Tính năng | Câu lệnh SQL (PostgreSQL) | Cú pháp tương đương trong Pandas |
| :--- | :--- | :--- |
| **Lọc dữ liệu** | `WHERE` | `df[condition]` |
| **Sắp xếp** | `ORDER BY` | `.sort_values()` |
| **Gom nhóm** | `GROUP BY` | `.groupby()` |
| **Đếm số lượng** | `COUNT()` | `.size()` hoặc `.count()` |

Mối liên hệ trực quan này giúp tôi tận dụng tốt những kiến thức backend đã học về PostgreSQL để tiếp thu thư viện Pandas nhanh chóng hơn.
