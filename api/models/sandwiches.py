from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from ..dependencies.database import Base
from api.models.order_details import OrderDetail


class Sandwich(Base):
    __tablename__ = "sandwiches"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    sandwich_name = Column(String(100), unique=True, nullable=True)
    price = Column(DECIMAL(4, 2), nullable=False, server_default='0.0')

    recipes = relationship("Recipe", back_populates="sandwich")
    order_details = relationship("OrderDetail", back_populates="sandwich")

    def __repr__(self):
        return f"ID: {self.id}, SANDWICH NAME: {self.sandwich_name}, PRICE: {self.price}"
