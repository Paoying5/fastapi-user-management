import re
import uuid

from playwright.sync_api import expect

from tests.e2e.utils import (
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

    assert create_response.status == 201, (
        f"Failed to create test user: "
        f"{create_response.status} "
        f"{create_response.text()}"
    )

    # ---------------------------------------------------------
    # 2. Open Swagger UI
    # ---------------------------------------------------------
    open_swagger(page)

    # ---------------------------------------------------------
    # 3. Open Authorize dialog
    # ---------------------------------------------------------
    authorize_button = page.get_by_role(
        "button",
        name="Authorize",
    )

    expect(authorize_button).to_be_visible()
    authorize_button.click()

    dialog = page.locator(".modal-ux")

    expect(dialog).to_be_visible()

    # ---------------------------------------------------------
    # 4. Fill OAuth2 credentials
    # ---------------------------------------------------------
    username_input = dialog.get_by_role(
        "textbox",
        name="username:",
    )

    password_input = dialog.get_by_role(
        "textbox",
        name="password:",
    )

    expect(username_input).to_be_visible()
    expect(password_input).to_be_visible()

    username_input.fill(email)
    password_input.fill(password)

    # ---------------------------------------------------------
    # 5. Authorize
    # ---------------------------------------------------------
    #
    # Swagger UI uses:
    # aria-label="Apply given OAuth2 credentials"
    #
    # The visible text is "Authorize", but the accessible
    # role/name used by Playwright is "Apply given OAuth2 credentials".
    #
    authorize_dialog_button = dialog.get_by_role(
        "button",
        name="Apply given OAuth2 credentials",
    )

    expect(authorize_dialog_button).to_be_visible()
    expect(authorize_dialog_button).to_be_enabled()

    authorize_dialog_button.click()

    # ---------------------------------------------------------
    # 6. Verify authorization
    # ---------------------------------------------------------
    authorization_button = page.get_by_role(
        "button",
        name="authorization button unlocked",
    ).first

    expect(authorization_button).to_be_visible()

    # ---------------------------------------------------------
    # 7. Capture evidence
    # ---------------------------------------------------------
    screenshot(
        page,
        "swagger/05_authorize_success.png",
    )
