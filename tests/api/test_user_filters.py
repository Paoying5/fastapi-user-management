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


def test_filter_users_by_user_role(admin_client):
    create_user(
        admin_client,
        name="Alpha User",
        email="alpha-filter@example.com",
    )
    create_user(
        admin_client,
        name="Beta User",
        email="beta-filter@example.com",
    )

    response = admin_client.get(
        "/users/",
        params={"role": "user"},
    )

    assert response.status_code == 200

    body = response.json()

    assert len(body["data"]) == 2
    assert all(
        user["role"] == "user"
        for user in body["data"]
    )
    assert response.headers["X-Total-Count"] == "2"


def test_filter_users_by_admin_role(admin_client):
    create_user(
        admin_client,
        name="Normal User",
        email="normal-filter@example.com",
    )

    response = admin_client.get(
        "/users/",
        params={"role": "admin"},
    )

    assert response.status_code == 200

    body = response.json()

    assert len(body["data"]) == 1
    assert all(
        user["role"] == "admin"
        for user in body["data"]
    )
    assert response.headers["X-Total-Count"] == "1"


def test_role_filter_combines_with_search(admin_client):
    create_user(
        admin_client,
        name="Alpha User",
        email="alpha-search@example.com",
    )

    response = admin_client.get(
        "/users/",
        params={
            "role": "admin",
            "search": "Alpha",
        },
    )

    assert response.status_code == 200

    body = response.json()

    assert body["data"] == []
    assert response.headers["X-Total-Count"] == "0"


def test_invalid_role_returns_422(admin_client):
    response = admin_client.get(
        "/users/",
        params={"role": "superadmin"},
    )

    assert response.status_code == 422
