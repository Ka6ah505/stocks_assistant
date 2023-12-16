import os
from pydantic import BaseConfig


class BaseConfig(BaseConfig):
    DB_HOST = os.getenv('DB_HOST', '')
    DB_NAME = os.getenv('DB_NAME', '')
    DB_PORT = os.getenv('DB_PORT', '')
    DB_USER = os.getenv('DB_USER', '')
    DB_PASS = os.getenv('DB_PASS', '')

    class Config:
        pass
