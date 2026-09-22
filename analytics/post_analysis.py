import pandas as pd
import numpy as np
from sqlalchemy import select

from app.models.post import Post


def get_posts_dataframe(session):
    posts = session.scalars(
        select(Post)
    ).all()

    data = []

    for post in posts:
        data.append(
            {
                "id": post.id,
                "title": post.title,
                "content": post.content,
                "user_id": post.user_id,
            }
        )

    return pd.DataFrame(data)


def posts_per_user(df: pd.DataFrame):
    return (
        df["user_id"]
        .value_counts()
        .rename_axis("user_id")
        .reset_index(name="post_count")
    )


def calculate_post_statistics(df: pd.DataFrame):
    counts = (
        df["user_id"]
        .value_counts()
        .to_numpy()
    )

    if len(counts) == 0:
        return {
            "total_posts": 0,
            "average_posts_per_user": 0,
            "max_posts_by_one_user": 0,
            "min_posts_by_one_user": 0,
            "std": 0,
        }

    return {
        "total_posts": int(len(df)),
        "average_posts_per_user": float(
            np.mean(counts)
        ),
        "max_posts_by_one_user": int(
            np.max(counts)
        ),
        "min_posts_by_one_user": int(
            np.min(counts)
        ),
        "std": float(
            np.std(counts)
        ),
    }


def merge_users_posts(
    users_df: pd.DataFrame,
    posts_df: pd.DataFrame,
):
    post_counts = (
        posts_df["user_id"]
        .value_counts()
        .rename_axis("id")
        .reset_index(name="post_count")
    )

    result = users_df.merge(
        post_counts,
        on="id",
        how="left",
    )

    result["post_count"] = (
        result["post_count"]
        .fillna(0)
        .astype(int)
    )

    return result


def top_users_by_posts(
    users_df: pd.DataFrame,
    posts_df: pd.DataFrame,
    limit: int = 10,
):
    merged = merge_users_posts(
        users_df,
        posts_df,
    )

    return (
        merged
        .sort_values(
            "post_count",
            ascending=False,
        )
        .head(limit)
    )


def posts_by_role(
    users_df: pd.DataFrame,
    posts_df: pd.DataFrame,
):
    merged = merge_users_posts(
        users_df,
        posts_df,
    )

    return (
        merged
        .groupby("role")["post_count"]
        .sum()
        .reset_index()
    )