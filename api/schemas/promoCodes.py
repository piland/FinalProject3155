from typing import Optional
from pydantic import BaseModel

class PromoCodeBase(BaseModel):
    id: int


class PromoCodeCreate(PromoCodeBase):
    discount: float
    name: str


class PromoCodeUpdate(BaseModel):
    id: int = None
    discount: Optional[float] = None
    name: str = None


class PromoCode(PromoCodeBase):
    discount: Optional[float] = None
    name: str = None

