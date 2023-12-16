"""
created: 2022-02-15
by: Mironov Sergei [ka6ah505@gmail.com]
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import BaseConfig


LINK_CONNECT_TO_BASE = f'postgresql+psycopg2://{BaseConfig.DB_USER}:' \
                       f'{BaseConfig.DB_PASS}@' \
                       f'{BaseConfig.DB_HOST}/' \
                       f'{BaseConfig.DB_NAME}'


engine = create_engine(LINK_CONNECT_TO_BASE)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
