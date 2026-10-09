import pytest
from sqlalchemy import select, text
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models import Post, User


pytestmark = pytest.mark.integration


def make_user(
    email: str,
    name: str = "Integration User",
    role: str = "user",
) -> User:
    return User(
        name=name,
        email=email,
        role=role,
        password="integration-test-hash",
        full_name=name,
    )


def test_duplicate_email_constraint(
    pg_session: Session,
):
    first_user = make_user(
        email="duplicate-pg@example.com",
        name="First User",
    )

    pg_session.add(
        first_user
    )

    pg_session.flush()

    second_user = make_user(
        email="duplicate-pg@example.com",
        name="Second User",
    )

    pg_session.add(
        second_user
    )

    with pytest.raises(
        IntegrityError
    ):
        pg_session.flush()

    pg_session.rollback()


def test_invalid_role_check_constraint(
    pg_session: Session,
):
    user = make_user(
        email="invalid-role-pg@example.com",
        role="superadmin",
    )

    pg_session.add(
        user
    )

    with pytest.raises(
        IntegrityError
    ):
        pg_session.flush()

    pg_session.rollback()


def test_role_not_null_constraint(
    pg_session: Session,
):
    with pytest.raises(
        IntegrityError
    ):
        pg_session.execute(
            text(
                """
                INSERT INTO users (
                    name,
                    email,
                    role,
                    password,
                    full_name
                )
                VALUES (
                    :name,
                    :email,
                    NULL,
                    :password,
                    :full_name
                )
                """
            ),
            {
                "name": "Null Role User",
                "email":
                    "null-role-pg@example.com",
                "password":
                    "integration-test-hash",
                "full_name":
                    "Null Role User",
            },
        )

    pg_session.rollback()


def test_post_user_foreign_key_constraint(
    pg_session: Session,
):
    post = Post(
        title="Invalid Owner Post",
        content="Integration test",
        user_id=999999999,
    )

    pg_session.add(
        post
    )

    with pytest.raises(
        IntegrityError
    ):
        pg_session.flush()

    pg_session.rollback()


def test_ilike_is_case_insensitive(
    pg_session: Session,
):
    user = make_user(
        email="mixed-case@example.com",
        name="MiXeDCaseUser",
    )

    pg_session.add(
        user
    )

    pg_session.flush()

    statement = select(
        User
    ).where(
        User.name.ilike(
            "%mixedcaseuser%"
        )
    )

    result = pg_session.scalars(
        statement
    ).all()

    assert len(result) == 1

    assert (
        result[0].email
        == "mixed-case@example.com"
    )