"""empty message

Revision ID: da381a1eb77b
Revises: 079327268744
Create Date: 2023-04-22 22:29:20.183450

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da381a1eb77b'
down_revision = '079327268744'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('items', sa.Column('item_name', sa.String(), nullable=True))
    op.drop_column('items', 'name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('items', sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('items', 'item_name')
    # ### end Alembic commands ###
