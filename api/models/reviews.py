from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, mapped_column
from api.dependencies.database import Base


class Review(Base):
    __tablename__ = "reviews"

    id = mapped_column(Integer, primary_key=True, autoincrement=True, index=True)
    stars = Column(Integer, nullable=False)
    description = Column(String(750), nullable=False, default="")
    account_id = Column(Integer, ForeignKey("accounts.id"), nullable=False)
    sandwich_id = Column(Integer, ForeignKey("sandwiches.id"), nullable=False)

    account = relationship("Account", back_populates="reviews")
    sandwich = relationship("Sandwich", back_populates="reviews")
