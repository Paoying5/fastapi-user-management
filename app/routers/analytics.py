from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from analytics.user_analysis import (
    count_users,
    get_users_dataframe,
    users_by_role,
)
from app.dependencies import (
    get_admin_user,
    get_db,
)
from app.models import User
from app.schemas import APIResponse
from app.utils.response import response


router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"],
)


@router.get(
    "/users/summary",
    response_model=APIResponse,
    summary="Get user analytics summary",
)
def user_summary(
    db: Session = Depends(get_db),
    admin: User = Depends(get_admin_user),
) -> dict:
    """
    Return basic user statistics.

    Access is restricted to admin users.
    """
    users_df = get_users_dataframe(db)

    role_counts = users_by_role(
        users_df
    )

    data = {
        "total_users": count_users(
            users_df
        ),
        "users_by_role": role_counts.to_dict(
            orient="records"
        ),
    }

    return response(
        "User analytics retrieved successfully",
        data,
    )