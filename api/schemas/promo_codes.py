from typing import Optional
from pydantic import BaseModel


class PromoCodeBase(BaseModel):
    pass


class PromoCodeCreate(PromoCodeBase):
    discount: float
    name: str


class PromoCodeUpdate(BaseModel):
    discount: Optional[float] = None
    name: Optional[str] = None


class PromoCode(PromoCodeBase):
    discount: float
    name: str

    class Config:
        from_attributes = True
