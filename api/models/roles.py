from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    description = Column(String(250), nullable=False)
    title = Column(String(250), nullable=False)

    accounts = relationship('Account', back_populates='roles')
