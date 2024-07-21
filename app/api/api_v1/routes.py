"""
created: 2021-09-20
by: Mironov Sergei [ka6ah505@gmail.com]
"""
from typing import List

from fastapi import APIRouter

from app.db import schemas
from app.repositories.stocks.stock_repository import StockRepository

router = APIRouter(
    tags=["stocks"],
)


@router.get('/stocks', response_model=List[schemas.Record])
async def get_all():
    result = await StockRepository().find_all()
    return result


@router.get(
    '/stocks/{ticket}',
    response_model=List[schemas.Record],
    summary="Get stocks by ticket"
)
async def get_stocks(ticket: str) -> List[schemas.Record]:
    stocks = await StockRepository().find({'ticket': ticket})
    return stocks


@router.post('/stocks')
async def add(details: List[schemas.Record]):
    stock_dict = [d.model_dump() for d in details]
    count_new_rows = await StockRepository().add(stock_dict)
    return count_new_rows


@router.post('/add_row', summary="Add one row")
async def add_row(details: schemas.Record):
    stock_dict = details.model_dump()
    new_row = await StockRepository().add_one(stock_dict)
    return new_row
