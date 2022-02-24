"""init

Revision ID: a281c68b4ba3
Revises: 
Create Date: 2022-02-24 17:12:16.964778

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a281c68b4ba3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'stock',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('ticket', sa.String, nullable=False)
    )


def downgrade():
    op.drop_table('stock')
