import uuid


def test_create_user(client):
    email = f"{uuid.uuid4()}@gmail.com"

    payload = {
        "name": "Test User",
        "full_name": "Test User",
        "email": email,
        "password": "12345678",
    }

    response = client.post(
        "/users/",
        json=payload,
    )

    assert response.status_code == 201

    body = response.json()

    assert body["status"] == "success"
    assert body["data"]["name"] == "Test User"
    assert body["data"]["full_name"] == "Test User"
    assert body["data"]["email"] == email
    assert body["data"]["role"] == "user"
    assert "password" not in body["data"]