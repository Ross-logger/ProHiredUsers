"""Database creation

Revision ID: 5cc15e479bcc
Revises: 
Create Date: 2024-08-24 10:45:39.927492

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5cc15e479bcc'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create the user table
    op.create_table(
        'user',
        sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column('email', sa.VARCHAR(), nullable=False),
        sa.Column('username', sa.VARCHAR(), nullable=False),
        sa.Column('hashed_password', sa.VARCHAR(length=1024), nullable=False),
        sa.Column('phone_number', sa.VARCHAR(), nullable=True),
        sa.Column('is_active', sa.BOOLEAN(), nullable=False),
        sa.Column('is_superuser', sa.BOOLEAN(), nullable=False),
        sa.Column('is_verified', sa.BOOLEAN(), nullable=False),
        sa.PrimaryKeyConstraint('id', name='user_pkey'),
        sa.UniqueConstraint('email', name='user_email_key')
    )


def downgrade() -> None:
    # Drop the user table
    op.drop_table('user')