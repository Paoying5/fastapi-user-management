from sqlalchemy.orm import Session

from app.core.security import (
    create_access_token,
    verify_password,
)
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.auth import Token


class AuthService:
    """Authentication business rules."""

    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def authenticate_user(
        self,
        email: str,
        password: str,
    ) -> User | None:
        normalized_email = email.strip().lower()

        user = self.repository.get_by_email(
            normalized_email
        )

        if user is None:
            return None

        if not verify_password(
            password,
            user.password,
        ):
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

        access_token = create_access_token(
            {
                "sub": str(user.id),
            }
        )

        return Token(
            access_token=access_token,
            token_type="bearer",
        )

    def get_user_by_id(
        self,
        user_id: int,
    ) -> User | None:
        return self.repository.get_by_id(
            user_id
        )

    def get_user_by_email(
        self,
        email: str,
    ) -> User | None:
        normalized_email = email.strip().lower()

        return self.repository.get_by_email(
            normalized_email
        )