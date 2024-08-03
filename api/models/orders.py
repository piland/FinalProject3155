from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from api.dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(String(100))
    order_date = Column(DATETIME, nullable=False, default=datetime.utcnow())
    description = Column(String(300))
    account_id = Column(Integer, ForeignKey("accounts.id"), nullable=False)

    accounts = relationship('Account', back_populates='order')
    order_details = relationship("OrderDetail", back_populates="order")
