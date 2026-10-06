def create_user(
    client,
    *,
    name: str,
    email: str,
):
    response = client.post(
        "/users/",
        json={
            "name": name,
            "email": email,
            "password": "123456",
            "full_name": name,
        },
    )

    assert response.status_code == 201

    return response.json()["data"]


def test_create_user_rejects_whitespace_name(
    client,
):
    response = client.post(
        "/users/",
        json={
            "name": "   ",
            "email": "whitespace@example.com",
            "password": "123456",
            "full_name": "Whitespace User",
        },
    )

    assert response.status_code == 422


def test_create_user_rejects_extra_role(
    client,
):
    response = client.post(
        "/users/",
        json={
            "name": "Normal User",
            "email": "extra-role@example.com",
            "password": "123456",
            "full_name": "Normal User",
            "role": "admin",
        },
    )

    assert response.status_code == 422


def test_patch_user_rejects_null_name(
    admin_client,
):
    user = create_user(
        admin_client,
        name="Patch User",
        email="patch-null@example.com",
    )

    response = admin_client.patch(
        f"/users/{user['id']}",
        json={
            "name": None,
        },
    )

    assert response.status_code == 422


def test_create_post_rejects_whitespace_title(
    user_client,
):
    response = user_client.post(
        "/posts/",
        json={
            "title": "   ",
            "content": "Content",
        },
    )

    assert response.status_code == 422


def test_patch_post_rejects_null_title(
    user_client,
):
    create_response = user_client.post(
        "/posts/",
        json={
            "title": "Valid Post",
            "content": "Content",
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
            "title": None,
        },
    )

    assert response.status_code == 422


def test_create_post_rejects_extra_user_id(
    user_client,
):
    response = user_client.post(
        "/posts/",
        json={
            "title": "Secure Post",
            "content": "Content",
            "user_id": 999999,
        },
    )

    assert response.status_code == 422