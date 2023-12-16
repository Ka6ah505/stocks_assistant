"""Create database

Revision ID: 3cb3a97e5520
Revises: 
Create Date: 2023-12-16 14:47:03.905421

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '3cb3a97e5520'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stock_prices',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('stock', sa.String(), nullable=False),
                    sa.Column('date_time', sa.DateTime(), nullable=False),
                    sa.Column('open', sa.Float(), nullable=False),
                    sa.Column('high', sa.Float(), nullable=False),
                    sa.Column('close', sa.Float(), nullable=False),
                    sa.Column('low', sa.Float(), nullable=False),
                    sa.Column('volume', sa.Integer(), nullable=False),
                    sa.Column('time_frame', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stock_prices')
    # ### end Alembic commands ###