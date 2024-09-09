"""
created: 2022-02-15
by: Mironov Sergei [ka6ah505@gmail.com]
"""
import enum
from sqlalchemy import Column, Float, String, MetaData, Table, TIMESTAMP, Enum
from sqlalchemy.orm import registry
from sqlalchemy.types import Integer

from app.db.schemas import Record, Bond

metadata = MetaData()
mapper_registry = registry(metadata=metadata)

stock_prices = Table(
    'stock_price',
    mapper_registry.metadata,
    Column('id', Integer, primary_key=True),
    Column('ticket', String, nullable=False),
    Column('datetime', TIMESTAMP(timezone=True), nullable=False),
    Column('open', Float, nullable=False),
    Column('high', Float, nullable=False),
    Column('close', Float, nullable=False),
    Column('low', Float, nullable=False),
    Column('volume', Integer, nullable=False),
    Column('timeframe', String, nullable=False),
)

mapper_registry.map_imperatively(Record, stock_prices)


class TypeBond(enum.Enum):
    TQOB = 'TQOB'


bonds = Table(
    'bond',
    mapper_registry.metadata,
    Column('isin', String, primary_key=True),
    Column('type_bond', Enum(TypeBond), nullable=False),
    Column('name', String, nullable=False),
    Column('mat_date',
           TIMESTAMP(timezone=True),
           nullable=False,
           comment='Дата погашения'
           ),
    Column('coupon_value', Float, nullable=False, comment='купон в валюте'),
    Column('coupon_period', Integer, nullable=False),
)

mapper_registry.map_imperatively(Bond, bonds)
