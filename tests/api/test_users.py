def test_get_users(auth_client):
    response = auth_client.get("/users/")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "success"
    assert isinstance(data["data"], list)


def test_get_users_unauthorized(client):
    response = client.get("/users/")

    assert response.status_code == 401

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
    assert data["data"]["name"] == "testuser"
    assert data["data"]["email"] == "testuser@example.com"
    assert data["data"]["role"] == "user"
    assert data["data"]["full_name"] == "Test User"

    assert "password" not in data["data"]


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

    assert first_response.status_code == 201

    second_response = client.post(
        "/users/",
        json=payload,
    )

    assert second_response.status_code == 409
    assert second_response.json()["detail"] == "Email already exists"


def test_create_user_invalid_password(client):
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