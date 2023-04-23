from datetime import datetime

import schemas.order as order_schema
from models.Order import orders_table, carts_table
from models.Item import items_table
from models.User import users_table
from models.database import database
from schemas import user
from sqlalchemy import select
import pandas as pd

async def create_order(order: order_schema.OrderCreate, user: user.User):
    query = (
        orders_table.insert().values(
            order_date=datetime.now()
        ).returning(
            orders_table.c.id
        )
    )
    order_id = await database.fetch_one(query)
    order_id = dict(zip(order_id, order_id.values()))
    order_id = order_id['id']
    cart = []
    for o in order.items:
        print(o)
        for i in range(0, o.count):
            cart.append((user.id, o.item_id, order_id))
    print(cart)
    query = (
        carts_table.insert().values(
            cart
        )
    )
    await database.execute(query)

    query = (
        select(
            items_table.c.id,
            items_table.c.item_name,
            items_table.c.price,
            items_table.c.mass,
            items_table.c.description,
            items_table.c.category,
            items_table.c.subcategory,
            items_table.c.harvest_date,
            items_table.c.compound,
            items_table.c.package,
            items_table.c.manufacturer
        ).select_from(orders_table.join(carts_table).join(items_table))
        .where(
            orders_table.c.id == order_id
        )
    )
    result = await database.fetch_all(query)
    items = []
    for rec in result:
        items.append(dict(zip(rec, rec.values())))
    print({'name': user.name, 'items': items})
    return {'name': user.name, 'items': items}

async def get_orders(page: int):
    max_per_page = 10
    offset1 = (page - 1) * max_per_page
    query = (
        select(
            [
                users_table.c.name,
                items_table.c.id,
                items_table.c.item_name,
                items_table.c.price,
                items_table.c.mass,
                items_table.c.description,
                items_table.c.category,
                items_table.c.subcategory,
                items_table.c.harvest_date,
                items_table.c.compound,
                items_table.c.package,
                items_table.c.manufacturer
            ]
        ).select_from(carts_table.join(items_table).join(users_table))
        .limit(max_per_page)
        .offset(offset1)
    )
    result = await database.fetch_all(query)
    orders_records_list = []
    for rec in result:
        orders_records_list.append(dict(zip(rec, rec.values())))
    print(orders_records_list)
    df = pd.DataFrame(orders_records_list)
    df = df.groupby('name').apply(lambda x: x[[
        'id',
        'item_name',
        'price',
        'mass',
        'description',
        'category',
        'subcategory',
        'category',
        'subcategory',
        'harvest_date',
        'compound',
        'package',
        'manufacturer'
    ]].to_dict('records')).reset_index()
    df = df.rename(columns={0: 'items'})
    orders = df.to_dict(orient='records')
    print(orders)
    orders = {'orders': orders}
    return orders



async def get_order(id: int):
    query = (
        select([
            users_table.c.name,
            items_table.c.id,
            items_table.c.item_name,
            items_table.c.price,
            items_table.c.mass,
            items_table.c.description,
            items_table.c.category,
            items_table.c.subcategory,
            items_table.c.harvest_date,
            items_table.c.compound,
            items_table.c.package,
            items_table.c.manufacturer
            ]
        ).select_from(carts_table.join(users_table).join(items_table).join(orders_table))
        .where(orders_table.c.id == id)
    )
    result = await database.fetch_all(query)
    items_records_list = []
    for rec in result:
        items_records_list.append(dict(zip(rec, rec.values())))
    df = pd.DataFrame(items_records_list)
    df = df.groupby('name').apply(lambda x: x[[
        'id',
        'item_name',
        'price',
        'mass',
        'description',
        'category',
        'subcategory',
        'harvest_date',
        'compound',
        'package',
        'manufacturer'
    ]].to_dict('records')).reset_index()
    df = df.rename(columns={0: 'items'})
    items = df.to_dict(orient='records')
    print(items)
    return items[0]
