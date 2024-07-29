from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(150), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    age = Column(Integer, nullable=True)
    password = Column(String, nullable=False)
    rolesId = Column(Integer, ForeignKey("roles.id"), nullable=False)
    paymentMethod = Column(String(150), nullable=True)

    roles = relationship("roles", back_populates="accounts")
