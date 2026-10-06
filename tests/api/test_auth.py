from jose import jwt

from app.core.config import settings
from app.core.security import create_access_token


def create_user(
    client,
    *,
    name: str,
    email: str,
    password: str = "123456",
):
    response = client.post(
        "/users/",
        json={
            "name": name,
            "email": email,
            "password": password,
            "full_name": name,
        },
    )

    assert response.status_code == 201

    return response.json()["data"]


def login(
    client,
    *,
    email: str,
    password: str = "123456",
):
    return client.post(
        "/auth/login",
        data={
            "username": email,
            "password": password,
        },
    )


def test_login_success(client):
    user = create_user(
        client,
        name="Login User",
        email="login@example.com",
    )

    response = login(
        client,
        email="login@example.com",
    )

    assert response.status_code == 200

    data = response.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"

    payload = jwt.decode(
        data["access_token"],
        settings.SECRET_KEY,
        algorithms=[
            settings.ALGORITHM,
        ],
    )

    assert payload["sub"] == str(
        user["id"]
    )


def test_login_wrong_password(client):
    create_user(
        client,
        name="Wrong Password",
        email="wrong-password@example.com",
    )

    response = login(
        client,
        email="wrong-password@example.com",
        password="wrong-password",
    )

    assert response.status_code == 401
    assert (
        response.json()["detail"]
        == "Invalid email or password"
    )


def test_login_unknown_user(client):
    response = login(
        client,
        email="notfound@example.com",
    )

    assert response.status_code == 401
    assert (
        response.json()["detail"]
        == "Invalid email or password"
    )


def test_auth_me_with_valid_token(client):
    user = create_user(
        client,
        name="Current User",
        email="current-user@example.com",
    )

    login_response = login(
        client,
        email="current-user@example.com",
    )

    assert (
        login_response.status_code
        == 200
    )

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

    data = response.json()

    assert data["id"] == user["id"]
    assert (
        data["email"]
        == "current-user@example.com"
    )


def test_auth_me_with_invalid_token(
    client,
):
    response = client.get(
        "/auth/me",
        headers={
            "Authorization": (
                "Bearer invalid-token"
            ),
        },
    )

    assert response.status_code == 401

    assert (
        response.json()["detail"]
        == "Could not validate credentials"
    )

    assert (
        response.headers[
            "www-authenticate"
        ]
        == "Bearer"
    )


def test_legacy_email_subject_token_still_works(
    client,
):
    user = create_user(
        client,
        name="Legacy User",
        email="legacy@example.com",
    )

    legacy_token = create_access_token(
        {
            "sub": "legacy@example.com",
        }
    )

    response = client.get(
        "/auth/me",
        headers={
            "Authorization": (
                f"Bearer {legacy_token}"
            ),
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == user["id"]
    assert (
        data["email"]
        == "legacy@example.com"
    )