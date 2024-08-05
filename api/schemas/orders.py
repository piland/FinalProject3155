from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .order_details import OrderDetail


class OrderBase(BaseModel):
    customer_name: str
    description: Optional[str] = None
    account_id: Optional[int] = None
    promo_code_id: Optional[int] = None
    order_type: Optional[str] = None
    order_status: Optional[bool] = None


class OrderCreate(OrderBase):
    order_date: Optional[datetime] = None


class OrderUpdate(BaseModel):
    customer_name: Optional[str] = None
    description: Optional[str] = None
    account_id: Optional[int] = None
    promo_code_id: Optional[int] = None
    order_type: Optional[str] = None
    order_status: Optional[bool] = None


class Order(OrderBase):
    id: int
    order_date: Optional[datetime] = None
    order_details: Optional[list[OrderDetail]] = None

    class Config:
        from_attributes = True
