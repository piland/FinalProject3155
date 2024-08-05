from typing import Optional

import datetime
from pydantic import BaseModel


class PromoCodeBase(BaseModel):
    pass


class PromoCodeCreate(PromoCodeBase):
    discount: float
    name: str
    order_date: datetime.date


class PromoCodeUpdate(BaseModel):
    discount: Optional[float] = None
    name: Optional[str] = None
    expiration_date: Optional[datetime.date] = None



class PromoCode(PromoCodeBase):
    discount: float
    name: str
    expiration_date: Optional[datetime.date] = None

    class Config:
        from_attributes = True
