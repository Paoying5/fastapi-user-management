from sqlalchemy import desc
from sqlalchemy.orm import Session, joinedload

from app.models.post import Post


class PostRepository:
    """Persistence operations for Post entities only."""

    def __init__(self, db: Session):
        self.db = db

    def get_all(
        self,
        limit: int = 10,
        offset: int = 0,
        search: str = "",
    ) -> list[Post]:
        query = self.db.query(Post).options(joinedload(Post.owner))
        if search:
            query = query.filter(Post.title.ilike(f"%{search}%"))
        return (
            query.order_by(desc(Post.id))
            .offset(offset)
            .limit(limit)
            .all()
        )

    def get_by_id(self, post_id: int) -> Post | None:
        return (
            self.db.query(Post)
            .options(joinedload(Post.owner))
            .filter(Post.id == post_id)
            .first()
        )

    def get_by_user_id(self, user_id: int) -> list[Post]:
        return (
            self.db.query(Post)
            .options(joinedload(Post.owner))
            .filter(Post.user_id == user_id)
            .order_by(desc(Post.id))
            .all()
        )

    def add(self, post: Post) -> Post:
        self.db.add(post)
        self.db.flush()
        self.db.refresh(post)
        return post

    def update(self, post: Post) -> Post:
        self.db.flush()
        self.db.refresh(post)
        return post

    def delete(self, post: Post) -> None:
        self.db.delete(post)
        self.db.flush()
