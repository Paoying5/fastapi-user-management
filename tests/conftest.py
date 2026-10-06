from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import StaticPool

from app.core.security import hash_password
from app.database import Base
from app.dependencies import get_db
from app.main import app
from app.models import User


SQLALCHEMY_DATABASE_URL = "sqlite://"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={
        "check_same_thread": False,
    },
    poolclass=StaticPool,
)


TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


@pytest.fixture(scope="function")
def db_session() -> Generator[
    Session,
    None,
    None,
]:
    Base.metadata.create_all(
        bind=engine
    )

    db = TestingSessionLocal()

    try:
        yield db
    finally:
        db.close()

        Base.metadata.drop_all(
            bind=engine
        )


@pytest.fixture(scope="function")
def client(
    db_session: Session,
) -> Generator[
    TestClient,
    None,
    None,
]:
    def override_get_db():
        yield db_session

    app.dependency_overrides[
        get_db
    ] = override_get_db

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()


def login_client(
    client: TestClient,
    email: str,
    password: str,
) -> None:
    response = client.post(
        "/auth/login",
        data={
            "username": email,
            "password": password,
        },
    )

    assert response.status_code == 200

    token = response.json()[
        "access_token"
    ]

    client.headers.update(
        {
            "Authorization": (
                f"Bearer {token}"
            ),
        }
    )


@pytest.fixture(scope="function")
def user_client(
    client: TestClient,
) -> Generator[
    TestClient,
    None,
    None,
]:
    response = client.post(
        "/users/",
        json={
            "name": "testuser",
            "email": "testuser@example.com",
            "password": "123456",
            "full_name": "Test User",
        },
    )

    assert response.status_code == 201

    login_client(
        client,
        email="testuser@example.com",
        password="123456",
    )

    yield client

    client.headers.pop(
        "Authorization",
        None,
    )


@pytest.fixture(scope="function")
def admin_client(
    client: TestClient,
    db_session: Session,
) -> Generator[
    TestClient,
    None,
    None,
]:
    admin = User(
        name="testadmin",
        email="testadmin@example.com",
        role="admin",
        password=hash_password(
            "123456"
        ),
        full_name="Test Admin",
    )

    db_session.add(admin)
    db_session.commit()

    login_client(
        client,
        email="testadmin@example.com",
        password="123456",
    )

    yield client

    client.headers.pop(
        "Authorization",
        None,
    )


@pytest.fixture(scope="function")
def auth_client(
    admin_client: TestClient,
) -> TestClient:
    """
    Backward-compatible alias.

    Existing tests currently expect auth_client
    to be an authenticated admin client.

    New tests should prefer the explicit fixtures:
    - user_client
    - admin_client
    """
    return admin_client