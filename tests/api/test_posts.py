def create_user(client, name, email):
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


def login(client, email):
    response = client.post(
        "/auth/login",
        data={
            "username": email,
            "password": "123456",
        },
    )
    assert response.status_code == 200

    token = response.json()["access_token"]
    client.headers.update(
        {"Authorization": f"Bearer {token}"}
    )


def create_post(client, title="Test Post", content="Test content"):
    response = client.post(
        "/posts/",
        json={
            "title": title,
            "content": content,
        },
    )
    assert response.status_code == 201
    return response.json()


def test_create_post(client):
    create_user(
        client,
        "Post User",
        "postuser@example.com",
    )
    login(client, "postuser@example.com")

    response = create_post(client)

    assert response["id"] > 0
    assert response["title"] == "Test Post"
    assert response["content"] == "Test content"
    assert response["user_id"] > 0
    assert response["owner"]["email"] == "postuser@example.com"


def test_create_post_unauthorized(client):
    response = client.post(
        "/posts/",
        json={
            "title": "Unauthorized Post",
            "content": "Content",
        },
    )

    assert response.status_code == 401


def test_get_posts(client):
    create_user(
        client,
        "Post User",
        "getposts@example.com",
    )
    login(client, "getposts@example.com")

    create_post(client, "Post 1", "Content 1")
    create_post(client, "Post 2", "Content 2")

    response = client.get("/posts/")

    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, list)
    assert len(data) == 2

    titles = {post["title"] for post in data}

    assert titles == {"Post 1", "Post 2"}


def test_get_posts_search(client):
    create_user(
        client,
        "Search User",
        "search@example.com",
    )
    login(client, "search@example.com")

    create_post(client, "Python FastAPI", "Backend")
    create_post(client, "SQLAlchemy", "Database")

    response = client.get(
        "/posts/",
        params={"search": "FastAPI"},
    )

    assert response.status_code == 200
    data = response.json()

    assert len(data) == 1
    assert data[0]["title"] == "Python FastAPI"


def test_get_my_posts(client):
    create_user(
        client,
        "My Post User",
        "myposts@example.com",
    )
    login(client, "myposts@example.com")

    create_post(client, "My Post", "My content")

    response = client.get("/posts/me")

    assert response.status_code == 200
    data = response.json()

    assert len(data) == 1
    assert data[0]["title"] == "My Post"


def test_get_post(client):
    create_user(
        client,
        "Get User",
        "getpost@example.com",
    )
    login(client, "getpost@example.com")

    post = create_post(client)

    response = client.get(f"/posts/{post['id']}")

    assert response.status_code == 200
    data = response.json()

    assert data["id"] == post["id"]
    assert data["title"] == "Test Post"


def test_get_post_not_found(client):
    response = client.get("/posts/999999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Post not found"


def test_update_post(client):
    create_user(
        client,
        "Update User",
        "update@example.com",
    )
    login(client, "update@example.com")

    post = create_post(client)

    response = client.put(
        f"/posts/{post['id']}",
        json={
            "title": "Updated Title",
            "content": "Updated content",
        },
    )

    assert response.status_code == 200
    data = response.json()

    assert data["title"] == "Updated Title"
    assert data["content"] == "Updated content"


def test_patch_post(client):
    create_user(
        client,
        "Patch User",
        "patch@example.com",
    )
    login(client, "patch@example.com")

    post = create_post(client)

    response = client.patch(
        f"/posts/{post['id']}",
        json={
            "title": "Patched Title",
        },
    )

    assert response.status_code == 200
    data = response.json()

    assert data["title"] == "Patched Title"
    assert data["content"] == "Test content"


def test_delete_post(client):
    create_user(
        client,
        "Delete User",
        "delete@example.com",
    )
    login(client, "delete@example.com")

    post = create_post(client)

    response = client.delete(
        f"/posts/{post['id']}"
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Post deleted successfully"

    response = client.get(
        f"/posts/{post['id']}"
    )

    assert response.status_code == 404


def test_post_ownership_forbidden(client):
    create_user(
        client,
        "Owner User",
        "owner@example.com",
    )
    login(client, "owner@example.com")

    post = create_post(client)

    # Tạo user thứ hai
    client.headers.pop("Authorization", None)

    create_user(
        client,
        "Other User",
        "other@example.com",
    )
    login(client, "other@example.com")

    response = client.put(
        f"/posts/{post['id']}",
        json={
            "title": "Hacked",
            "content": "Hacked",
        },
    )

    assert response.status_code == 403
    assert response.json()["detail"] == "You do not own this post"


def test_create_post_invalid_title(client):
    create_user(
        client,
        "Validation User",
        "validation@example.com",
    )
    login(client, "validation@example.com")

    response = client.post(
        "/posts/",
        json={
            "title": "A",
            "content": "Content",
        },
    )

    assert response.status_code == 422

