from sqlalchemy import desc
from sqlalchemy.orm import Session, joinedload

from app.models import Post
from app.schemas import (
    PostCreate,
    PostPatch,
    PostUpdate,
)


def create_post(
    db: Session,
    post_data: PostCreate,
    user_id: int,
) -> Post:
    db_post = Post(
        title=post_data.title,
        content=post_data.content,
        user_id=user_id,
    )

    db.add(db_post)
    db.commit()
    db.refresh(db_post)

    return get_post(db, db_post.id)


def get_posts(
    db: Session,
    limit: int = 10,
    offset: int = 0,
    search: str = "",
) -> list[Post]:
    query = (
        db.query(Post)
        .options(joinedload(Post.owner))
    )

    if search:
        query = query.filter(
            Post.title.ilike(f"%{search}%"),
        )

    return (
        query
        .order_by(desc(Post.id))
        .offset(offset)
        .limit(limit)
        .all()
    )


def get_post(
    db: Session,
    post_id: int,
) -> Post | None:
    return (
        db.query(Post)
        .options(joinedload(Post.owner))
        .filter(Post.id == post_id)
        .first()
    )


def get_my_posts(
    db: Session,
    user_id: int,
) -> list[Post]:
    return (
        db.query(Post)
        .options(joinedload(Post.owner))
        .filter(Post.user_id == user_id)
        .order_by(desc(Post.id))
        .all()
    )


def update_post(
    db: Session,
    post_id: int,
    post_data: PostUpdate,
    user_id: int,
) -> Post | None | bool:
    db_post = get_post(db, post_id)

    if db_post is None:
        return None

    if db_post.user_id != user_id:
        return False

    db_post.title = post_data.title
    db_post.content = post_data.content

    db.commit()
    db.refresh(db_post)

    return db_post


def patch_post(
    db: Session,
    post_id: int,
    post_data: PostPatch,
    user_id: int,
) -> Post | None | bool:
    db_post = get_post(db, post_id)

    if db_post is None:
        return None

    if db_post.user_id != user_id:
        return False

    update_data = post_data.model_dump(
        exclude_unset=True,
    )

    for field_name, value in update_data.items():
        setattr(db_post, field_name, value)

    db.commit()
    db.refresh(db_post)

    return db_post


def delete_post(
    db: Session,
    post_id: int,
    user_id: int,
) -> bool | None:
    db_post = get_post(db, post_id)

    if db_post is None:
        return None

    if db_post.user_id != user_id:
        return False

    db.delete(db_post)
    db.commit()

    return True