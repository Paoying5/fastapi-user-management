from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.core.security import (
    create_access_token,
    verify_password,
)
from app.models.user import User
from app.repositories.user_repository import (
    UserRepository,
)
from app.schemas.auth import Token


class AuthService:
    """Authentication business rules."""

    def __init__(
        self,
        db: Session,
    ):
        self.db = db
        self.repository = UserRepository(
            db
        )

    def authenticate_user(
        self,
        email: str,
        password: str,
    ) -> User | None:
        email = email.strip().lower()

        user = self.repository.get_by_email(
            email
        )

        if user is None:
            return None

        if not verify_password(
            password,
            user.password,
        ):
            return None

        if not user.is_active:
            return None

        return user

    def login(
        self,
        email: str,
        password: str,
    ) -> Token | None:
        user = self.authenticate_user(
            email,
            password,
        )

        if user is None:
            return None

        try:
            user.last_login_at = datetime.now(
                timezone.utc
            )

            self.db.commit()
            self.db.refresh(user)

        except Exception:
            self.db.rollback()
            raise

        return Token(
            access_token=create_access_token(
                {
                    "sub": str(user.id),
                }
            ),
            token_type="bearer",
        )

    def get_user_by_email(
        self,
        email: str,
    ) -> User | None:
        return self.repository.get_by_email(
            email.strip().lower()
        )

    def get_user_by_id(
        self,
        user_id: int,
    ) -> User | None:
        return self.repository.get_by_id(
            user_id
        )