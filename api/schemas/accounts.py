from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .sandwiches import Sandwich

class AccountBase(BaseModel):
    name: str
    age: Optional[int] = None
    phoneNumber: Optional[str] = None

class AccountCreate(AccountBase):
    email: str
    password: str

class AccountUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    email: Optional[str] = None
    password: Optional[str] = None
    phoneNumber: Optional[str] = None

class Account(AccountBase):
    id: int
    email: str
    password: str

    class Config:
        from_attributes = True