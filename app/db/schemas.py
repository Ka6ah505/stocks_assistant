"""
created: 2022-02-15
by: Mironov Sergei [ka6ah505@gmail.com]
"""
from datetime import datetime

from pydantic import BaseModel


class Record(BaseModel):
    ticket: str
    datetime: datetime
    open: float
    high: float
    low: float
    close: float
    volume: int
    timeframe: str


class Token(BaseModel):
    access_token: str
    token_type: str


class RecSt(BaseModel):
    id: int = None
    ticket: str
    close: float = None


class Bond(BaseModel):
    isin: str
    type_bond: str
    name: str
    mat_date: datetime
    coupon_value: float
    coupon_period: int
