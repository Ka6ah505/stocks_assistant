"""
created: 2022-02-15
by: Mironov Sergei [ka6ah505@gmail.com]
"""
from datetime import datetime

from sqlalchemy import Column, Float, String, MetaData, Table, DateTime
from sqlalchemy.types import Integer

metadata = MetaData()

stock_prices = Table(
    'stock_prices',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('stock', String, nullable=False),
    Column('date_time', DateTime, nullable=False),
    Column('open', Float, nullable=False),
    Column('high', Float, nullable=False),
    Column('close', Float, nullable=False),
    Column('low', Float, nullable=False),
    Column('volume', Integer, nullable=False),
    Column('time_frame', String, nullable=False),

)
