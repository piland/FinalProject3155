from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Float
from ..dependencies.database import Base


class PromoCode(Base):
    __tablename__ = "promoCodes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(20), unique=True, nullable=False)
    discount = Column(Float, default=0)


