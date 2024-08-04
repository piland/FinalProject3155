from sqlalchemy import Column, Integer, String, DECIMAL, BOOLEAN
from sqlalchemy.orm import relationship
from api.dependencies.database import Base


class PaymentInformation(Base):
    __tablename__ = 'payment_information'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    balance_on_account = Column(DECIMAL, default=0)
    card_information = Column(String(100), nullable=False)
    payment_type = Column(String(100), nullable=False)
    last_transaction_status = Column(BOOLEAN, nullable=True)

    accounts = relationship('Account', back_populates='payment_information')
