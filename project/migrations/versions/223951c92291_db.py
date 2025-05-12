"""db

Revision ID: 223951c92291
Revises: 87762dfaf637
Create Date: 2025-04-27 11:46:59.996781

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '223951c92291'
down_revision: Union[str, None] = '87762dfaf637'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
