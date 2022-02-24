"""added column [close] to table stock

Revision ID: 9fac61820772
Revises: a281c68b4ba3
Create Date: 2022-02-24 17:32:17.120883

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9fac61820772'
down_revision = 'a281c68b4ba3'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('stock', sa.Column('close', sa.Float))


def downgrade():
    op.drop_column('stock', 'close')
