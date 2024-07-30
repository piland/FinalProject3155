from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class PaymentInformation(Base):
    __tablename__ = 'paymentInformation'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    balanceOnAccount = Column(DECIMAL, default=0)
    cardInformation = Column(String, nullable=False)
    paymentType = Column(String, nullable=False)
    lastTransactionStatus = Column(bool, nullable=True)

    accounts = relationship('accounts', back_populates='paymentInformation')
