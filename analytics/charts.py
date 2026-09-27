# biểu đồ User theo Role
import matplotlib.pyplot as plt

from analytics.post_analysis import top_users_by_posts


def plot_users_by_role(df):
    counts = (
        df["role"]
        .value_counts()
    )

    fig, ax = plt.subplots()

    counts.plot(
        kind="bar",
        ax=ax,
    )

    ax.set_title(
        "Number of Users by Role"
    )

    ax.set_xlabel("Role")
    ax.set_ylabel("Number of Users")

    fig.tight_layout()

    return fig


# biểu đồ User theo độ tuổi
def plot_age_distribution(df): 
    ages = df["age"].dropna() 
    fig, ax = plt.subplots()
    ax.hist( ages, bins=10, )
    ax.set_title( "User Age Distribution" )
    ax.set_xlabel("Age")
    ax.set_ylabel("Number of Users")
    fig.tight_layout() 
    return fig

# Top User có nhiều Post
def plot_top_users_by_posts( 
        users_df, 
        posts_df,
        limit=10,
):
        top_users = ( 
        top_users_by_posts( 
        users_df, 
        posts_df, 
        limit, 
        )
    ) 
        fig, ax = plt.subplots()
        ax.bar( top_users["username"],
                top_users["post_count"], 
        ) 
        ax.set_title( "Top Users by Number of Posts" ) 
        ax.set_xlabel("Username")
        ax.set_ylabel("Number of Posts")
        plt.xticks( 
                rotation=45, 
                ha="right", 
        ) 
        fig.tight_layout()
        return fig


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# ==========================================
# 0. KHỞI TẠO DỮ LIỆU GIẢ LẬP (MOCK DATA)
# ==========================================
# Dữ liệu Users
users_data = {
    "user_id":,
    "username": [
        "An",
        "Bình",
        "Cường",
        "Dũng",
        "Hoa",
        "Lan",
        "Minh",
        "Nam",
        "Oanh",
        "Phúc",
        "Quang",
        "Sơn",
    ],
    "age":,
    "role_id":,
}
df_users = pd.DataFrame(users_data)

# Dữ liệu Roles
roles_data = {
    "role_id":,
    "role_name": ["Admin", "Editor", "Viewer"],
}
df_roles = pd.DataFrame(roles_data)

# Dữ liệu Posts (Số lượng post của từng user)
posts_data = {
    "user_id":,
    "post_count":,
}
df_posts = pd.DataFrame(posts_data)


# ==========================================
# BÀI 1: Thống kê tuổi của User
# ==========================================
print("--- BÀI 1: Thống kê tuổi ---")
# Chuyển cột tuổi thành mảng numpy để tính toán
ages = df_users["age"].to_numpy()

age_max = np.max(ages)
age_min = np.min(ages)
age_mean = np.mean(ages)
age_median = np.median(ages)
age_std = np.std(ages)

print(f"User lớn tuổi nhất: {age_max}")
print(f"User trẻ tuổi nhất: {age_min}")
print(f"Tuổi trung bình: {age_mean:.2f}")
print(f"Median tuổi: {age_median}")
print(f"Độ lệch chuẩn tuổi: {age_std:.2f}\n")


# ==========================================
# BÀI 2: Tìm 5 user có nhiều post nhất
# ==========================================
print("--- BÀI 2: Top 5 users có nhiều post nhất ---")
# Gộp bảng users và posts để lấy tên user kèm số post
df_user_posts = pd.merge(df_users, df_posts, on="user_id")

# Sắp xếp giảm dần theo số post và lấy 5 dòng đầu
top_5_users = df_user_posts.sort_values(by="post_count", ascending=False).head(5)
print(top_5_users[["username", "post_count"]].to_string(index=False), "\n")


# ==========================================
# BÀI 3: Tính số post trung bình của mỗi role
# ==========================================
print("--- BÀI 3: Số post trung bình của mỗi role ---")
# Merge bảng user_posts với bảng roles
df_merged = pd.merge(df_user_posts, df_roles, on="role_id")

# Groupby theo role_name và tính mean của post_count
role_post_mean = (
    df_merged.groupby("role_name")["post_count"].mean().reset_index()
)
print(role_post_mean.to_string(index=False), "\n")


# ==========================================
# BÀI 4: Vẽ biểu đồ - User theo role
# ==========================================
# Đếm số lượng user thuộc mỗi role
role_counts = df_merged["role_name"].value_counts()

fig, ax = plt.subplots(figsize=(6, 4))
ax.bar(role_counts.index, role_counts.values, color="skyblue", edgecolor="black")
ax.set_title("Số lượng User theo Role")
ax.set_xlabel("Tên Role")
ax.set_ylabel("Số lượng User")
fig.tight_layout()


# ==========================================
# BÀI 5: Vẽ histogram - Phân bố tuổi của User
# ==========================================
fig2, ax2 = plt.subplots(figsize=(6, 4))
# Sử dụng plt.hist() thông qua ax (hướng đối tượng) hoặc trực tiếp plt.hist()
ax2.hist(df_users["age"], bins=5, color="lightgreen", edgecolor="black")
ax2.set_title("Biểu đồ phân bố tuổi của User (Histogram)")
ax2.set_xlabel("Độ tuổi")
ax2.set_ylabel("Tần suất (Số user)")
fig2.tight_layout()


# ==========================================
# BÀI 6: Vẽ Top 10 user có nhiều post nhất
# ==========================================
# Lấy top 10 user nhiều post nhất
top_10_users = df_user_posts.sort_values(by="post_count", ascending=False).head(
    10
)

fig3, ax3 = plt.subplots(figsize=(10, 5))
ax3.bar(
    top_10_users["username"],
    top_10_users["post_count"],
    color="salmon",
    edgecolor="black",
)
ax3.set_title("Top 10 User có nhiều bài Post nhất")
ax3.set_xlabel("Tên User")
ax3.set_ylabel("Số lượng Post")
fig3.tight_layout()

# Hiển thị tất cả các biểu đồ đã vẽ
plt.show()
