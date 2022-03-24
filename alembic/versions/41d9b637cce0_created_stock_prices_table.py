"""created stock_prices table

Revision ID: 41d9b637cce0
Revises: 9fac61820772
Create Date: 2022-03-24 20:08:26.110784

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41d9b637cce0'
down_revision = '9fac61820772'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'stock_prices',
        sa.Column('ticket', sa.String, nullable=False),
        sa.Column('dateCandle', sa.Integer, nullable=False),
        sa.Column('open', sa.Float, nullable=False),
        sa.Column('high', sa.Float, nullable=False),
        sa.Column('low', sa.Float, nullable=False),
        sa.Column('close', sa.Float, nullable=False),
        sa.Column('volume', sa.Integer, nullable=False),
        sa.Column('timeFrame', sa.String, nullable=False),
        sa.Column('id', sa.Integer, primary_key=True)
    )


def downgrade():
    op.drop_table('stock_prices')
