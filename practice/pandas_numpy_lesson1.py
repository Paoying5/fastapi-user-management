import numpy as np
import pandas as pd

from sqlalchemy import select

from app.database import SessionLocal
from app.models.user import User


# ==========================================
# 1. Lấy User từ PostgreSQL
# ==========================================

with SessionLocal() as db:
    users = db.scalars(
        select(User)
    ).all()


# ==========================================
# 2. SQLAlchemy objects -> Pandas DataFrame
# ==========================================

data = []

for user in users:
    data.append(
        {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "role": user.role,
            "full_name": user.full_name,
        }
    )

df = pd.DataFrame(data)


# ==========================================
# 3. Xem DataFrame
# ==========================================

print("\n========== DATAFRAME ==========")
print(df)


# ==========================================
# 4. Kích thước DataFrame
# ==========================================

print("\n========== SHAPE ==========")
print(df.shape)


# ==========================================
# 5. Tên các cột
# ==========================================

print("\n========== COLUMNS ==========")
print(df.columns)


# ==========================================
# 6. Kiểu dữ liệu
# ==========================================

print("\n========== DTYPES ==========")
print(df.dtypes)


# ==========================================
# 7. 5 dòng đầu
# ==========================================

print("\n========== HEAD ==========")
print(df.head())


# ==========================================
# 8. Thống kê cơ bản
# ==========================================

print("\n========== DESCRIBE ==========")
print(df.describe())


# ==========================================
# 9. Đếm User theo Role
# ==========================================

print("\n========== USERS BY ROLE ==========")
print(df["role"].value_counts())


# ==========================================
# 10. Kiểm tra dữ liệu thiếu
# ==========================================

print("\n========== MISSING VALUES ==========")
print(df.isna().sum())


# ==========================================
# 11. Lấy riêng cột name
# ==========================================

print("\n========== NAMES ==========")
print(df["name"])


# ==========================================
# 12. Lấy nhiều cột
# ==========================================

print("\n========== NAME + ROLE ==========")

print(
    df[
        [
            "name",
            "role",
        ]
    ]
)


# ==========================================
# 13. Chuyển User ID sang NumPy array
# ==========================================

user_ids = df["id"].to_numpy()

print("\n========== NUMPY USER IDS ==========")
print(user_ids)


# ==========================================
# 14. NumPy statistics
# ==========================================

print("\n========== NUMPY STATISTICS ==========")

print("Mean   :", np.mean(user_ids))
print("Median :", np.median(user_ids))
print("Min    :", np.min(user_ids))
print("Max    :", np.max(user_ids))
print("Sum    :", np.sum(user_ids))
print("Std    :", np.std(user_ids))