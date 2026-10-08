from sqlalchemy.orm import Session

from app.core.exceptions import (
    PermissionDeniedError,
    ResourceNotFoundError,
)
from app.models.post import Post
from app.repositories.post_repository import PostRepository
from app.schemas.post import (
    PostCreate,
    PostPatch,
    PostUpdate,
)


class PostService:
    """Business rules for posts, ownership and transactions."""

    def __init__(self, db: Session):
        self.db = db
        self.repository = PostRepository(db)

    def create_post(
        self,
        post_data: PostCreate,
        user_id: int,
    ) -> Post:
        post = Post(
            title=post_data.title,
            content=post_data.content,
            user_id=user_id,
        )

        try:
            post = self.repository.add(post)

            self.db.commit()

            created_post = self.repository.get_by_id(
                post.id
            )

            if created_post is None:
                raise ResourceNotFoundError(
                    "Post not found after creation"
                )

            return created_post

        except Exception:
            self.db.rollback()
            raise

    def get_posts(
        self,
        limit: int = 10,
        offset: int = 0,
        search: str = "",
    ) -> list[Post]:
        return self.repository.get_all(
            limit=limit,
            offset=offset,
            search=search,
        )

    def get_my_posts(
        self,
        user_id: int,
    ) -> list[Post]:
        return self.repository.get_by_user_id(
            user_id
        )

    def get_post(
        self,
        post_id: int,
    ) -> Post:
        post = self.repository.get_by_id(
            post_id
        )

        if post is None:
            raise ResourceNotFoundError(
                "Post not found"
            )

        return post

    def update_post(
        self,
        post_id: int,
        post_data: PostUpdate,
        user_id: int,
    ) -> Post:
        post = self._get_owned_post(
            post_id,
            user_id,
        )

        post.title = post_data.title
        post.content = post_data.content

        return self._commit_update(post)

    def patch_post(
        self,
        post_id: int,
        post_data: PostPatch,
        user_id: int,
    ) -> Post:
        post = self._get_owned_post(
            post_id,
            user_id,
        )

        update_data = post_data.model_dump(
            exclude_unset=True
        )

        for field_name, value in update_data.items():
            setattr(
                post,
                field_name,
                value,
            )

        return self._commit_update(post)

    def delete_post(
        self,
        post_id: int,
        user_id: int,
    ) -> None:
        post = self._get_owned_post(
            post_id,
            user_id,
        )

        try:
            self.repository.delete(post)
            self.db.commit()

        except Exception:
            self.db.rollback()
            raise

    def _get_owned_post(
        self,
        post_id: int,
        user_id: int,
    ) -> Post:
        post = self.repository.get_by_id(
            post_id
        )

        if post is None:
            raise ResourceNotFoundError(
                "Post not found"
            )

        if post.user_id != user_id:
            raise PermissionDeniedError(
                "You do not own this post"
            )

        return post

    def _commit_update(
        self,
        post: Post,
    ) -> Post:
        try:
            post = self.repository.update(post)

            self.db.commit()
            self.db.refresh(post)

            return post

        except Exception:
            self.db.rollback()
            raise