Chào Trường, dựa trên toàn bộ file project_context.md mà bạn cung cấp, cấu trúc dự án của bạn hiện đã hoàn thiện mô hình 3 lớp (Router -> Service -> Repository) rất sạch sẽ. Phần analytics hiện mới chỉ là các hàm xử lý thô dữ liệu với pandas, numpy, matplotlib hoặc là một endpoint sơ khai.
Để tối ưu, tích hợp hoàn toàn analytics chạy mượt mà cùng Docker thông qua các lệnh siêu dễ nhớ, chúng ta sẽ thực hiện theo phương án chuẩn hóa dưới đây.
------------------------------
## 1. Kiến trúc tối ưu hóa thư mục analytics
Hiện tại file analytics/charts.py đang chứa cả code tạo mock data và lệnh plt.show(). Lệnh plt.show() sẽ gây treo/block container Docker vì môi trường container chạy không có màn hình (headless).
Chúng ta sẽ tối ưu lại: Tầng analytics chịu trách nhiệm tính toán số liệu và xuất biểu đồ ra file ảnh hoặc trả về luồng binary cho API.
## analytics/user_analysis.py (Tính toán số liệu)

import pandas as pdimport numpy as npfrom sqlalchemy import selectfrom app.models.user import User
def get_users_dataframe(session):
    users = session.scalars(select(User)).all()
    data = []
    for user in users:
        # Lưu ý: check đúng các attributes đang có trong app/models/user.py
        data.append({
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "role": user.role,
            "full_name": user.full_name
        })
    return pd.DataFrame(data)
def calculate_advanced_stats(users_df, posts_df):
    """Tính toán nâng cao bằng numpy và pandas"""
    if users_df.empty:
        return {"total_users": 0, "avg_posts": 0}
        
    merged = pd.merge(users_df, posts_df, left_on="id", right_on="user_id", how="left")
    merged["post_count"] = merged["post_count"].fillna(0)
    
    return {
        "total_users": int(len(users_df)),
        "role_distribution": users_df["role"].value_counts().to_dict(),
        "avg_posts_per_user": float(np.mean(merged["post_count"])),
        "max_posts_by_one_user": int(np.max(merged["post_count"]))
    }

## analytics/charts.py (Vẽ biểu đồ - lưu file tĩnh thay vì plt.show())

import matplotlib
matplotlib.use('Agg') # BẮT BUỘC dùng backend này để vẽ không cần màn hình UI trên Dockerimport matplotlib.pyplot as pltimport os
def generate_role_chart(df, output_dir="/app/static"):
    if df.empty or "role" not in df.columns:
        return None
        
    os.makedirs(output_dir, exist_ok=True)
    counts = df["role"].value_counts()
    
    fig, ax = plt.subplots(figsize=(6, 4))
    counts.plot(kind="bar", color="skyblue", edgecolor="black", ax=ax)
    ax.set_title("Số lượng User theo Role")
    ax.set_xlabel("Role")
    ax.set_ylabel("Số lượng")
    
    fig.tight_layout()
    chart_path = os.path.join(output_dir, "role_chart.png")
    fig.savefig(chart_path)
    plt.close(fig) # Giải phóng bộ nhớ giải quyết rò rỉ RAM container
    return chart_path

------------------------------
## 2. Tách Endpoint API chính thức (app/routers/analytics.py)
Tích hợp thẳng luồng dữ liệu vào API và chặn quyền truy cập, chỉ cho tài khoản admin xem số liệu:

from fastapi import APIRouter, Dependsfrom sqlalchemy.orm import Sessionfrom app.database import get_dbfrom app.dependencies import get_admin_userfrom app.models import Userfrom analytics.user_analysis import get_users_dataframe, calculate_advanced_statsfrom analytics.post_analysis import get_posts_dataframe, posts_per_userfrom analytics.charts import generate_role_chart
router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"],
)

@router.get("/summary")def get_analytics_summary(
    db: Session = Depends(get_db),
    admin: User = Depends(get_admin_user) # Bảo mật: Chỉ admin mới xem được số liệu
):
    df_users = get_users_dataframe(db)
    
    # Lấy data posts thông qua hàm có sẵn từ post_analysis.py của bạn
    raw_posts_df = get_posts_dataframe(db)
    df_posts_summary = posts_per_user(raw_posts_df)
    
    # Tính số liệu & vẽ biểu đồ lưu vào container
    stats = calculate_advanced_stats(df_users, df_posts_summary)
    chart_path = generate_role_chart(df_users)
    
    return {
        "status": "success",
        "data": stats,
        "chart_saved_at": chart_path
    }

Đăng ký router này vào app/main.py:

from app.routers import auth, health, post, user, analytics# ...
app.include_router(analytics.router)

------------------------------
## 3. Tối ưu hóa cấu hình chạy trên Docker dễ dàng## Cập nhật Dockerfile
Vì matplotlib cần một số thư viện hệ thống của Linux để xử lý render chữ và hình ảnh, bạn cần bổ sung fontconfig và libfreetype6 vào tầng chạy ngầm của OS (Dockerfile):

FROM python:3.12-slim
WORKDIR /app
ENV PLAYWRIGHT_BROWSERS_PATH=/ms-playwright
COPY requirements.txt requirements-dev.txt ./
# Tối ưu: Cài thêm thư viện bổ trợ cho matplotlib vẽ biểu đồ mượt màRUN apt-get update && apt-get install -y --no-install-recommends \
    fontconfig \
    libfreetype6 \
    && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir -r requirements-dev.txt
RUN playwright install --with-deps firefox
COPY . .
# Khởi tạo thư mục static để map biểu đồ ra máy ngoàiRUN mkdir -p /app/static
HEALTHCHECK \
    --interval=30s \
    --timeout=5s \
    --start-period=20s \
    --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

## Cập nhật docker-compose.yml
Thêm cấu hình Mount Volume cho thư mục hình ảnh tĩnh /app/static để khi Docker vẽ xong biểu đồ, bạn có thể xem trực tiếp file ảnh trên máy chủ máy local cá nhân của bạn mà không cần chui vào trong Container:

services:
  api:
    build: .
    container_name: fastapi-api
    security_opt:
      - seccomp:unconfined
    ports:
      - "8000:8000"
    volumes:
      - .:/app
      - ./static:/app/static # Mount đồng bộ ảnh biểu đồ ra ngoài máy thật
    env_file:
      - .env
    depends_on:
      - postgres# ... các cấu hình postgres giữ nguyên như cũ ...

------------------------------
## 4. Tích hợp lệnh điều khiển siêu dễ nhớ vào scripts/menu.sh
Bạn đang có tập lệnh quản trị bằng Bash Script rất hay (scripts/menu.sh). Hãy mở file đó ra và thêm các dòng lệnh sau vào menu để bấm phím chạy trực tiếp cho nhàn nhé:
Thêm hàm thực thi:

run_analytics_test()
{
    info "Đang chạy script phân tích số liệu trực tiếp trong Container..."
    docker compose exec $API_SERVICE python -m analytics.charts
    success "Đã thực thi chạy kiểm tra cấu trúc dữ liệu xong."
}

Thêm ký tự điều hướng vào phần show_menu():

echo "19. Run Analytics Engine Test"

Thêm trường hợp vào lệnh case $choice in:

19)
run_analytics_test
pause
;;

Bây giờ bạn chỉ cần chạy ./scripts/menu.sh, gõ số 19 là hệ thống tự kích hoạt module tính toán phân tích dữ liệu ngay lập tức mà không cần nhớ các cấu trúc câu lệnh Docker dài dòng.
Nếu bạn đồng ý với luồng xử lý trên, hãy cho tôi biết:

* Bạn có muốn biến endpoint /analytics/users/summary trả về trực tiếp file ảnh biểu đồ dạng streaming thay vì lưu file tĩnh không?
* Hệ thống dữ liệu của bạn có cần phân tích thêm phân phối số lượng bài viết (posts) theo từng mốc thời gian cụ thể nào không?


