import pandas as pd

from sqlalchemy import select

from app.database import SessionLocal
from app.models.user import User


# ==========================================
# 1. LOAD USERS FROM DATABASE
# ==========================================

with SessionLocal() as db:
    users = db.scalars(
        select(User)
    ).all()


# ==========================================
# 2. CONVERT DATABASE DATA -> DATAFRAME
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
# 3. SELECT ONE COLUMN
# ==========================================

print("\n========== ONE COLUMN ==========")

print(df["name"])


# ==========================================
# 4. SELECT MULTIPLE COLUMNS
# ==========================================

print("\n========== MULTIPLE COLUMNS ==========")

print(
    df[
        ["name", "email", "role"]
    ]
)


print("\n========== NAME + FULL NAME ==========")

print(
    df[
        ["name", "full_name"]
    ]
)

# ==========================================
# 5. FILTER BY ROLE
# ==========================================

print("\n========== FILTER: ROLE = USER ==========")

users = df[df["role"] == "user"]

print(users)

# ==========================================
# 6. FILTER NAME CONTAINS "SWAGGER"
# ==========================================

print("\n========== FILTER: NAME CONTAINS SWAGGER ==========")

swagger_users = df[
    df["name"].str.contains("Swagger", case=False, na=False)
]

print(swagger_users)


# ==========================================
# 7. COUNT SWAGGER USERS
# ==========================================

print("\n========== NUMBER OF SWAGGER USERS ==========")

print(len(swagger_users))


# ==========================================
# 8. SORT BY NAME
# ==========================================

print("\n========== SORT BY NAME ==========")

sorted_by_name = df.sort_values(
    "name"
)

print(
    sorted_by_name[
        ["id", "name", "role"]
    ]
)


# ==========================================
# 9. SORT NAME DESCENDING
# ==========================================

print("\n========== SORT NAME DESCENDING ==========")

sorted_by_name_desc = df.sort_values(
    "name",
    ascending=False
)

print(
    sorted_by_name_desc[
        ["id", "name"]
    ]
)


# ==========================================
# 10. SORT BY ID DESCENDING
# ==========================================

print("\n========== SORT BY ID DESCENDING ==========")

latest_users = df.sort_values(
    "id",
    ascending=False
)

print(
    latest_users[
        ["id", "name", "email"]
    ].head(10)
)

# ==========================================
# 11. GROUP BY ROLE
# ==========================================

print("\n========== GROUP BY ROLE ==========")

grouped_by_role = df.groupby("role")

print(grouped_by_role)


# ==========================================
# 11. GROUP BY ROLE + SIZE
# ==========================================

print("\n========== USERS BY ROLE ==========")

users_by_role = (
    df.groupby("role")
      .size()
)

print(users_by_role)


# ==========================================
# 12. GROUP BY ROLE + COUNT ID
# ==========================================

print("\n========== COUNT USERS BY ROLE ==========")

user_count_by_role = (
    df.groupby("role")["id"]
      .count()
)

print(user_count_by_role)


# ==========================================
# 13. GROUP BY ROLE -> DATAFRAME
# ==========================================

print("\n========== USERS BY ROLE DATAFRAME ==========")

users_by_role_df = (
    df.groupby("role")
      .size()
      .reset_index(name="user_count")
)

print(users_by_role_df)


# ==========================================
# 11. USERS BY ROLE
# ==========================================

print("\n========== USERS BY ROLE ==========")

users_by_role = (
    df.groupby("role")
      .size()
)

print(users_by_role)


# ==========================================
# 12. COUNT ID BY ROLE
# ==========================================

print("\n========== COUNT ID BY ROLE ==========")

user_count_by_role = (
    df.groupby("role")["id"]
      .count()
)

print(user_count_by_role)


# ==========================================
# 13. USERS BY ROLE DATAFRAME
# ==========================================

print("\n========== USERS BY ROLE DATAFRAME ==========")

users_by_role_df = (
    df.groupby("role")
      .size()
      .reset_index(name="user_count")
)

print(users_by_role_df)


# ==========================================
# 14. VALUE COUNTS
# ==========================================

print("\n========== VALUE COUNTS ==========")

role_counts = df["role"].value_counts()

print(role_counts)


# ==========================================
# 15. GROUP BY FIRST LETTER OF NAME
# ==========================================

print("\n========== USERS BY FIRST LETTER ==========")

users_by_first_letter = (
    df["name"]
      .str[0]
      .value_counts()
      .sort_index()
)

print(users_by_first_letter)


# ==========================================
# 16. GROUP BY FIRST LETTER - CASE INSENSITIVE
# ==========================================

print("\n========== FIRST LETTER CASE INSENSITIVE ==========")

users_by_first_letter = (
    df["name"]
      .str[0]
      .str.upper()
      .value_counts()
      .sort_index()
)

print(users_by_first_letter)

# ==========================================
# 14. VALUE COUNTS
# ==========================================

print("\n========== VALUE COUNTS ==========")

role_counts = df["role"].value_counts()

print(role_counts)


# ==========================================
# 15. FIRST LETTER OF NAME
# ==========================================

print("\n========== USERS BY FIRST LETTER ==========")

users_by_first_letter = (
    df["name"]
      .str[0]
      .str.upper()
      .value_counts()
      .sort_index()
)

print(users_by_first_letter)


# ==========================================
# 16. CHECK MISSING VALUES
# ==========================================

print("\n========== MISSING VALUES ==========")

missing_values = df.isna().sum()

print(missing_values)


# ==========================================
# 17. SMALL PRACTICE
# ==========================================

print("\n========== SWAGGER USERS SORTED ==========")

swagger_users = df[
    df["name"].str.contains("Swagger", case=False, na=False)
]

swagger_users = swagger_users.sort_values("name")

print(swagger_users[["id", "name", "email"]])

print("\n========== SWAGGER NAME COUNTS ==========")

swagger_name_counts = swagger_users["name"].value_counts()

print(swagger_name_counts)

print("\n========== MISSING VALUES ==========")

print(swagger_users.isna().sum())