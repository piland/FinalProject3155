from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, BOOLEAN
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class PaymentInformation(Base):
    __tablename__ = 'paymentInformation'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    balanceOnAccount = Column(DECIMAL, default=0)
    cardInformation = Column(String(100), nullable=False)
    paymentType = Column(String(100), nullable=False)
    lastTransactionStatus = Column(BOOLEAN, nullable=True)

    accounts = relationship('Account', back_populates='paymentInformation')
