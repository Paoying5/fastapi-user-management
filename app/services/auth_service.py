from sqlalchemy.orm import Session

from app.core.security import verify_password
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
