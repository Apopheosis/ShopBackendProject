from typing import List, Optional

from pydantic import BaseModel
from schemas.item import ItemDetailsModel

class OrderItem(BaseModel):
    item_id: int
    count: int

class OrderCreate(BaseModel):
    items: List[OrderItem]

class Order(BaseModel):
    name: str
    items: Optional[List[ItemDetailsModel]]

class OrderList(BaseModel):
    orders: List[Order]