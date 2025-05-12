"""initial_migration

Revision ID: 87762dfaf637
Revises: 006d07ff2d4c
Create Date: 2025-04-25 23:05:34.435683

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '87762dfaf637'
down_revision: Union[str, None] = '006d07ff2d4c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
