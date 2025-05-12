"""create users table

Revision ID: 2df02cad03d8
Revises: 223951c92291
Create Date: 2025-04-27 12:10:26.750258

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2df02cad03d8'
down_revision: Union[str, None] = '223951c92291'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
