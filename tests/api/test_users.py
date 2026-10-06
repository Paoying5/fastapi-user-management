def test_get_users(admin_client):
    response = admin_client.get(
        "/users/"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "success"
    assert isinstance(
        data["data"],
        list,
    )


def test_get_users_unauthorized(client):
    response = client.get(
        "/users/"
    )

    assert response.status_code == 401


def test_get_users_forbidden_for_normal_user(
    user_client,
):
    response = user_client.get(
        "/users/"
    )

    assert response.status_code == 403

    assert (
        response.json()["detail"]
        == "Admin access required"
    )


def test_create_user(client):
    response = client.post(
        "/users/",
        json={
            "name": "testuser",
            "email": "testuser@example.com",
            "password": "123456",
            "full_name": "Test User",
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["status"] == "success"

    assert (
        data["data"]["name"]
        == "testuser"
    )

    assert (
        data["data"]["email"]
        == "testuser@example.com"
    )

    assert (
        data["data"]["role"]
        == "user"
    )

    assert (
        data["data"]["full_name"]
        == "Test User"
    )

    assert (
        "password"
        not in data["data"]
    )


def test_create_duplicate_email(client):
    payload = {
        "name": "testuser",
        "email": "duplicate@example.com",
        "password": "123456",
        "full_name": "Test User",
    }

    first_response = client.post(
        "/users/",
        json=payload,
    )

    assert (
        first_response.status_code
        == 201
    )

    second_response = client.post(
        "/users/",
        json=payload,
    )

    assert (
        second_response.status_code
        == 409
    )

    assert (
        second_response.json()["detail"]
        == "Email already exists"
    )


def test_create_user_invalid_password(
    client,
):
    response = client.post(
        "/users/",
        json={
            "name": "testuser",
            "email": "invalid@example.com",
            "password": "123",
            "full_name": "Invalid User",
        },
    )

    assert response.status_code == 422


def test_update_user_rejects_invalid_role(
    admin_client,
):
    create_response = admin_client.post(
        "/users/",
        json={
            "name": "Role User",
            "email": "role-user@example.com",
            "password": "123456",
            "full_name": "Role User",
        },
    )

    assert (
        create_response.status_code
        == 201
    )

    user_id = create_response.json()[
        "data"
    ]["id"]

    response = admin_client.put(
        f"/users/{user_id}",
        json={
            "name": "Role User",
            "email": "role-user@example.com",
            "role": "superadmin",
            "full_name": "Role User",
        },
    )

    assert response.status_code == 422


def test_patch_user_rejects_invalid_role(
    admin_client,
):
    create_response = admin_client.post(
        "/users/",
        json={
            "name": "Patch Role User",
            "email": "patch-role@example.com",
            "password": "123456",
            "full_name": "Patch Role User",
        },
    )

    assert (
        create_response.status_code
        == 201
    )

    user_id = create_response.json()[
        "data"
    ]["id"]

    response = admin_client.patch(
        f"/users/{user_id}",
        json={
            "role": "root",
        },
    )

    assert response.status_code == 422