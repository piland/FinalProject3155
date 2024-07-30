from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class RoleBase(BaseModel):
    title: str
    description: str

class RoleCreate(RoleBase):
    pass

class RoleUpdate(BaseModel):
    title = Optional[str]
    description: Optional[str] = None


class Role(RoleBase):
    id: int

    class Config:
        from_attributes = True