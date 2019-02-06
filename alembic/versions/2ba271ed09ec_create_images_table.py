"""create images table

Revision ID: 2ba271ed09ec
Revises: 
Create Date: 2019-02-05 17:06:15.730956

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ba271ed09ec'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'objects',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('alias', sa.String(100), nullable=False),
        sa.Column('object_name', sa.String(100), nullable=False),
        sa.Column('type', sa.String(50), nullable=False),
        sa.Column('status', sa.String(50), nullable=False),
        sa.Column('updated_at', sa.DateTime, nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False)
    )


def downgrade():
    op.drop_table('images')

