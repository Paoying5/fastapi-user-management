from playwright.sync_api import expect

from tests.e2e.utils import (
    click_execute,
    click_try_it_out,
    fill_request_body,
    get_post_endpoint,
    open_swagger,
    screenshot,
)


def test_swagger_create_user(page):
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
        "swagger/03_create_user_success.png",
    )