from sqlalchemy.orm import Session

from app.core.security import verify_password
from app.crud.user import get_user_by_email
from app.models import User


def authenticate_user(
    db: Session,
    email: str,
    password: str,
) -> User | None:
    user = get_user_by_email(
        db,
        email,
    )

    if user is None:
        return None

    if not verify_password(
        password,
        user.password,
    ):
        return None

    return user