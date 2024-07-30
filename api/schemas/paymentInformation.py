from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class PaymentInformationBase(BaseModel):
    balanceOnAccount: Optional[float]
    lastTransactionStatus: Optional[bool]

class PaymentInformationCreate(PaymentInformationBase):
    cardInformation: str
    paymentType: str

class PaymentInformationUpdate(BaseModel):
    cardInformation: Optional[str] = None
    balanceOnAccount: Optional[float] = None
    paymentType: Optional[str] = None
    lastTransactionStatus: Optional[bool] = None

class PaymentInformation(PaymentInformationBase):
    id: int
    cardInformation: str
    paymentType: str

    class ConfigDict:
        from_attributes = True