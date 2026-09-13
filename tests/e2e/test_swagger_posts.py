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


def test_swagger_create_post(page):
    # ---------------------------------------------------------
    # 1. Create a test user through API
    # ---------------------------------------------------------
    email = (
        f"swagger-post-{uuid.uuid4().hex[:8]}"
        "@example.com"
    )
    password = "123456"

    create_response = page.request.post(
        "http://api:8000/users/",
        data={
            "name": "Swagger Post User",
            "email": email,
            "password": password,
            "full_name": "Swagger Post User",
        },
    )

    assert create_response.status == 201

    # ---------------------------------------------------------
    # 2. Open Swagger UI
    # ---------------------------------------------------------
    open_swagger(page)

    # ---------------------------------------------------------
    # 3. Authorize
    # ---------------------------------------------------------
    page.get_by_role(
        "button",
        name="Authorize",
    ).click()

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

    authorize_dialog_button = dialog.get_by_role(
        "button",
        name="Apply given OAuth2 credentials",
    )

    expect(authorize_dialog_button).to_be_enabled()

    authorize_dialog_button.click()

    # ---------------------------------------------------------
    # 4. Verify authorization and wait for modal to close
    # ---------------------------------------------------------
    authorization_button = page.get_by_role(
        "button",
        name="authorization button unlocked",
    ).first

    expect(authorization_button).to_be_visible()

    # Swagger UI may keep the backdrop briefly while
    # the authorization modal is closing.
    backdrop = page.locator(".backdrop-ux")
    expect(backdrop).to_be_hidden()

    # ---------------------------------------------------------
    # 5. Open POST /posts/
    # ---------------------------------------------------------
    endpoint = get_post_endpoint(
        page,
        "/posts/",
    )

    expect(endpoint).to_be_visible()
    endpoint.click()
    # ---------------------------------------------------------
    # 6. Fill request body
    # ---------------------------------------------------------
    fill_request_body(
        endpoint,
        """{
  "title": "Swagger E2E Post",
  "content": "Post created through Swagger UI E2E test"
}""",
    )

    # ---------------------------------------------------------
    # 7. Execute
    # ---------------------------------------------------------
    click_execute(endpoint)

    # ---------------------------------------------------------
    # 8. Verify response
    # ---------------------------------------------------------
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

    # ---------------------------------------------------------
    # 9. Capture evidence
    # ---------------------------------------------------------
    screenshot(
        page,
        "swagger/06_create_post_success.png",
    )