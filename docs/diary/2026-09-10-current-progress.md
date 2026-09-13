# Diary – 10/09/2026

Hôm nay em tiếp tục debug phần Swagger E2E.

Em kiểm tra lại flow Authorize. Ý định là sau khi login lấy được token thì đưa token vào Swagger Authorize, sau đó mới thực hiện POST /posts/.

Vấn đề là Swagger có modal Authorize và backdrop phía sau. Sau khi authorize xong, em tưởng modal đã đóng nhưng Playwright vẫn thấy .backdrop-ux còn visible.

Vì vậy khi test cố click sang endpoint /posts/ thì bị lỗi do overlay đang chặn pointer events.

Em thử kiểm tra locator và thứ tự thao tác thay vì chỉ tăng thời gian chờ.

**Tình trạng:** Chưa fix được. Em bắt đầu mất khá nhiều thời gian ở phần UI của Swagger chứ không phải ở API Post.
