from collections.abc import Callable

from sqlalchemy import event
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from app.models import Post, User
from app.repositories.post_repository import (
    PostRepository,
)
from app.repositories.user_repository import (
    UserRepository,
)


def count_select_queries(
    db_session: Session,
    operation: Callable,
) -> int:
    engine = db_session.get_bind()

    if not isinstance(
        engine,
        Engine,
    ):
        raise RuntimeError(
            "Expected Session to be bound "
            "to an Engine"
        )

    statements: list[str] = []

    def before_cursor_execute(
        connection,
        cursor,
        statement,
        parameters,
        context,
        executemany,
    ):
        normalized = (
            statement
            .lstrip()
            .upper()
        )

        if normalized.startswith(
            "SELECT"
        ):
            statements.append(
                statement
            )

    event.listen(
        engine,
        "before_cursor_execute",
        before_cursor_execute,
    )

    try:
        operation()

    finally:
        event.remove(
            engine,
            "before_cursor_execute",
            before_cursor_execute,
        )

    return len(statements)


def seed_users_and_posts(
    db_session: Session,
) -> None:
    users = []

    for index in range(3):
        user = User(
            name=(
                f"Query User {index}"
            ),
            email=(
                f"query-user-{index}"
                "@example.com"
            ),
            role="user",
            password="test-hash",
            full_name=(
                f"Query User {index}"
            ),
        )

        db_session.add(user)
        users.append(user)

    db_session.flush()

    for index, user in enumerate(
        users
    ):
        db_session.add(
            Post(
                title=(
                    f"Query Post {index}"
                ),
                content="Content",
                user_id=user.id,
            )
        )

    db_session.commit()

    db_session.expunge_all()


def test_user_list_uses_two_select_queries(
    db_session,
):
    seed_users_and_posts(
        db_session
    )

    repository = UserRepository(
        db_session
    )

    query_count = (
        count_select_queries(
            db_session,
            lambda: repository.get_all(
                limit=10,
                offset=0,
            ),
        )
    )

    # SELECT users
    # +
    # SELECT posts WHERE user_id IN (...)
    assert query_count == 2


def test_post_list_uses_one_select_query(
    db_session,
):
    seed_users_and_posts(
        db_session
    )

    repository = PostRepository(
        db_session
    )

    query_count = (
        count_select_queries(
            db_session,
            lambda: repository.get_all(
                limit=10,
                offset=0,
            ),
        )
    )

    # Post.owner is many-to-one,
    # so joinedload can load everything
    # in one SELECT.
    assert query_count == 1