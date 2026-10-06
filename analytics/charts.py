import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.figure import Figure

from analytics.post_analysis import top_users_by_posts


def plot_users_by_role(
    df: pd.DataFrame,
) -> Figure:
    """
    Create a bar chart showing the number of users for each role.
    """
    if "role" not in df.columns:
        raise ValueError(
            "DataFrame must contain a 'role' column"
        )

    counts = (
        df["role"]
        .fillna("unknown")
        .value_counts()
    )

    fig, ax = plt.subplots()

    ax.bar(
        counts.index,
        counts.values,
    )

    ax.set_title("Number of Users by Role")
    ax.set_xlabel("Role")
    ax.set_ylabel("Number of Users")

    fig.tight_layout()

    return fig


def plot_age_distribution(
    df: pd.DataFrame,
) -> Figure:
    """
    Create an age histogram from a DataFrame that already contains
    an 'age' column.

    The current User database model does not provide age data,
    so this helper is not used by the FastAPI analytics endpoint.
    """
    if "age" not in df.columns:
        raise ValueError(
            "DataFrame must contain an 'age' column"
        )

    ages = df["age"].dropna()

    fig, ax = plt.subplots()

    ax.hist(
        ages,
        bins=10,
    )

    ax.set_title("User Age Distribution")
    ax.set_xlabel("Age")
    ax.set_ylabel("Number of Users")

    fig.tight_layout()

    return fig


def plot_top_users_by_posts(
    users_df: pd.DataFrame,
    posts_df: pd.DataFrame,
    limit: int = 10,
) -> Figure:
    """
    Create a bar chart of users with the highest number of posts.
    """
    if limit < 1:
        raise ValueError(
            "limit must be greater than or equal to 1"
        )

    top_users = top_users_by_posts(
        users_df=users_df,
        posts_df=posts_df,
        limit=limit,
    )

    fig, ax = plt.subplots()

    ax.bar(
        top_users["name"],
        top_users["post_count"],
    )

    ax.set_title(
        "Top Users by Number of Posts"
    )
    ax.set_xlabel("User")
    ax.set_ylabel("Number of Posts")

    ax.tick_params(
        axis="x",
        labelrotation=45,
    )

    fig.tight_layout()

    return fig