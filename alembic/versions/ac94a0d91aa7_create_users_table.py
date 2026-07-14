"""create users table

Revision ID: ac94a0d91aa7
Revises: 6e23794ea3a5
Create Date: 2026-07-10 20:02:58.717315

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ac94a0d91aa7'
down_revision: Union[str, Sequence[str], None] = '6e23794ea3a5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, nullable=False),
        sa.Column('email', sa.String, nullable=False, unique=True),
        sa.Column('password', sa.String, nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    )
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
