from sqlalchemy import Column, Float, String
from sqlalchemy.types import Integer

from .database import Base


class StockPrice(Base):
    __tablename__ = 'stock_prices'

    ticket = Column(String(100), index=True)
    date_candle = Column(Integer)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Integer)
    time_frame = Column(String(100))
    id = Column(Integer, primary_key=True)


class Stock(Base):
    __tablename__ = 'stock'

    id = Column(Integer, primary_key=True)
    ticket = Column(String(10))
