"""
created: 2021-09-20
by: Mironov Sergei [ka6ah505@gmail.com]
"""
import platform
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import models, schemas
from app.db.database import get_async_session
from app.repositories.stocks.stock_repository import StockRepository

router = APIRouter()


@router.get("/info", status_code=200)
async def info():
    """ Получаем информацию о системе"""
    response = platform.system()
    return response


@router.get('/all', response_model=List[schemas.Record])
async def get_all():
    result = await StockRepository().find_all()
    return result


@router.get('/prices/{ticket}', response_model=List[schemas.Record])
async def get_all(ticket: str, session: AsyncSession = Depends(get_async_session)):
    query = select(models.stock_prices).where(models.stock_prices.c.ticket == ticket)
    result = await session.execute(query)
    return result.all()


@router.post('/add')
async def add(details: schemas.Record):
    stock_dict = details.model_dump()
    result = await StockRepository().add_one(stock_dict)
    return result
