from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .sandwiches import Sandwich



class ReviewBase(BaseModel):
    pass


class ReviewCreate(ReviewBase):
    stars: int
    description: str
    account_id: int


class ReviewUpdate(BaseModel):
    stars: Optional[int] = None
    description: Optional[str] = None
    account_id: Optional[int] = None


class Review(ReviewBase):
    id: int
    stars: int
    description: str
    account_id: int

    class Config:
        from_attributes = True
