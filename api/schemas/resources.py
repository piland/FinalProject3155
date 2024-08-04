from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ResourceBase(BaseModel):
    item: str
    amount: int
    price: int


class ResourceCreate(ResourceBase):
    pass


class ResourceUpdate(BaseModel):
    item: Optional[str] = None
    amount: Optional[int] = None
    price : Optional[float] = None


class Resource(ResourceBase):
    id: int

    class Config:
        from_attributes = True
