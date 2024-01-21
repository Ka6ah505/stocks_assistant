"""
created: 2021-09-20
by: Mironov Sergei [ka6ah505@gmail.com]
"""
import platform

from fastapi import APIRouter, Depends
from typing import List

from sqlalchemy import insert, select

from app.db import models, schemas
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_async_session

router = APIRouter()


@router.get("/info", status_code=200)
async def info():
    """ Получаем информацию о системе"""
    response = platform.system()
    return response


@router.get('/all', response_model=List[schemas.Record])
async def get_all(session: AsyncSession = Depends(get_async_session)):
    query = select(models.stock_prices)
    result = await session.execute(query)
    return result.all()


@router.get('/prices/{ticket}', response_model=List[schemas.Record])
async def get_all(ticket: str, session: AsyncSession = Depends(get_async_session)):
    query = select(models.stock_prices).where(models.stock_prices.c.ticket == ticket)
    result = await session.execute(query)
    return result.all()


@router.post('/add')
async def add(details: schemas.Record, session: AsyncSession = Depends(get_async_session)):
    stocks = insert(models.stock_prices).values(**details.dict())
    try:
        await session.execute(stocks)
        await session.commit()
    except Exception as ex:
        print(f'Error - {ex}')
        return {
            "success": False,
        }
    return {
        "success": True,
    }
