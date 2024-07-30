from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .sandwiches import Sandwich



class ReviewBase(BaseModel):
    pass


class ReviewCreate(ReviewBase):
    stars: int
    description: str


class ReviewUpdate(BaseModel):
    stars: Optional[int] = None
    description: Optional[str] = None


class Review(ReviewBase):
    id: int
    stars: int
    description: str

    class Config:
        from_attributes = True
