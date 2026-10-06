def login_user(
    client,
    email: str,
    password: str = "123456",
) -> None:
    response = client.post(
        "/auth/login",
        data={
            "username": email,
            "password": password,
        },
    )

    assert response.status_code == 200

    token = response.json()["access_token"]

    client.headers.update(
        {
            "Authorization": f"Bearer {token}",
        }
    )


def test_analytics_requires_authentication(
    client,
):
    response = client.get(
        "/analytics/users/summary"
    )

    assert response.status_code == 401


def test_analytics_rejects_normal_user(
    client,
):
    create_response = client.post(
        "/users/",
        json={
            "name": "analyticsuser",
            "email": "analytics-user@example.com",
            "password": "123456",
            "full_name": "Analytics User",
        },
    )

    assert create_response.status_code == 201

    login_user(
        client,
        "analytics-user@example.com",
    )

    response = client.get(
        "/analytics/users/summary"
    )

    assert response.status_code == 403
    assert (
        response.json()["detail"]
        == "Admin access required"
    )


def test_admin_can_get_user_analytics(
    auth_client,
):
    response = auth_client.get(
        "/analytics/users/summary"
    )

    assert response.status_code == 200

    body = response.json()

    assert body["status"] == "success"

    assert (
        body["message"]
        == "User analytics retrieved successfully"
    )

    data = body["data"]

    assert isinstance(
        data["total_users"],
        int,
    )

    assert data["total_users"] >= 1

    assert isinstance(
        data["users_by_role"],
        list,
    )

    admin_rows = [
        row
        for row in data["users_by_role"]
        if row["role"] == "admin"
    ]

    assert len(admin_rows) == 1
    assert admin_rows[0]["user_count"] >= 1