import uuid

from playwright.sync_api import expect

from tests.e2e.utils import (
    click_execute,
    click_try_it_out,
    fill_request_body,
    get_post_endpoint,
    open_swagger,
    screenshot,
)


def create_test_user(page, prefix: str) -> tuple[str, str]:
    email = (
        f"swagger-{prefix}-{uuid.uuid4().hex[:8]}"
        "@example.com"
    )
    password = "123456"

    response = page.request.post(
        "http://api:8000/users/",
        data={
            "name": f"Swagger {prefix} User",
            "email": email,
            "password": password,
            "full_name": f"Swagger {prefix} User",
        },
    )

    assert response.status == 201, (
        f"Failed to create test user: "
        f"{response.status} "
        f"{response.text()}"
    )

    return email, password


def create_test_post(
    page,
    email: str,
    password: str,
    title: str,
    content: str,
) -> tuple[str, int]:
    login_response = page.request.post(
        "http://api:8000/auth/login",
        form={
            "username": email,
            "password": password,
        },
    )

    assert login_response.status == 200, (
        f"Login failed: "
        f"{login_response.status} "
        f"{login_response.text()}"
    )

    token = login_response.json()["access_token"]

    post_response = page.request.post(
        "http://api:8000/posts/",
        headers={
            "Authorization": f"Bearer {token}",
        },
        data={
            "title": title,
            "content": content,
        },
    )

    assert post_response.status == 201, (
        f"Failed to create test post: "
        f"{post_response.status} "
        f"{post_response.text()}"
    )

    post_id = post_response.json()["id"]

    return token, post_id

def authorize_swagger(
    page,
    email: str,
    password: str,
) -> None:
    authorize_button = page.get_by_role(
        "button",
        name="Authorize",
    )

    expect(authorize_button).to_be_visible()
    authorize_button.click()

    dialog = page.locator(".modal-ux")

    expect(dialog).to_be_visible()

    username_input = dialog.get_by_role(
        "textbox",
        name="username:",
    )

    password_input = dialog.get_by_role(
        "textbox",
        name="password:",
    )

    username_input.fill(email)
    password_input.fill(password)

    apply_button = dialog.get_by_role(
        "button",
        name="Apply given OAuth2 credentials",
    )

    expect(apply_button).to_be_enabled()
    apply_button.click()

    page.evaluate("""
        () => {
            document.querySelectorAll(
                '.modal-ux, .dialog-ux, .backdrop-ux'
            ).forEach(element => {
                element.remove();
            });
        }
    """)

    authorization_button = page.get_by_role(
        "button",
        name="authorization button unlocked",
    ).first

    expect(authorization_button).to_be_visible()



def fill_post_id(endpoint, post_id: int) -> None:
    post_id_input = endpoint.get_by_role(
        "textbox",
        name="post_id",
    )

    expect(post_id_input).to_be_visible()
    post_id_input.fill(str(post_id))


def test_swagger_create_post(page):
    email, password = create_test_user(
        page,
        "post",
    )

    open_swagger(page)

    authorize_swagger(
        page,
        email,
        password,
    )

    endpoint = get_post_endpoint(
        page,
        "/posts/",
    )

    endpoint.locator(".opblock-summary").click()

    click_try_it_out(endpoint)

    fill_request_body(
        endpoint,
        """{
            "title": "Swagger E2E Post",
            "content": "Post created through Swagger UI E2E test"
}""",
    )

    click_execute(endpoint)

    response_section = endpoint.locator(
        ".responses-inner"
    )

    expect(response_section).to_contain_text("201")
    expect(response_section).to_contain_text(
        "Swagger E2E Post"
    )
    expect(response_section).to_contain_text(
        "Post created through Swagger UI E2E test"
    )
    expect(response_section).to_contain_text(email)

    screenshot(
            page,
            "swagger/06_create_post_success.png",
        )


def test_swagger_get_posts(page):
    email, password = create_test_user(
        page,
        "get-posts",
    )

    create_test_post(
        page,
        email,
        password,
        "Swagger GET Posts Test",
        "Post for GET /posts/ E2E test",
    )

    open_swagger(page)

    endpoint = (
        page.locator(".opblock-get")
        .filter(has_text="/posts/")
        .first
    )

    expect(endpoint).to_be_visible()

    endpoint.locator(".opblock-summary").click()

    click_try_it_out(endpoint)
    click_execute(endpoint)

    response_section = endpoint.locator(
        ".responses-inner"
    )

    expect(response_section).to_contain_text("200")
    expect(response_section).to_contain_text(
        "Swagger GET Posts Test"
    )
    expect(response_section).to_contain_text(
        "Post for GET /posts/ E2E test"
    )
    expect(response_section).to_contain_text(email)

    screenshot(
        page,
        "swagger/07_get_posts_success.png",
    )


def test_swagger_get_post_by_id(page):
    email, password = create_test_user(
        page,
        "get-post",
    )

    _, post_id = create_test_post(
        page,
        email,
        password,
        "Swagger GET Post By ID",
        "Post for GET /posts/{post_id} E2E test",
    )

    open_swagger(page)

    endpoint = (
        page.locator(".opblock-get")
        .filter(has_text="/posts/{post_id}")
        .first
    )

    expect(endpoint).to_be_visible()

    endpoint.locator(".opblock-summary").click()

    click_try_it_out(endpoint)

    fill_post_id(
        endpoint,
        post_id,
    )

    click_execute(endpoint)

    response_section = endpoint.locator(
        ".responses-inner"
    )

    expect(response_section).to_contain_text("200")
    expect(response_section).to_contain_text(
        "Swagger GET Post By ID"
    )
    expect(response_section).to_contain_text(
        "Post for GET /posts/{post_id} E2E test"
    )
    expect(response_section).to_contain_text(email)

    screenshot(
        page,
        "swagger/08_get_post_by_id_success.png",
    )


def test_swagger_update_post(page):
    email, password = create_test_user(
        page,
        "update-post",
    )

    _, post_id = create_test_post(
        page,
        email,
        password,
        "Original Post Title",
        "Original post content",
    )

    open_swagger(page)

    authorize_swagger(
        page,
        email,
        password,
    )

    endpoint = (
        page.locator(".opblock-put")
        .filter(has_text="/posts/{post_id}")
        .first
    )

    expect(endpoint).to_be_visible()

    endpoint.locator(".opblock-summary").click()

    click_try_it_out(endpoint)

    fill_post_id(
        endpoint,
        post_id,
    )

    fill_request_body(
        endpoint,
        """{
  "title": "Updated Post Title",
  "content": "Updated post content"
}""",
    )

    click_execute(endpoint)

    response_section = endpoint.locator(
        ".responses-inner"
    )

    expect(response_section).to_contain_text("200")
    expect(response_section).to_contain_text(
        "Updated Post Title"
    )
    expect(response_section).to_contain_text(
        "Updated post content"
    )
    expect(response_section).to_contain_text(email)

    screenshot(
        page,
        "swagger/09_update_post_success.png",
    )