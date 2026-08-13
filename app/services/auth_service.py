from sqlalchemy.orm import Session
from app.schemas.auth import Token
from app.core.security import create_access_token, verify_password
from app.models.user import User
from app.repositories.user_repository import UserRepository


class AuthService:
    """Authentication business rules."""

    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def authenticate_user(self, email: str, password: str) -> User | None:
        user = self.repository.get_by_email(email.strip().lower())
        if user is None or not verify_password(password, user.password):
            return None
        return user


    def get_user_by_email(
        self,
        email: str,
    ) -> User | None:

        return self.repository.get_by_email(
            email.strip().lower()
        )

def login(
    self,
    email: str,
    password: str,
) -> Token:

    user = self.authenticate_user(
        email,
        password,
    )

    if user is None:
        raise ValueError(
            "Invalid email or password"
        )

    return Token(
        access_token=create_access_token(
            {"sub": user.email}
        ),
        token_type="bearer",
    )