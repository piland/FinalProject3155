from pydantic import BaseModel
from typing import Optional


class AccountBase(BaseModel):
    name: str
    age: Optional[int] = None
    phone_number: Optional[str] = None


class AccountCreate(AccountBase):
    email: str
    password: str
    role_id: int
    payment_information_id: int


class AccountUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    email: Optional[str] = None
    password: Optional[str] = None
    phone_number: Optional[str] = None
    role_id: Optional[int] = None
    payment_information_id: Optional[int] = None


class Account(AccountBase):
    id: int
    email: str
    password: str
    role_id: int
    payment_information_id: int

    class Config:
        from_attributes = True
