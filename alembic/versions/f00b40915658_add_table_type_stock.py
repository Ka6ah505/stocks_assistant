"""add table type_stock

Revision ID: f00b40915658
Revises: 41d9b637cce0
Create Date: 2022-04-13 21:13:21.588902

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f00b40915658'
down_revision = '41d9b637cce0'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'type_stock',
        sa.Column('ticket', sa.String, nullable=False, primary_key=True),
        sa.Column('initial_margin', sa.Float, nullable=False),
        sa.Column('exchange', sa.String, nullable=False)
    )


def downgrade():
    op.drop_table('type_stock')
