"""updating table users

Revision ID: 065519ffc0b6
Revises: d104cec1a8a5
Create Date: 2022-09-18 09:51:59.559665

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '065519ffc0b6'
down_revision = 'd104cec1a8a5'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('token', sa.String, nullable=False))
    op.add_column('users', sa.Column('last_updated', sa.Integer, nullable=False))


def downgrade():
    op.drop_column('users', 'token')
    op.drop_column(('users', 'last_updated'))
