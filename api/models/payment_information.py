from sqlalchemy import Column, Integer, String, DECIMAL, BOOLEAN
from sqlalchemy.orm import relationship
from api.dependencies.database import Base


class PaymentInformation(Base):
    __tablename__ = 'payment_information'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    balance_on_account = Column(DECIMAL, default=0)
    card_information = Column(String(100), nullable=False)
    payment_type = Column(String(100), nullable=False)

    accounts = relationship('Account', back_populates='payment_information')

    def __repr__(self):
        return f"ID: {self.id}, Balance: {self.balance_on_account}, Type: {self.payment_type}"
