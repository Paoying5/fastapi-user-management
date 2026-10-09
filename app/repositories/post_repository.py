from sqlalchemy import (
    desc,
    func,
    select,
)
from sqlalchemy.orm import (
    Session,
    joinedload,
)

from app.models.post import Post


class PostRepository:
    """Persistence operations for Post entities."""

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
    ) -> list[Post]:
        statement = (
            select(Post)
            .options(
                joinedload(
                    Post.owner
                )
            )
        )

        if search:
            statement = (
                statement.where(
                    Post.title.ilike(
                        f"%{search}%"
                    )
                )
            )

        statement = (
            statement
            .order_by(
                desc(Post.id)
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
            .select_from(Post)
        )

        if search:
            statement = (
                statement.where(
                    Post.title.ilike(
                        f"%{search}%"
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
        post_id: int,
    ) -> Post | None:
        statement = (
            select(Post)
            .options(
                joinedload(
                    Post.owner
                )
            )
            .where(
                Post.id
                == post_id
            )
        )

        return (
            self.db
            .scalars(statement)
            .first()
        )

    def get_by_user_id(
        self,
        user_id: int,
    ) -> list[Post]:
        statement = (
            select(Post)
            .options(
                joinedload(
                    Post.owner
                )
            )
            .where(
                Post.user_id
                == user_id
            )
            .order_by(
                desc(Post.id)
            )
        )

        return list(
            self.db.scalars(
                statement
            ).all()
        )

    def add(
        self,
        post: Post,
    ) -> Post:
        self.db.add(post)
        self.db.flush()
        self.db.refresh(post)

        return post

    def update(
        self,
        post: Post,
    ) -> Post:
        self.db.flush()
        self.db.refresh(post)

        return post

    def delete(
        self,
        post: Post,
    ) -> None:
        self.db.delete(post)
        self.db.flush()