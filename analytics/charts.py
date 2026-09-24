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