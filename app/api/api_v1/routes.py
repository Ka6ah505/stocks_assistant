"""
created: 2021-09-20
by: Mironov Sergei [ka6ah505@gmail.com]
"""
import os
from fastapi import APIRouter, Depends
from typing import List
from app.db import models, schemas
from sqlalchemy.orm import Session
from app.db.database import SessionLocal

router = APIRouter()


# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@router.get("/info", status_code=200)
async def info():
    """ Получаем информацию о системе"""
    response = os.uname()
    return response


@router.get('/all', response_model=List[schemas.Record])
async def get_all(db: Session = Depends(get_db)):
    records = db.query(models.StockPrice).all()
    return records


@router.get('/prices/{ticket}', response_model=List[schemas.Record])
async def get_all(ticket: str, db: Session = Depends(get_db)):
    records = db.query(models.StockPrice).filter(models.StockPrice.ticket == ticket).all()
    return records


@router.post('/add')
async def add(details: schemas.Record, db: Session = Depends(get_db)):
    to_create = models.StockPrice(
        ticket=details.ticket,
        dateCandle=details.dateCandle,
        open=details.open,
        high=details.high,
        low=details.low,
        close=details.close,
        volume=details.volume,
        timeFrame=details.timeFrame
    )
    try:
        db.add(to_create)
        db.commit()
    except:
        return {
            "success": False,
            "created_id": to_create.id
        }
    return {
        "success": True,
        "created_id": to_create.id
    }
