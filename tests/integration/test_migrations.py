from pathlib import Path

import pytest
from alembic.config import Config
from alembic.script import ScriptDirectory
from sqlalchemy import Engine, inspect, text


pytestmark = pytest.mark.integration


PROJECT_ROOT = Path(
    __file__
).resolve().parents[2]


def get_script_heads() -> set[str]:
    config = Config(
        str(
            PROJECT_ROOT
            / "alembic.ini"
        )
    )

    config.set_main_option(
        "script_location",
        str(
            PROJECT_ROOT
            / "alembic"
        ),
    )

    script = ScriptDirectory.from_config(
        config
    )

    return set(
        script.get_heads()
    )


def test_alembic_database_is_at_head(
    pg_engine: Engine,
):
    with pg_engine.connect() as connection:
        rows = connection.execute(
            text(
                """
                SELECT version_num
                FROM alembic_version
                """
            )
        )

        database_heads = {
            row[0]
            for row in rows
        }

    assert (
        database_heads
        == get_script_heads()
    )


def test_expected_tables_exist(
    pg_engine: Engine,
):
    inspector = inspect(
        pg_engine
    )

    tables = set(
        inspector.get_table_names()
    )

    assert "users" in tables
    assert "posts" in tables
    assert "alembic_version" in tables


def test_user_role_schema_constraints(
    pg_engine: Engine,
):
    inspector = inspect(
        pg_engine
    )

    columns = {
        column["name"]: column
        for column
        in inspector.get_columns(
            "users"
        )
    }

    role_column = columns[
        "role"
    ]

    assert (
        role_column["nullable"]
        is False
    )

    assert "user" in str(
        role_column["default"]
    ).lower()

    constraints = (
        inspector
        .get_check_constraints(
            "users"
        )
    )

    role_constraint = next(
        (
            constraint
            for constraint
            in constraints
            if (
                constraint["name"]
                == "ck_users_role_allowed"
            )
        ),
        None,
    )

    assert role_constraint is not None

    sql_text = str(
        role_constraint["sqltext"]
    ).lower()

    assert "user" in sql_text
    assert "admin" in sql_text

def test_user_lifecycle_columns_exist(
    pg_engine,
):
    inspector = inspect(
        pg_engine
    )

    columns = {
        column["name"]: column
        for column
        in inspector.get_columns(
            "users"
        )
    }

    assert "is_active" in columns
    assert "created_at" in columns
    assert "updated_at" in columns
    assert "last_login_at" in columns

    assert (
        columns["is_active"]["nullable"]
        is False
    )

    assert (
        columns["created_at"]["nullable"]
        is False
    )

    assert (
        columns["updated_at"]["nullable"]
        is False
    )


def test_post_lifecycle_schema_exists(
    pg_engine,
):
    inspector = inspect(
        pg_engine
    )

    columns = {
        column["name"]: column
        for column
        in inspector.get_columns(
            "posts"
        )
    }

    assert "status" in columns
    assert "created_at" in columns
    assert "updated_at" in columns

    assert (
        columns["status"]["nullable"]
        is False
    )

    assert (
        columns["created_at"]["nullable"]
        is False
    )

    assert (
        columns["updated_at"]["nullable"]
        is False
    )

    constraints = (
        inspector.get_check_constraints(
            "posts"
        )
    )

    status_constraint = next(
        (
            constraint
            for constraint
            in constraints
            if (
                constraint["name"]
                == "ck_posts_status_allowed"
            )
        ),
        None,
    )

    assert status_constraint is not None

    sql_text = str(
        status_constraint["sqltext"]
    ).lower()

    assert "draft" in sql_text
    assert "published" in sql_text
    assert "archived" in sql_text