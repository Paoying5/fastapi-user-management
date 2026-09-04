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

    print(response.status_code)
    print(response.text)

    assert response.status_code == 201

    body = response.json()

    assert body["success"] is True

    assert body["data"]["email"] == email