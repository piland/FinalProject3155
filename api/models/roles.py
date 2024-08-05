from typing import List
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from api.dependencies.database import Base

class Role(Base):
    __tablename__ = 'roles'

    id = mapped_column(Integer, primary_key=True, index=True, nullable=False)
    title = Column(String(50), nullable=False)
    description = Column(String(250), nullable=False)

    accounts = relationship("Account", back_populates='roles')
