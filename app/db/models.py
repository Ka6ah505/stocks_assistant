"""
created: 2022-02-15
by: Mironov Sergei [ka6ah505@gmail.com]
"""
from sqlalchemy import Column, Float, String
from sqlalchemy.types import Integer
from app.db.database import Base


class StockPrice(Base):
    """ Таблица с параметрами свечей финансового инструмента
    """
    __tablename__ = 'stock_prices'

    ticket = Column(String(100), index=True)
    dateCandle = Column(Integer)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Integer)
    timeFrame = Column(String(10))
    id = Column(Integer, primary_key=True)


class Stock(Base):
    """ Таблица с закрытием цены по инструменту (sandbox)
    """
    __tablename__ = 'stock'

    id = Column(Integer, primary_key=True)
    ticket = Column(String(10))
    close = Column(Float, nullable=True)
