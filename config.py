import os
from pydantic import BaseConfig


class BaseConfig(BaseConfig):
    HOST = os.getenv('HOST', '')
    DATABASE = os.getenv('DATABASE', '')
    PORT = os.getenv('PORT', '')
    USER = os.getenv('USESR', '')
    PASSWORD = os.getenv('PASSWORD', '')

    class Config:
        pass
