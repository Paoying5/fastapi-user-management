from sqlalchemy import asc, select
from sqlalchemy.orm import (
    Session,
    joinedload,
    selectinload,
)

from app.models.user import User


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(
        self,
        limit: int = 10,
        offset: int = 0,
        search: str = "",
    ) -> list[User]:
        statement = select(User).options(
            selectinload(User.posts)
        )

        if search:
            statement = statement.where(
                User.name.ilike(
                    f"%{search}%"
                )
                | User.email.ilike(
                    f"%{search}%"
                )
            )

        statement = (
            statement
            .order_by(asc(User.id))
            .offset(offset)
            .limit(limit)
        )

        return list(
            self.db.scalars(
                statement
            ).all()
        )

    def get_by_id(
        self,
        user_id: int,
    ) -> User | None:
        statement = (
            select(User)
            .options(
                joinedload(User.posts)
            )
            .where(
                User.id == user_id
            )
        )

        return (
            self.db.scalars(statement)
            .unique()
            .first()
        )

    def get_by_email(
        self,
        email: str,
    ) -> User | None:
        statement = select(User).where(
            User.email == email
        )

        return self.db.scalars(
            statement
        ).first()

    def add(
        self,
        user: User,
    ) -> User:
        self.db.add(user)
        self.db.flush()
        self.db.refresh(user)

        return user

    def update(
        self,
        user: User,
    ) -> User:
        self.db.flush()
        self.db.refresh(user)

        return user

    def delete(
        self,
        user: User,
    ) -> None:
        self.db.delete(user)
        self.db.flush()