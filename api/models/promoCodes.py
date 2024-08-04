from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Float
from ..dependencies.database import Base


class PromoCode(Base):
    __tablename__ = "promoCodes"

    id = Column(String(20), primary_key=True, index=True)
    discount = Column(Float, default=0)
