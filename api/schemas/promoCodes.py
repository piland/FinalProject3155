from typing import Optional
from pydantic import BaseModel

class PromoCodeBase(BaseModel):
    id: str


class PromoCodeCreate(PromoCodeBase):
    discount: float


class PromoCodeUpdate(BaseModel):
    id: str = None
    discount: Optional[float] = None


class PromoCode(PromoCodeBase):
    discount: Optional[float] = None

