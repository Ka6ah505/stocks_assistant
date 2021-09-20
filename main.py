"""
created: 2021-09-20
by: Mironov Sergei [ka6ah505@gmail.coms]
"""
from fastapi import FastAPI
from app.api.api_v1 import routes


app = FastAPI()


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
