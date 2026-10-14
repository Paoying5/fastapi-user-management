"""add lifecycle fields

Revision ID: c42a7f91d8e3
Revises: b31f9c2a6d10
Create Date: 2026-10-14
"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op


revision: str = "c42a7f91d8e3"

down_revision: Union[
    str,
    Sequence[str],
    None,
] = "b31f9c2a6d10"

branch_labels: Union[
    str,
    Sequence[str],
    None,
] = None

depends_on: Union[
    str,
    Sequence[str],
    None,
] = None


def upgrade() -> None:
    op.add_column(
        "users",
        sa.Column(
            "is_active",
            sa.Boolean(),
            nullable=False,
            server_default=sa.true(),
        ),
    )

    op.add_column(
        "users",
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text(
                "CURRENT_TIMESTAMP"
            ),
        ),
    )

    op.add_column(
        "users",
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text(
                "CURRENT_TIMESTAMP"
            ),
        ),
    )

    op.add_column(
        "users",
        sa.Column(
            "last_login_at",
            sa.DateTime(timezone=True),
            nullable=True,
        ),
    )

    op.add_column(
        "posts",
        sa.Column(
            "status",
            sa.String(length=20),
            nullable=False,
            server_default=sa.text(
                "'published'"
            ),
        ),
    )

    op.add_column(
        "posts",
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text(
                "CURRENT_TIMESTAMP"
            ),
        ),
    )

    op.add_column(
        "posts",
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text(
                "CURRENT_TIMESTAMP"
            ),
        ),
    )

    op.create_check_constraint(
        "ck_posts_status_allowed",
        "posts",
        (
            "status IN "
            "('draft', 'published', 'archived')"
        ),
    )


def downgrade() -> None:
    op.drop_constraint(
        "ck_posts_status_allowed",
        "posts",
        type_="check",
    )

    op.drop_column(
        "posts",
        "updated_at",
    )

    op.drop_column(
        "posts",
        "created_at",
    )

    op.drop_column(
        "posts",
        "status",
    )

    op.drop_column(
        "users",
        "last_login_at",
    )

    op.drop_column(
        "users",
        "updated_at",
    )

    op.drop_column(
        "users",
        "created_at",
    )

    op.drop_column(
        "users",
        "is_active",
    )