"""add table users

Revision ID: d104cec1a8a5
Revises: 94410b910503
Create Date: 2022-04-13 21:43:12.337404

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd104cec1a8a5'
down_revision = '94410b910503'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('uuid', sa.String, primary_key=True),
        sa.Column('nickname', sa.String, nullable=True),
        sa.Column('created_ts', sa.Integer, nullable=True),
        sa.Column('mail', sa.String, nullable=False)
    )


def downgrade():
    op.drop_table('users')
