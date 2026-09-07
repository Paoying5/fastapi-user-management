from pathlib import Path

from playwright.sync_api import Locator, Page, expect


SCREENSHOT_DIR = Path("tests/screenshots/automation")


def open_swagger(page: Page) -> None:
    page.goto("http://api:8000/docs")

    expect(page).to_have_title(
        "FastAPI User Management - Swagger UI"
    )


def get_post_endpoint(
    page: Page,
    path: str,
) -> Locator:
    endpoint = (
        page.locator(".opblock-post")
        .filter(has_text=path)
        .first
    )

    expect(endpoint).to_be_visible()

    return endpoint


def click_try_it_out(endpoint: Locator) -> None:
    endpoint.get_by_role(
        "button",
        name="Try it out",
    ).click()


def click_execute(endpoint: Locator) -> None:
    endpoint.get_by_role(
        "button",
        name="Execute",
    ).click()


def fill_request_body(
    endpoint: Locator,
    body: str,
) -> None:
    request_body = endpoint.locator("textarea")

    expect(request_body).to_be_visible()

    request_body.fill(body)


def fill_form_field(
    endpoint: Locator,
    field_name: str,
    value: str,
) -> None:
    field = endpoint.locator(
        f'input[name="{field_name}"]'
    )

    expect(field).to_be_visible()

    field.fill(value)


def screenshot(
    page: Page,
    filename: str,
) -> None:
    path = SCREENSHOT_DIR / filename

    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    page.screenshot(
        path=path,
        full_page=True,
    )