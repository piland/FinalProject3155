from sqlalchemy import Column, ForeignKey, Integer, String, DATETIME
from sqlalchemy.orm import relationship, mapped_column
from datetime import datetime
from api.dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = mapped_column(String(100))
    order_date = mapped_column(DATETIME, nullable=False, default=datetime.utcnow)
    description = mapped_column(String(300))
    order_type = mapped_column(String(100))
    account_id = mapped_column(Integer, ForeignKey("accounts.id"))

    accounts = relationship('Account', back_populates="orders")
    order_details = relationship("OrderDetail", back_populates="order")


