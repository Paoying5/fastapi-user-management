import pandas as pd
import numpy as np
from psutil import users 
from sqlalchemy import select 
from app.models.user import User 
from datetime import date

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

# Tính tuổi
def add_age_column(df: pd.DataFrame):
    current_year = date.today().year

    df = df.copy()

    df["age"] = (
        current_year - df["birth_year"]
    )

    return df

# Nếu `birth_year` bị thiếu thì nên xử lý
def add_age_column(df: pd.DataFrame):
    current_year = date.today().year

    df = df.copy()

    df["age"] = (
        current_year - df["birth_year"]
    )

    return df

# Phân nhóm độ tuổi
def add_age_group(df: pd.DataFrame):
    df = df.copy()

    df["age_group"] = pd.cut(
        df["age"],
        bins=[0, 18, 25, 35, 50, 100],
        labels=[
            "Under 18",
            "18-25",
            "26-35",
            "36-50",
            "50+",
        ],
        right=True,
    )

    return df

def users_by_age_group(df: pd.DataFrame):
    return (
        df["age_group"]
        .value_counts()
        .sort_index()
        .reset_index()
    )

def calculate_age_statistics(df: pd.DataFrame):
    ages = df["age"].dropna().to_numpy()

    if len(ages) == 0:
        return {
            "count": 0,
            "mean": None,
            "median": None,
            "min": None,
            "max": None,
            "std": None,
        }

    return {
        "count": len(ages),
        "mean": float(np.mean(ages)),
        "median": float(np.median(ages)),
        "min": float(np.min(ages)),
        "max": float(np.max(ages)),
        "std": float(np.std(ages)),
    }