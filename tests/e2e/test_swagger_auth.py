import uuid

from playwright.sync_api import expect

from tests.e2e.utils import (
    click_execute,
    click_try_it_out,
    fill_form_field,
    get_post_endpoint,
    open_swagger,
    screenshot,
)


def test_swagger_login(page):
    # ---------------------------------------------------------
    # 1. Create a test user through API
    # ---------------------------------------------------------
    email = f"swagger-login-{uuid.uuid4().hex[:8]}@example.com"
    password = "123456"

    create_response = page.request.post(
        "http://api:8000/users/",
        data={
            "name": "Swagger Login User",
            "email": email,
            "password": password,
            "full_name": "Swagger Login User",
        },
    )

    assert create_response.status == 201

    # ---------------------------------------------------------
    # 2. Open Swagger UI
    # ---------------------------------------------------------
    open_swagger(page)

    # ---------------------------------------------------------
    # 3. Open POST /auth/login
    # ---------------------------------------------------------
    endpoint = get_post_endpoint(
        page,
        "/auth/login",
    )

    endpoint.click()

    # ---------------------------------------------------------
    # 4. Enable Try it out
    # ---------------------------------------------------------
    click_try_it_out(endpoint)

    # ---------------------------------------------------------
    # 5. Fill OAuth2PasswordRequestForm
    # ---------------------------------------------------------
    fill_form_field(
        endpoint,
        "username",
        email,
    )

    fill_form_field(
        endpoint,
        "password",
        password,
    )

    # ---------------------------------------------------------
    # 6. Execute login
    # ---------------------------------------------------------
    click_execute(endpoint)

    # ---------------------------------------------------------
    # 7. Verify response
    # ---------------------------------------------------------
    response_section = endpoint.locator(
        ".responses-inner"
    )

    expect(response_section).to_contain_text("200")
    expect(response_section).to_contain_text(
        "access_token"
    )
    expect(response_section).to_contain_text(
        "bearer"
    )

    # ---------------------------------------------------------
    # 8. Capture evidence
    # ---------------------------------------------------------
    screenshot(
        page,
        "swagger/04_login_success.png",
    )