from playwright.sync_api import Page, expect

from tests.e2e.utils import (
    click_execute,
    click_try_it_out,
    fill_request_body,
    get_post_endpoint,
    open_swagger,
    screenshot,
)


def test_swagger_health(page: Page):
    open_swagger(page)

    screenshot(
        page,
        "01_swagger_home.png",
    )


def test_swagger_openapi(page: Page):
    response = page.request.get(
        "http://api:8000/openapi.json"
    )

    assert response.status == 200

    data = response.json()

    assert data["info"]["title"] == (
        "FastAPI User Management"
    )

    assert "/health" in data["paths"]
    assert "/auth/login" in data["paths"]
    assert "/users/" in data["paths"]
    assert "/posts/" in data["paths"]

    open_swagger(page)

    screenshot(
        page,
        "02_swagger_endpoints.png",
    )


def test_swagger_create_user(page: Page):
    open_swagger(page)

    endpoint = get_post_endpoint(
        page,
        "/users/",
    )

    endpoint.click()

    click_try_it_out(endpoint)

    fill_request_body(
        endpoint,
        """{
  "name": "Swagger E2E User",
  "email": "swagger-e2e@example.com",
  "password": "123456",
  "full_name": "Swagger E2E User"
}""",
    )

    click_execute(endpoint)

    response_section = endpoint.locator(
        ".responses-inner"
    )

    expect(response_section).to_contain_text("201")
    expect(response_section).to_contain_text(
        "swagger-e2e@example.com"
    )
    expect(response_section).to_contain_text(
        "Swagger E2E User"
    )

    screenshot(
        page,
        "03_swagger_create_user_success.png",
    )

