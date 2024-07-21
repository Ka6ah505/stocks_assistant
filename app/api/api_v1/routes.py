"""
created: 2021-09-20
by: Mironov Sergei [ka6ah505@gmail.com]
"""
from typing import List

from fastapi import APIRouter

from app.db import schemas
from app.services.stocks.stock_service_impl import StockService

router = APIRouter(
    tags=["stocks"],
)


@router.get('/stocks', response_model=List[schemas.Record])
async def get_all():
    result = await StockService().load_stocks()
    return result


@router.get(
    '/stocks/{ticket}',
    response_model=List[schemas.Record],
    summary="Get stocks by ticket"
)
async def get_stocks(ticket: str) -> List[schemas.Record]:
    stocks = await StockService().load_stock_by_ticket(ticket)
    return stocks


@router.post('/stocks')
async def add(details: List[schemas.Record]):
    stocks = [d.model_dump() for d in details]
    count_new_rows = await StockService().add_stocks(stocks)
    return count_new_rows
