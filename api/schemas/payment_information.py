from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .sandwiches import Sandwich


class PaymentInformationBase(BaseModel):
    balance_on_account: Optional[float]
    last_transaction_status: Optional[bool]


class PaymentInformationCreate(PaymentInformationBase):
    card_information: str
    payment_type: str


class PaymentInformationUpdate(BaseModel):
    card_information: Optional[str] = None
    balance_on_account: Optional[float] = None
    payment_type: Optional[str] = None
    last_transaction_status: Optional[bool] = None


class PaymentInformation(PaymentInformationBase):
    id: int
    card_information: str
    payment_type: str

    class Config:
        from_attributes = True
