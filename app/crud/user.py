from sqlalchemy.orm import Session, joinedload

from app.core.security import hash_password
from app.models import User
from app.schemas import UserCreate, UserPatch, UserUpdate, user


def get_users(db: Session) -> list[User]:
    return (
        db.query(User)
        .options(joinedload(User.posts))
        .order_by(User.id.asc())
        .all()
    )


def get_user(
    db: Session,
    user_id: int,
) -> User | None:
    return (
        db.query(User)
        .options(joinedload(User.posts))
        .filter(User.id == user_id)
        .first()
    )


def get_user_by_email(
    db: Session,
    email: str,
) -> User | None:
    return (
        db.query(User)
        .filter(User.email == email)
        .first()
    )


def create_user(
    db: Session,
    user_data: UserCreate,
) -> User:
    db_user = User(
        name=user_data.name,
        email=user_data.email,
        role=user_data.role,
        password=hash_password(user_data.password),
        full_name=user.full_name
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def update_user(
    db: Session,
    user_id: int,
    user_data: UserUpdate,
) -> User | None:
    db_user = get_user(db, user_id)

    if db_user is None:
        return None

    db_user.name = user_data.name
    db_user.email = user_data.email
    db_user.role = user_data.role

    db.commit()
    db.refresh(db_user)

    return db_user


def patch_user(
    db: Session,
    user_id: int,
    user_data: UserPatch,
) -> User | None:
    db_user = get_user(db, user_id)

    if db_user is None:
        return None

    update_data = user_data.model_dump(
        exclude_unset=True,
    )

    for field_name, value in update_data.items():
        setattr(db_user, field_name, value)

    db.commit()
    db.refresh(db_user)

    return db_user


def delete_user(
    db: Session,
    user_id: int,
) -> bool:
    db_user = get_user(db, user_id)

    if db_user is None:
        return False

    db.delete(db_user)
    db.commit()

    return True