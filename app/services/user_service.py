from sqlalchemy.orm import Session

from app.crud import user as user_repository
from app.schemas.user import (
    UserCreate,
    UserUpdate,
    UserPatch,
)


def get_users(
    db: Session,
):
    return user_repository.get_users(db)


def get_user(
    db: Session,
    user_id: int,
):
    return user_repository.get_user(
        db,
        user_id,
    )


def create_user(
    db: Session,
    user: UserCreate,
):
    return user_repository.create_user(
        db,
        user,
    )


def update_user(
    db: Session,
    user_id: int,
    user: UserUpdate,
):
    return user_repository.update_user(
        db,
        user_id,
        user,
    )


def patch_user(
    db: Session,
    user_id: int,
    user: UserPatch,
):
    return user_repository.patch_user(
        db,
        user_id,
        user,
    )


def delete_user(
    db: Session,
    user_id: int,
):
    return user_repository.delete_user(
        db,
        user_id,
    )