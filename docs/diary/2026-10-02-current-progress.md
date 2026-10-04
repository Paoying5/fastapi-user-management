# Bắt đầu học NumPy và Pandas

## 📊 Bắt đầu phần Data Analysis

Sau khi phần backend và testing đã tương đối ổn định, tôi chuyển sang lộ trình học tập mới bao gồm các thư viện:
* **NumPy**
* **Pandas**
* **Matplotlib**

Để chuẩn bị, tôi đã tạo riêng thư mục `practice/` để chứa toàn bộ mã nguồn thực hành, nhằm đảm bảo cô lập hoàn toàn và không làm ảnh hưởng đến mã nguồn production của dự án.

---

## 💾 Làm việc với dữ liệu User

Tôi thực hiện kết nối và trích xuất dữ liệu `User` trực tiếp từ cơ sở dữ liệu **PostgreSQL** thông qua **SQLAlchemy**, sau đó chuyển đổi tập dữ liệu này thành một **Pandas DataFrame**.

### Cấu trúc dữ liệu thu được:
* **Kích thước:** `93 rows` × `5 columns`
* **Chi tiết các trường thông tin (Fields):**

| Model thực tế trong DB | DataFrame thu được |
| :--- | :--- |
| `id`, `name`, `email`, `role`, `password`, `full_name` | `id`, `name`, `email`, `role`, `full_name` *(loại bỏ `password`)* |

---

## 🧮 Thực hành với NumPy

Tôi làm quen với các phép toán thống kê cơ bản của **NumPy** bao gồm:
* `mean` (trung bình)
* `median` (trung vị)
* `min` / `max` (giá trị nhỏ nhất / lớn nhất)
* `sum` (tổng)
* `std` (độ lệch chuẩn)

> 💡 **Bài học rút ra:** Ban đầu, tôi sử dụng cột `id` để luyện tập các phép tính trên. Tuy nhiên, tôi nhanh chóng nhận ra rằng vì `id` chỉ đóng vai trò là định danh (*identifier*), các chỉ số thống kê toán học trên cột này hoàn toàn không mang lại giá trị hay ý nghĩa về mặt nghiệp vụ (*business logic*). Mặc dù vậy, bài tập này vẫn giúp tôi hiểu rõ cách thức NumPy xử lý và vận hành trên các mảng dữ liệu số.

---

## 🐛 Lỗi gặp phải trong quá trình thực hành

Trong đoạn code ban đầu, tôi đã gọi ra trường dữ liệu `username` theo thói quen cũ. Do model thực tế không tồn tại trường này, hệ thống đã trả về cảnh báo lỗi:

```text
AttributeError: 'User' object has no attribute 'username'
```

**Cách xử lý:** Tôi đã tiến hành đối chiếu lại cấu trúc định nghĩa của model `User` và điều chỉnh mã nguồn để sử dụng chính xác các trường dữ liệu hiện có (`id`, `name`, `email`, `role`, `full_name`).

---

## 💡 Bài học kinh nghiệm

* **Tránh tư duy lối mòn:** Khi làm việc với một dự án thực tế có sẵn, tuyệt đối không được tự giả định cấu trúc dữ liệu hay các model sẽ giống hệt với các bài hướng dẫn (*tutorials*) trên mạng.
* **Quy trình chuẩn:** Luôn có bước kiểm tra, rà soát lại cấu trúc thực tế của database schema hoặc file định nghĩa model trước khi bắt tay vào viết code xử lý dữ liệu.
