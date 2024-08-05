from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Float
from sqlalchemy.orm import relationship

from ..dependencies.database import Base


class PromoCode(Base):
    __tablename__ = "promoCodes"

    name = Column(String(20), primary_key=True, index=True)
    discount = Column(Float, default=0)

