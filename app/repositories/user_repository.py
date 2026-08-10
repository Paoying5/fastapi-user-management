from sqlalchemy.orm import Session, joinedload

from app.models.user import User


class UserRepository:
    """Persistence operations for User entities only."""

    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[User]:
        return (
            self.db.query(User)
            .options(joinedload(User.posts))
            .order_by(User.id.asc())
            .all()
        )

    def get_by_id(self, user_id: int) -> User | None:
        return (
            self.db.query(User)
            .options(joinedload(User.posts))
            .filter(User.id == user_id)
            .first()
        )

    def get_by_email(self, email: str) -> User | None:
        return self.db.query(User).filter(User.email == email).first()

    def add(self, user: User) -> User:
        self.db.add(user)
        self.db.flush()
        self.db.refresh(user)
        return user

    def update(self, user: User) -> User:
        self.db.flush()
        self.db.refresh(user)
        return user

    def delete(self, user: User) -> None:
        self.db.delete(user)
        self.db.flush()
