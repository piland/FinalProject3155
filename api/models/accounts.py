from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from api.dependencies.database import Base

class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(150), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    age = Column(Integer, nullable=True)
    phoneNumber = Column(String(25), nullable=True)
    password = Column(String(100), nullable=False)
    rolesId = Column(Integer, ForeignKey("roles.id"), nullable=False)
    paymentInformationId = Column(Integer, ForeignKey("paymentInformation.id"), nullable=False)

    reviews = relationship("Review", back_populates="account")
    orders = relationship("Order", back_populates="account")
    paymentInformation = relationship("PaymentInformation", back_populates="accounts")
    roles = relationship("Role", back_populates="accounts")
