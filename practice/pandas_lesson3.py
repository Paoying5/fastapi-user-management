import pandas as pd

from sqlalchemy import text

from app.database import engine


# ==========================================
# 1. SQL QUERY
# ==========================================

query = text("""
    SELECT
        role,
        COUNT(*) AS total_users

    FROM users

    GROUP BY role

    ORDER BY total_users DESC
""")


# ==========================================
# 2. SQL RESULT -> DATAFRAME
# ==========================================

df = pd.read_sql_query(
    query,
    engine
)


# ==========================================
# 3. DISPLAY DATA
# ==========================================

print("\n========== USERS BY ROLE ==========")

print(df)


# ==========================================
# 4. CHECK DATAFRAME
# ==========================================

print("\n========== DATAFRAME INFO ==========")

print(df.info())


# ==========================================
# 5. TOTAL USERS
# ==========================================

print("\n========== TOTAL USERS ==========")

print(df["total_users"].sum())