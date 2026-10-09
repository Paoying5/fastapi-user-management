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


def create_post(
    client,
    *,
    title: str,
):
    response = client.post(
        "/posts/",
        json={
            "title": title,
            "content": "Pagination content",
        },
    )

    assert response.status_code == 201

    return response.json()


def test_users_pagination_headers(
    admin_client,
):
    for index in range(3):
        create_user(
            admin_client,
            name=f"Page User {index}",
            email=(
                f"page-user-{index}"
                "@example.com"
            ),
        )

    response = admin_client.get(
        "/users/",
        params={
            "search": "Page User",
            "limit": 2,
            "offset": 1,
        },
    )

    assert response.status_code == 200

    body = response.json()

    assert (
        body["status"]
        == "success"
    )

    assert len(
        body["data"]
    ) == 2

    assert (
        response.headers[
            "X-Total-Count"
        ]
        == "3"
    )

    assert (
        response.headers[
            "X-Limit"
        ]
        == "2"
    )

    assert (
        response.headers[
            "X-Offset"
        ]
        == "1"
    )

    assert (
        response.headers[
            "X-Has-More"
        ]
        == "false"
    )


def test_posts_pagination_headers(
    user_client,
):
    for index in range(3):
        create_post(
            user_client,
            title=(
                f"Pagination Post {index}"
            ),
        )

    response = user_client.get(
        "/posts/",
        params={
            "search":
                "Pagination Post",
            "limit": 2,
            "offset": 0,
        },
    )

    assert response.status_code == 200

    body = response.json()

    assert len(body) == 2

    assert (
        response.headers[
            "X-Total-Count"
        ]
        == "3"
    )

    assert (
        response.headers[
            "X-Limit"
        ]
        == "2"
    )

    assert (
        response.headers[
            "X-Offset"
        ]
        == "0"
    )

    assert (
        response.headers[
            "X-Has-More"
        ]
        == "true"
    )