from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class AccountBase(BaseModel):
    name: str
    age: Optional[int] = None

class AccountCreate(AccountBase):
    email: str
    password: str

class AccountUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    email: Optional[str] = None
    password: Optional[str] = None

class Account(AccountBase):
    id: int
    email: str
    password: str

    class ConfigDict:
        from_attributes = True