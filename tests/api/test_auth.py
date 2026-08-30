def test_login_success(client):
    create_response = client.post(
        "/users/",
        json={
            "name": "loginuser",
            "email": "login@example.com",
            "password": "123456",
            "full_name": "Login User",
        },
    )

    assert create_response.status_code == 201

    response = client.post(
        "/auth/login",
        data={
            "username": "login@example.com",
            "password": "123456",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_login_wrong_password(client):
    client.post(
        "/users/",
        json={
            "name": "loginuser",
            "email": "wrong-password@example.com",
            "password": "123456",
            "full_name": "Wrong Password",
        },
    )

    response = client.post(
        "/auth/login",
        data={
            "username": "wrong-password@example.com",
            "password": "wrong-password",
        },
    )

    assert response.status_code == 401


def test_login_unknown_user(client):
    response = client.post(
        "/auth/login",
        data={
            "username": "notfound@example.com",
            "password": "123456",
        },
    )

    assert response.status_code == 401