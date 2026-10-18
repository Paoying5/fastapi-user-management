def create_user(
    client,
    *,
    email: str,
):
    response = client.post(
        "/users/",
        json={
            "name": "Lifecycle User",
            "email": email,
            "password": "123456",
            "full_name": "Lifecycle User",
        },
    )

    assert response.status_code == 201

    return response.json()["data"]


def login(
    client,
    *,
    email: str,
):
    return client.post(
        "/auth/login",
        data={
            "username": email,
            "password": "123456",
        },
    )


def test_new_user_has_lifecycle_fields(
    client,
):
    user = create_user(
        client,
        email="lifecycle-fields@example.com",
    )

    assert user["is_active"] is True
    assert user["created_at"] is not None
    assert user["updated_at"] is not None
    assert user["last_login_at"] is None


def test_login_updates_last_login_at(
    client,
):
    email = "last-login@example.com"

    create_user(
        client,
        email=email,
    )

    login_response = login(
        client,
        email=email,
    )

    assert login_response.status_code == 200

    token = login_response.json()[
        "access_token"
    ]

    response = client.get(
        "/auth/me",
        headers={
            "Authorization": (
                f"Bearer {token}"
            ),
        },
    )

    assert response.status_code == 200

    assert (
        response.json()["last_login_at"]
        is not None
    )


def test_inactive_user_cannot_login(
    client,
    admin_client,
):
    email = "inactive-login@example.com"

    user = create_user(
        client,
        email=email,
    )

    deactivate_response = admin_client.patch(
        f"/users/{user['id']}",
        json={
            "is_active": False,
        },
    )

    assert (
        deactivate_response.status_code
        == 200
    )

    login_response = login(
        client,
        email=email,
    )

    assert (
        login_response.status_code
        == 401
    )


def test_existing_token_rejected_after_deactivation(
    client,
    admin_client,
):
    email = "inactive-token@example.com"

    user = create_user(
        client,
        email=email,
    )

    login_response = login(
        client,
        email=email,
    )

    assert login_response.status_code == 200

    token = login_response.json()[
        "access_token"
    ]

    deactivate_response = admin_client.patch(
        f"/users/{user['id']}",
        json={
            "is_active": False,
        },
    )

    assert (
        deactivate_response.status_code
        == 200
    )

    response = client.get(
        "/auth/me",
        headers={
            "Authorization": (
                f"Bearer {token}"
            ),
        },
    )

    assert response.status_code == 403

    assert (
        response.json()["detail"]
        == "Inactive user"
    )


def test_post_default_status_is_published(
    user_client,
):
    response = user_client.post(
        "/posts/",
        json={
            "title": "Published Post",
            "content": "Content",
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["status"] == "published"
    assert data["created_at"] is not None
    assert data["updated_at"] is not None


def test_post_status_can_be_changed(
    user_client,
):
    create_response = user_client.post(
        "/posts/",
        json={
            "title": "Lifecycle Post",
            "content": "Lifecycle content",
        },
    )

    assert (
        create_response.status_code
        == 201
    )

    post_id = create_response.json()["id"]

    response = user_client.patch(
        f"/posts/{post_id}",
        json={
            "status": "archived",
        },
    )

    assert response.status_code == 200

    assert (
        response.json()["status"]
        == "archived"
    )


def test_invalid_post_status_rejected(
    user_client,
):
    response = user_client.post(
        "/posts/",
        json={
            "title": "Invalid Status",
            "content": "Content",
            "status": "deleted",
        },
    )

    assert response.status_code == 422