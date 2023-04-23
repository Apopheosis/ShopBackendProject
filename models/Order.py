import sqlalchemy

from .User import users_table
from .Item import items_table
metadata = sqlalchemy.MetaData()

orders_table = sqlalchemy.Table(
    'orders',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('order_date', sqlalchemy.DateTime)
)

carts_table = sqlalchemy.Table(
    'carts',
    metadata,
    sqlalchemy.Column('user_id', sqlalchemy.ForeignKey(users_table.c.id)),
    sqlalchemy.Column('item_id', sqlalchemy.ForeignKey(items_table.c.id)),
    sqlalchemy.Column('order_id', sqlalchemy.ForeignKey('orders.id')),
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
)