"""init auth tables

Revision ID: bdc16d8cbc2d
Revises: 
Create Date: 2026-06-29 00:45:20.715888
"""

from collections.abc import Sequence

from alembic import op
import sqlalchemy as sa

revision: str = 'bdc16d8cbc2d'
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
