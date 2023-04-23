from fastapi import APIRouter, Depends
from utils.dependencies import get_current_user
from schemas import order
import utils.orders_utils as orders_utils
from schemas import user

router = APIRouter()

@router.post('/orders', response_model=order.Order)
async def create_order(order: order.OrderCreate, user: user.User = Depends(get_current_user)):
    order = await orders_utils.create_order(order, user)
    return order

@router.get('/orders', response_model=order.OrderList)
async def get_orders(page: int = 1):
    orders = await orders_utils.get_orders(page)
    return orders

@router.get('/orders/{id}', response_model=order.Order)
async def get_order(id: int):
    order = await orders_utils.get_order(id)
    return order