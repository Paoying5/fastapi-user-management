import pytest

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from app.core.security import hash_password
from app.models import User
from app.database import Base
from app.dependencies import get_db
from app.main import app


SQLALCHEMY_DATABASE_URL = "sqlite://"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


@pytest.fixture(scope="function")
def db_session():
    Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()

    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def client(db_session):
    def override_get_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()


@pytest.fixture
def auth_client(client):
    response = client.post(
        "/users/",
        json={
            "name": "pytestuser",
            "email": "pytest-auth@example.com",
            "password": "123456",
            "full_name": "Pytest Auth User",
        },
    )

    assert response.status_code == 201

    login_response = client.post(
        "/auth/login",
        data={
            "username": "pytest-auth@example.com",
            "password": "123456",
        },
    )

    assert login_response.status_code == 200

    token = login_response.json()["access_token"]

    client.headers.update(
        {
            "Authorization": f"Bearer {token}",
        }
    )

    return client

@pytest.fixture(scope="function")
def auth_client(client, db_session):
    admin = User(
        name="testadmin",
        email="testadmin@example.com",
        role="admin",
        password=hash_password("123456"),
        full_name="Test Admin",
    )

    db_session.add(admin)
    db_session.commit()

    response = client.post(
        "/auth/login",
        data={
            "username": "testadmin@example.com",
            "password": "123456",
        },
    )

    assert response.status_code == 200

    token = response.json()["access_token"]

    client.headers.update({
        "Authorization": f"Bearer {token}"
    })

    yield client

    client.headers.pop("Authorization", None)