from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    stars = Column(Integer, nullable=False)
    description = Column(String(750), nullable=False, default="")
    accountId = Column(Integer, ForeignKey("accounts.id"), nullable=False)

    account = relationship("Account", back_populates="reviews")

    def __repr__(self):
        return f"ID: {self.id}, STARS: {self.stars}, DESCRIPTION: {self.description}"