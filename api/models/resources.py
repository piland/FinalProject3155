from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from api.dependencies.database import Base


class Resource(Base):
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    item = Column(String(100), unique=True, nullable=False)
    amount = Column(DECIMAL, index=True, nullable=False, server_default='0.0')

    recipes = relationship("Recipe", back_populates="resource")

    def __repr__(self):
        return f"ID: {self.id}, ITEM: {self.item}, AMOUNT: {self.amount}"
