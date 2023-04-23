"""empty message

Revision ID: 02d0ca29b375
Revises: da381a1eb77b
Create Date: 2023-04-22 23:48:23.460950

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '02d0ca29b375'
down_revision = 'da381a1eb77b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('carts',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('item_id', sa.Integer(), nullable=True),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['item_id'], ['items.id'], ),
    sa.ForeignKeyConstraint(['order_id'], ['orders.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('orders', sa.Column('order_date', sa.DateTime(), nullable=True))
    op.drop_constraint('orders_user_id_fkey', 'orders', type_='foreignkey')
    op.drop_constraint('orders_item_id_fkey', 'orders', type_='foreignkey')
    op.drop_column('orders', 'user_id')
    op.drop_column('orders', 'item_id')
    op.drop_column('tokens', 'tg_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tokens', sa.Column('tg_id', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('orders', sa.Column('item_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('orders', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('orders_item_id_fkey', 'orders', 'items', ['item_id'], ['id'])
    op.create_foreign_key('orders_user_id_fkey', 'orders', 'users', ['user_id'], ['id'])
    op.drop_column('orders', 'order_date')
    op.drop_table('carts')
    # ### end Alembic commands ###
