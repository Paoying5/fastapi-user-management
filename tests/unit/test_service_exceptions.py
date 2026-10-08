import pytest

from app.core.exceptions import (
    PermissionDeniedError,
    ResourceNotFoundError,
)
from app.models import Post, User
from app.schemas.post import PostUpdate
from app.services.post_service import PostService
from app.services.user_service import UserService


def test_user_service_not_found(
    db_session,
):
    service = UserService(
        db_session
    )

    with pytest.raises(
        ResourceNotFoundError
    ) as exc_info:
        service.get_user(
            999999
        )

    assert (
        exc_info.value.message
        == "User not found"
    )


def test_post_service_not_found(
    db_session,
):
    service = PostService(
        db_session
    )

    with pytest.raises(
        ResourceNotFoundError
    ) as exc_info:
        service.get_post(
            999999
        )

    assert (
        exc_info.value.message
        == "Post not found"
    )


def test_post_service_rejects_non_owner(
    db_session,
):
    owner = User(
        name="Owner",
        email="owner-service@example.com",
        role="user",
        password="hashed-password",
        full_name="Owner",
    )

    other_user = User(
        name="Other User",
        email="other-service@example.com",
        role="user",
        password="hashed-password",
        full_name="Other User",
    )

    db_session.add_all(
        [
            owner,
            other_user,
        ]
    )

    db_session.commit()

    post = Post(
        title="Owned Post",
        content="Content",
        user_id=owner.id,
    )

    db_session.add(post)
    db_session.commit()
    db_session.refresh(post)

    service = PostService(
        db_session
    )

    update_data = PostUpdate(
        title="Updated Post",
        content="Updated Content",
    )

    with pytest.raises(
        PermissionDeniedError
    ) as exc_info:
        service.update_post(
            post.id,
            update_data,
            other_user.id,
        )

    assert (
        exc_info.value.message
        == "You do not own this post"
    )