"""
created: 2021-09-20
by: Mironov Sergei [ka6ah505@gmail.coms]
"""
from fastapi import FastAPI, Depends
from app.api.api_v1 import routes


from typing import List
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from app import models, schemas
from app.database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


@app.on_event("startup")
async def startup():
    """Когда приложение запускается"""
    pass


@app.on_event("shutdown")
async def shutdown():
    """Когда приложение останавливается"""
    pass


@app.get('/')
async def root():
    """Простой эндпоинт для проверки работоспособности
    """
    return {"message": "All right!"}

app.include_router(routes.router, prefix="/api/v1")


@app.get('/all', response_model=List[schemas.RecSt])
async def get_all(db: Session = Depends(get_db)):
    records = db.query(models.Stock).all()
    return records
