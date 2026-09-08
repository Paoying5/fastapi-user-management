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


def test_swagger_authorize(page):
    # ---------------------------------------------------------
    # 1. Create a test user through API
    # ---------------------------------------------------------
    email = (
        f"swagger-authorize-{uuid.uuid4().hex[:8]}"
        "@example.com"
    )
    password = "123456"

    create_response = page.request.post(
        "http://api:8000/users/",
        data={
            "name": "Swagger Authorize User",
            "email": email,
            "password": password,
            "full_name": "Swagger Authorize User",
        },
    )

    assert create_response.status == 201

    # ---------------------------------------------------------
    # 2. Open Swagger UI
    # ---------------------------------------------------------
    open_swagger(page)

    # ---------------------------------------------------------
    # 3. Login through Swagger
    # ---------------------------------------------------------
    endpoint = get_post_endpoint(
        page,
        "/auth/login",
    )

    endpoint.click()

    click_try_it_out(endpoint)

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

    click_execute(endpoint)

    # ---------------------------------------------------------
    # 4. Get access token from login response
    # ---------------------------------------------------------
    response_section = endpoint.locator(
        ".responses-inner"
    )

    expect(response_section).to_contain_text("200")
    expect(response_section).to_contain_text(
        "access_token"
    )

    response_text = response_section.inner_text()

    # ---------------------------------------------------------
    # 5. Extract access token
    # ---------------------------------------------------------
    import re

    match = re.search(
        r'"access_token"\s*:\s*"([^"]+)"',
        response_text,
    )

    assert match is not None

    access_token = match.group(1)

    assert access_token

    # ---------------------------------------------------------
    # 6. Open Authorize dialog
    # ---------------------------------------------------------
    page.get_by_role(
        "button",
        name="Authorize",
    ).click()

    page.screenshot(
        path="tests/screenshots/automation/swagger/debug_authorize_dialog.png",
        full_page=True,
    )

    page.pause()

    dialog = page.locator(
        ".modal-ux",
    )

    expect(dialog).to_be_visible()

    # ---------------------------------------------------------
    # 7. Fill bearer token
    # ---------------------------------------------------------
    token_input = dialog.locator(
        'input[type="text"]',
    ).first

    expect(token_input).to_be_visible()

    token_input.fill(
        f"Bearer {access_token}"
    )

    # ---------------------------------------------------------
    # 8. Authorize
    # ---------------------------------------------------------
    dialog.get_by_role(
        "button",
        name="Authorize",
    ).click()

    # ---------------------------------------------------------
    # 9. Close dialog
    # ---------------------------------------------------------
    dialog.get_by_role(
        "button",
        name="Close",
    ).click()

    # ---------------------------------------------------------
    # 10. Verify Swagger is authorized
    # ---------------------------------------------------------
    expect(
        page.get_by_role(
            "button",
            name="Authorize",
        )
    ).to_be_visible()

    expect(
        page.locator(".authorization__btn")
    ).to_have_class(
        re.compile(r"unlocked")
    )

    # ---------------------------------------------------------
    # 11. Capture evidence
    # ---------------------------------------------------------
    screenshot(
        page,
        "swagger/05_authorize_success.png",
    )