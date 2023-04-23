from models.Item import items_table
from sqlalchemy import and_, select
from models.database import database
from schemas import item as item_schema
from typing import List

async def get_items_by_category(category: str, subcategory: str, page: int):
    max_per_page = 10
    offset1 = (page-1) * max_per_page
    query = (
        select(
            [
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
                items_table.c.manufacturer,
                items_table.c.img_url
            ]
        ).select_from(items_table).where(
            and_(
                items_table.c.category == category,
                items_table.c.subcategory == subcategory
            )
        ).limit(max_per_page)
        .offset(offset1)
    )
    result = await database.fetch_all(query)
    items_records_table = []
    for rec in result:
        items_records_table.append(dict(zip(rec, rec.values())))
    items = {'Items': items_records_table}
    print(items)
    return items

async def post_item(item: item_schema.PostItemModel):
    query = (
        items_table.insert().values(
            item_name=item.item_name,
            price=item.price,
            mass=item.mass,
            description=item.description,
            category=item.category,
            subcategory=item.subcategory,
            harvest_date=item.harvest_date,
            compound=item.compound,
            package=item.package,
            manufacturer=item.manufacturer,
            img_url=item.img_url
        ).returning(
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
        )
    )
    item = await database.fetch_one(query)

    item = dict(zip(item, item.values()))
    return item

async def post_items(items: List[item_schema.PostItemModel]):
    items_values_list = []
    for item in items:
        print(item)
        items_values_list.append(
                vars(item)
        )
    print(items_values_list)
    query = items_table.insert().values(
        items_values_list
    ).returning(
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
        items_table.c.manufacturer,
        items_table.c.img_url
    )
    items = await database.fetch_all(query)
    items_list = []
    for item in items:
        items_list.append(dict(zip(item, item.values())))
    return {'Items': items_list}

async def get_item_by_id(id: int):
    query = select(
        [
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
            items_table.c.manufacturer,
            items_table.c.img_url
        ]
    ).select_from(items_table).where(items_table.c.id==id)
    item = await database.fetch_one(query)
    item = dict(zip(item, item.values()))
    return item