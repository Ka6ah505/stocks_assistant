"""
created: 2021-09-20
by: Mironov Sergei [ka6ah505@gmail.com]
"""
import platform

from fastapi import APIRouter, Depends
from typing import List

from sqlalchemy import insert, select

from app.db import models, schemas
from sqlalchemy.orm import Session
from app.db.database import SessionLocal

router = APIRouter()


# Dependency
def get_db():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_authentically_user(token: str = "", db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    record = db.query(models.Users).filter(models.Users.token == token).first()
    if record:
        return True
    raise credentials_exception


@router.get("/info", status_code=200)
async def info():
    """ Получаем информацию о системе"""
    response = platform.system()
    return response


@router.get('/all', response_model=List[schemas.Record])
async def get_all(session: Session = Depends(get_db)):
    query = select(models.stock_prices)
    result = session.execute(query)
    return result.all()


@router.get('/prices/{ticket}', response_model=List[schemas.Record])
async def get_all(ticket: str, session: Session = Depends(get_db)):
    query = select(models.stock_prices).where(models.stock_prices.c.ticket == ticket)
    result = session.execute(query)
    return result.all()


@router.post('/add')
async def add(details: schemas.Record, session: Session = Depends(get_db)):
    stocks = insert(models.stock_prices).values(details.dict())
    try:
        session.execute(stocks)
        session.commit()
    except Exception as ex:
        print(ex)
        return {
            "success": False,
        }
    return {
        "success": True,
    }
