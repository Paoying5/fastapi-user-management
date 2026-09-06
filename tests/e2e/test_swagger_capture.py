from pathlib import Path

from playwright.sync_api import Page, expect


SCREENSHOT_DIR = Path("tests/screenshots")


def test_swagger_health(page: Page):
    SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)

    page.goto("http://api:8000/docs")

    expect(page).to_have_title("FastAPI User Management - Swagger UI")

    page.screenshot(
        path=SCREENSHOT_DIR / "01_swagger_home.png",
        full_page=True,
    )


def test_swagger_openapi(page: Page):
    SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)

    response = page.request.get("http://api:8000/openapi.json")

    assert response.status == 200

    data = response.json()

    assert data["info"]["title"] == "FastAPI User Management"
    assert "/health" in data["paths"]
    assert "/auth/login" in data["paths"]
    assert "/users/" in data["paths"]
    assert "/posts/" in data["paths"]

    page.goto("http://api:8000/docs")

    page.screenshot(
        path=SCREENSHOT_DIR / "02_swagger_endpoints.png",
        full_page=True,
    )

