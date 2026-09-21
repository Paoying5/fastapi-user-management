import pandas as pd
from psutil import users 
from sqlalchemy import select 
from app.models.user import User 
def get_users_dataframe(session): 
    users = session.scalars( select(User) ).all() 
    data = [] 
    for user in users: 
        data.append( { 
            "id": user.id, 
            "username": user.username, 
            "email": user.email, 
            "gender": user.gender, 
            "birth_year": user.birth_year, 
            "role": user.role, 
            "is_active": user.is_active, 
        } ) 
    return pd.DataFrame(data)

def count_users(df: pd.DataFrame):
    return len(df)

# Thống kê theo role:

def users_by_role(df: pd.DataFrame):
    return (
        df["role"]
        .value_counts()
        .reset_index()
        .rename(
            columns={
                "role": "role",
                "count": "user_count",
            }
        )
    )

# Thống kê theo giới tính
def users_by_gender(df: pd.DataFrame):
    return (
        df["gender"]
        .fillna("Unknown")
        .value_counts()
        .reset_index()
        .rename(
            columns={
                "gender": "gender",
                "count": "user_count",
            }
        )
    )