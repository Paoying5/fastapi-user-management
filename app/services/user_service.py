from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.user import User

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
    user.email = user.email.strip().lower()

    if email_exists(
        db,
        user.email,
    ):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already exists",
        )

    return user_repository.create_user(
        db,
        user,
    )


def update_user(
    db: Session,
    user_id: int,
    user: UserUpdate,
):

    user.email = user.email.strip().lower()

    old_user = user_repository.get_user(
        db,
        user_id,
    )

    if old_user is None:
        return None

    if (
        old_user.email != user.email
        and email_exists(
            db,
            user.email,
        )
    ):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already exists",
        )

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

    old_user = user_repository.get_user(
        db,
        user_id,
    )

    if old_user is None:
        return None

    if user.email is not None:

        user.email = user.email.strip().lower()

        if (
            old_user.email != user.email
            and email_exists(
                db,
                user.email,
            )
        ):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already exists",
            )

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

def email_exists(
    db: Session,
    email: str,
) -> bool:

    return (
        db.query(User)
        .filter(User.email == email)
        .first()
        is not None
    )