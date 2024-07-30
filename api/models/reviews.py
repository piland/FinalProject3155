from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    stars = Column(Integer, nullable=False)
    description = Column(String, nullable=False, default="")
    accountId = Column(Integer, ForeignKey("accounts.id"), nullable=False)

    accounts = relationship("reviews", back_populates="accounts")