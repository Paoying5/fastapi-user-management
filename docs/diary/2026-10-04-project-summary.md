# Value Counts, xử lý dữ liệu và tổng kết tuần

## 📊 Kỹ thuật Value Counts

Hôm nay tôi tiếp tục học cách đếm tần suất xuất hiện của dữ liệu bằng phương thức:
```python
df["role"].value_counts()
```

**Kết quả trả về:**
```text
user    93
Name: role, dtype: int64
```

💡 **Bài học rút ra:** Hàm `value_counts()` cực kỳ phù hợp khi mục tiêu duy nhất là đếm nhanh số lần xuất hiện của từng giá trị trong một cột cụ thể. So với `groupby().size()`, phương thức này ngắn gọn và tiện lợi hơn rất nhiều khi không cần thực hiện thêm các phép tính tổng hợp phức tạp khác.

---

## 🔤 Xử lý dữ liệu chữ hoa và chữ thường

Tôi thực hành trích xuất chữ cái đầu tiên trong tên của User bằng cú pháp `df["name"].str[0]`.

* **Hiện tượng ban đầu:** Kết quả trả về chứa cả chữ hoa và chữ thường riêng biệt (`A`, `S`, `a`) do dữ liệu gốc chưa đồng nhất:
  * `Admin Test` → `A`
  * `Swagger ...` → `S`
  * `admin` → `a`
* **Giải pháp chuẩn hóa:** Tôi sử dụng `.str.upper()` để chuyển toàn bộ ký tự về dạng chữ in hoa trước khi đếm:
  ```python
  df["name"].str[0].str.upper().value_counts()
  ```
* **Kết quả sau khi xử lý:** Dữ liệu đã được gộp nhóm chính xác:
  ```text
  S    91
  A     2
  ```

> 📌 **Nhận xét:** Đây là một ví dụ thực tế điển hình về tầm quan trọng của việc **làm sạch và chuẩn hóa dữ liệu** (Data Cleaning) trước khi tiến hành các bước phân tích hay thống kê chuyên sâu.

---

## 🔍 Kiểm tra và xử lý dữ liệu thiếu (Missing Values)

Tôi bắt đầu tiếp cận các phương thức kiểm tra dữ liệu khuyết thiếu trong DataFrame:

* **Kiểm tra tổng số giá trị thiếu trên từng cột:**
  ```python
  df.isna().sum()
  ```
  *(Hiện tại, tập dữ liệu User đang sử dụng rất sạch và không có missing value nào).*

* **Phương pháp xử lý dữ liệu thiếu bằng `fillna()`:**
  Tôi học được cách điền giá trị thay thế cho các ô trống để tránh lỗi tính toán về sau. Ví dụ, nếu trường `full_name` bị khuyết thiếu, tôi có thể thay thế bằng chuỗi `"Unknown"` để chuẩn hóa luồng dữ liệu:
  ```python
  df["full_name"] = df["full_name"].fillna("Unknown")
  ```
