import pandas as pd
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User


def get_users_dataframe(
    session: Session,
) -> pd.DataFrame:
    """
    Load the currently supported User fields into a DataFrame.

    This function intentionally uses only columns that actually exist
    in the current SQLAlchemy User model.
    """
    users = session.scalars(
        select(User)
    ).all()

    data = [
        {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "role": user.role,
            "full_name": user.full_name,
        }
        for user in users
    ]

    return pd.DataFrame(
        data,
        columns=[
            "id",
            "name",
            "email",
            "role",
            "full_name",
        ],
    )


def count_users(
    df: pd.DataFrame,
) -> int:
    return len(df)


def users_by_role(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Count users grouped by role.

    Null roles are grouped as 'unknown' so analytics does not silently
    discard those records.
    """
    if df.empty:
        return pd.DataFrame(
            columns=[
                "role",
                "user_count",
            ]
        )

    role_counts = (
        df["role"]
        .fillna("unknown")
        .value_counts()
        .rename_axis("role")
        .reset_index(name="user_count")
    )

    return role_counts