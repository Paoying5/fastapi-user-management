import pytest
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

from app.core.security import hash_password
from app.models import User
from app.schemas.user import UserCreate
from app.services.user_service import UserService


def test_user_default_role_is_user(
    db_session,
):
    user = User(
        name="Default Role User",
        email="default-role@example.com",
        password=hash_password("123456"),
        full_name="Default Role User",
    )

    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)

    assert user.role == "user"


def test_database_rejects_invalid_role(
    db_session,
):
    user = User(
        name="Invalid Role User",
        email="invalid-role-db@example.com",
        role="superadmin",
        password=hash_password("123456"),
        full_name="Invalid Role User",
    )

    db_session.add(user)

    with pytest.raises(IntegrityError):
        db_session.commit()

    db_session.rollback()


def test_database_unique_constraint_rejects_duplicate_email(
    db_session,
):
    first_user = User(
        name="First User",
        email="duplicate-db@example.com",
        role="user",
        password=hash_password("123456"),
        full_name="First User",
    )

    second_user = User(
        name="Second User",
        email="duplicate-db@example.com",
        role="user",
        password=hash_password("123456"),
        full_name="Second User",
    )

    db_session.add(first_user)
    db_session.commit()

    db_session.add(second_user)

    with pytest.raises(IntegrityError):
        db_session.commit()

    db_session.rollback()


def test_service_converts_unique_race_to_409(
    db_session,
    monkeypatch,
):
    existing_user = User(
        name="Existing User",
        email="race@example.com",
        role="user",
        password=hash_password("123456"),
        full_name="Existing User",
    )

    db_session.add(existing_user)
    db_session.commit()

    service = UserService(
        db_session
    )

    # Simulate a race:
    #
    # The application-level SELECT believes
    # the email is still available,
    # but the database already contains it.
    monkeypatch.setattr(
        service.repository,
        "get_by_email",
        lambda email: None,
    )

    user_data = UserCreate(
        name="Race User",
        email="race@example.com",
        password="123456",
        full_name="Race User",
    )

    with pytest.raises(
        HTTPException
    ) as exc_info:
        service.create_user(
            user_data
        )

    assert (
        exc_info.value.status_code
        == 409
    )

    assert (
        exc_info.value.detail
        == "Email already exists"
    )