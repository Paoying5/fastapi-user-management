"""enforce user role constraints

Revision ID: b31f9c2a6d10
Revises: e7d9b8aad922
Create Date: 2026-10-07
"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op


revision: str = "b31f9c2a6d10"
down_revision: Union[str, Sequence[str], None] = "e7d9b8aad922"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    connection = op.get_bind()

    invalid_role_count = connection.execute(
        sa.text(
            """
            SELECT COUNT(*)
            FROM users
            WHERE role IS NOT NULL
              AND role NOT IN ('user', 'admin')
            """
        )
    ).scalar_one()

    if invalid_role_count > 0:
        raise RuntimeError(
            "Migration stopped because users table contains "
            "roles other than 'user' or 'admin'. "
            "Fix invalid role data before running this migration."
        )

    connection.execute(
        sa.text(
            """
            UPDATE users
            SET role = 'user'
            WHERE role IS NULL
            """
        )
    )

    op.alter_column(
        "users",
        "role",
        existing_type=sa.String(length=50),
        nullable=False,
        server_default="user",
    )

    op.create_check_constraint(
        "ck_users_role_allowed",
        "users",
        "role IN ('user', 'admin')",
    )


def downgrade() -> None:
    op.drop_constraint(
        "ck_users_role_allowed",
        "users",
        type_="check",
    )

    op.alter_column(
        "users",
        "role",
        existing_type=sa.String(length=50),
        nullable=True,
        server_default=None,
    )