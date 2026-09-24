from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.analytics.user_analysis import (
    get_users_dataframe,
    users_by_role,
    calculate_age_statistics,
)

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"],
)


@router.get("/users/summary")
def user_summary(
    db: Session = Depends(get_db),
):
    df = get_users_dataframe(db)

    role_counts = users_by_role(df)

    age_statistics = (
        calculate_age_statistics(df)
    )

    return {
        "total_users": len(df),
        "users_by_role": (
            role_counts
            .to_dict(orient="records")
        ),
        "age_statistics": age_statistics,
    }

Response có thể có dạng:

{
    "total_users": 69,
    "users_by_role": [
        {
            "role": "user",
            "user_count": 65
        },
        {
            "role": "admin",
            "user_count": 4
        }
    ],
    "age_statistics": {
        "count": 60,
        "mean": 25.8,
        "median": 25.0,
        "min": 20,
        "max": 39,
        "std": 4.2
    }
}