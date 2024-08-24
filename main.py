"""
created: 2021-09-20
by: Mironov Sergei [ka6ah505@gmail.com]
"""
import platform
from fastapi import FastAPI
from fastapi_cache import FastAPICache
from app.api.api_v1 import routes
from app.db.redis_db import redis
from fastapi_cache.decorator import cache

from fastapi.middleware.cors import CORSMiddleware


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
    FastAPICache.init(redis, prefix="fastapi-cache")


@app.on_event("shutdown")
async def shutdown():
    """Когда приложение останавливается"""
    pass


@app.get('/', status_code=200, tags=["System"])
@cache(expire=10)
async def root():
    """Простой эндпоинт для проверки работоспособности
    """
    return {"message": "All right!"}


@app.get("/info", status_code=200, summary="Get system name", tags=["System"])
async def info():
    """ Получаем информацию о системе"""
    response = platform.system()
    return response


app.include_router(routes.router, prefix="/api/v1")
