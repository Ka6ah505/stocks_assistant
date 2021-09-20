"""
created: 2021-09-20
by: Mironov Sergei [ka6ah505@gmail.com]
"""
import os
from fastapi import APIRouter

router = APIRouter()

@router.get("/info", status_code=200)
async def info():
    """ Получаем информацию о системе"""
    response  = os.uname()
    return response
