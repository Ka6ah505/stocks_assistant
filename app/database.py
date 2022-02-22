from config import BaseConfig

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


LINK_CONNECT_TO_BASE = f'postgresql+psycopg2://{BaseConfig.USER}:' \
                       f'{BaseConfig.PASSWORD}@' \
                       f'{BaseConfig.HOST}/' \
                       f'{BaseConfig.DATABASE}'


engine = create_engine(LINK_CONNECT_TO_BASE)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
