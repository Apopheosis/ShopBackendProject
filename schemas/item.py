from datetime import date
from typing import List, Optional

from pydantic import BaseModel

class ItemDetailsModel(BaseModel):
    id: Optional[int]
    item_name: str
    price: int
    mass: int
    description: str
    category: str
    subcategory: str
    harvest_date: Optional[date]
    compound: Optional[str]
    package: Optional[str]
    manufacturer: Optional[str]
    img_url: Optional[str]

class PostItemModel(BaseModel):
    item_name: str
    price: int
    mass: int
    description: str
    category: str
    subcategory: str
    harvest_date: Optional[date]
    compound: Optional[str]
    package: Optional[str]
    manufacturer: Optional[str]
    img_url: Optional[str]

class Items(BaseModel):
    Items: List[ItemDetailsModel]

