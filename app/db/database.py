"""
created: 2022-02-15
by: Mironov Sergei [ka6ah505@gmail.com]
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# from app.core.config import BaseConfig
from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASS


LINK_CONNECT_TO_BASE = f'postgresql+asyncpg://{DB_USER}:{DB_PORT}' \
                       f'{DB_PASS}@' \
                       f'{DB_HOST}/' \
                       f'{DB_NAME}'


engine = create_engine(LINK_CONNECT_TO_BASE)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()
