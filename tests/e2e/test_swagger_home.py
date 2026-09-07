from tests.e2e.utils import open_swagger, screenshot


def test_swagger_home(page):
    open_swagger(page)

    screenshot(
        page,
        "swagger/01_home.png",
    )


def test_swagger_openapi(page):
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
        "swagger/02_endpoints.png",
    )