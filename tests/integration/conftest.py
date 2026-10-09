import os
from collections.abc import Generator
from pathlib import Path

import pytest
from alembic import command
from alembic.config import Config
from sqlalchemy import Engine, create_engine, text
from sqlalchemy.engine import make_url
from sqlalchemy.orm import Session

from app.core.config import settings


PROJECT_ROOT = Path(__file__).resolve().parents[2]

ALEMBIC_INI = PROJECT_ROOT / "alembic.ini"

TEST_DATABASE_NAME = "fastapi_test_db"


def build_alembic_config() -> Config:
    config = Config(
        str(ALEMBIC_INI)
    )

    config.set_main_option(
        "script_location",
        str(PROJECT_ROOT / "alembic"),
    )

    return config


@pytest.fixture(scope="session")
def postgres_test_database() -> Generator[
    str,
    None,
    None,
]:
    base_url = make_url(
        settings.DATABASE_URL
    )

    if (
        base_url.get_backend_name()
        != "postgresql"
    ):
        raise RuntimeError(
            "Integration tests require PostgreSQL."
        )

    admin_url = base_url.set(
        database="postgres"
    )

    test_url = base_url.set(
        database=TEST_DATABASE_NAME
    )

    test_database_url = (
        test_url.render_as_string(
            hide_password=False
        )
    )

    admin_engine = create_engine(
        admin_url,
        isolation_level="AUTOCOMMIT",
        pool_pre_ping=True,
    )

    with admin_engine.connect() as connection:
        connection.execute(
            text(
                """
                SELECT pg_terminate_backend(pid)
                FROM pg_stat_activity
                WHERE datname = :database_name
                  AND pid <> pg_backend_pid()
                """
            ),
            {
                "database_name":
                    TEST_DATABASE_NAME
            },
        )

        connection.exec_driver_sql(
            f'DROP DATABASE IF EXISTS '
            f'"{TEST_DATABASE_NAME}"'
        )

        connection.exec_driver_sql(
            f'CREATE DATABASE '
            f'"{TEST_DATABASE_NAME}"'
        )

    previous_database_url = os.environ.get(
        "DATABASE_URL"
    )

    os.environ[
        "DATABASE_URL"
    ] = test_database_url

    try:
        alembic_config = (
            build_alembic_config()
        )

        command.upgrade(
            alembic_config,
            "head",
        )

        yield test_database_url

    finally:
        if previous_database_url is None:
            os.environ.pop(
                "DATABASE_URL",
                None,
            )
        else:
            os.environ[
                "DATABASE_URL"
            ] = previous_database_url

        with admin_engine.connect() as connection:
            connection.execute(
                text(
                    """
                    SELECT pg_terminate_backend(pid)
                    FROM pg_stat_activity
                    WHERE datname = :database_name
                      AND pid <> pg_backend_pid()
                    """
                ),
                {
                    "database_name":
                        TEST_DATABASE_NAME
                },
            )

            connection.exec_driver_sql(
                f'DROP DATABASE IF EXISTS '
                f'"{TEST_DATABASE_NAME}"'
            )

        admin_engine.dispose()


@pytest.fixture(scope="session")
def pg_engine(
    postgres_test_database: str,
) -> Generator[
    Engine,
    None,
    None,
]:
    engine = create_engine(
        postgres_test_database,
        pool_pre_ping=True,
    )

    try:
        yield engine
    finally:
        engine.dispose()


@pytest.fixture(scope="function")
def pg_session(
    pg_engine: Engine,
) -> Generator[
    Session,
    None,
    None,
]:
    session = Session(
        bind=pg_engine
    )

    try:
        yield session

    finally:
        session.rollback()
        session.close()