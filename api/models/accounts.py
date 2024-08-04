from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, mapped_column
from api.dependencies.database import Base

class Account(Base):
    __tablename__ = "accounts"

    id = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(150), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    age = Column(Integer, nullable=True)
    phone_number = Column(String(25), nullable=True)
    password = Column(String(100), nullable=False)
    role_id = mapped_column(Integer, ForeignKey("roles.id"), nullable=False)
    payment_information_id = mapped_column(Integer, ForeignKey("payment_information.id"), nullable=True)

    reviews = relationship("Review", back_populates="account")
    orders = relationship("Order", back_populates="accounts")
    payment_information = relationship("PaymentInformation", back_populates="accounts")
    roles = relationship("Role", back_populates="accounts")
