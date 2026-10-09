from sqlalchemy import (
    asc,
    func,
    or_,
    select,
)
from sqlalchemy.orm import (
    Session,
    joinedload,
    selectinload,
)

from app.models.user import User


class UserRepository:
    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def get_all(
        self,
        limit: int = 10,
        offset: int = 0,
        search: str = "",
    ) -> list[User]:
        statement = (
            select(User)
            .options(
                selectinload(
                    User.posts
                )
            )
        )

        if search:
            pattern = (
                f"%{search}%"
            )

            statement = (
                statement.where(
                    or_(
                        User.name.ilike(
                            pattern
                        ),
                        User.email.ilike(
                            pattern
                        ),
                    )
                )
            )

        statement = (
            statement
            .order_by(
                asc(User.id)
            )
            .offset(offset)
            .limit(limit)
        )

        return list(
            self.db.scalars(
                statement
            ).all()
        )

    def count(
        self,
        search: str = "",
    ) -> int:
        statement = (
            select(
                func.count()
            )
            .select_from(User)
        )

        if search:
            pattern = (
                f"%{search}%"
            )

            statement = (
                statement.where(
                    or_(
                        User.name.ilike(
                            pattern
                        ),
                        User.email.ilike(
                            pattern
                        ),
                    )
                )
            )

        result = self.db.scalar(
            statement
        )

        return int(
            result or 0
        )

    def get_by_id(
        self,
        user_id: int,
    ) -> User | None:
        statement = (
            select(User)
            .options(
                joinedload(
                    User.posts
                )
            )
            .where(
                User.id
                == user_id
            )
        )

        return (
            self.db
            .scalars(statement)
            .unique()
            .first()
        )

    def get_by_email(
        self,
        email: str,
    ) -> User | None:
        statement = (
            select(User)
            .where(
                User.email
                == email
            )
        )

        return (
            self.db
            .scalars(statement)
            .first()
        )

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