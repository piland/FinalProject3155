from pydantic import BaseModel
from typing import Optional


class ReviewBase(BaseModel):
    stars: int
    description: str


class ReviewCreate(ReviewBase):
    account_id: int
    sandwich_id: int


class ReviewUpdate(ReviewBase):
    account_id: Optional[int] = None
    description: Optional[str] = None
    stars: Optional[int] = None

class Review(ReviewBase):
    id: int
    account_id: int
    sandwich_id: int

    class Config:
        from_attributes = True
