"""add table operations

Revision ID: 94410b910503
Revises: f00b40915658
Create Date: 2022-04-13 21:18:15.658647

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94410b910503'
down_revision = 'f00b40915658'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'operation',
        sa.Column('uuid', sa.String, nullable=False, primary_key=True),
        sa.Column('user_id', sa.String, nullable=False),
        sa.Column('ticket', sa.String, nullable=False),
        sa.Column('type', sa.String, nullable=False),
        sa.Column('timestamp', sa.Integer, nullable=False)
    )


def downgrade():
    op.drop_table('operation')
