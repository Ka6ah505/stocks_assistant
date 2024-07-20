from sqlalchemy import insert, select
from typing import List

from app.db.database import async_session_maker
from app.repositories.abstract_repository import AbstractRepository


class SqlAlchemyRepository(AbstractRepository):
    model = None

    async def add_one(self, data: dict) -> int:
        async with async_session_maker() as session:
            stmt = insert(self.model).values(**data).returning(self.model)
            res = await session.execute(stmt)
            await session.commit()
            return len(res.all())
    
    async def add(self, data: List[dict]) -> int:
        async with async_session_maker() as session:
            stmt = insert(self.model).values(data).returning(self.model)
            res = await session.execute(stmt)
            await session.commit()
            return len(res.all())

    async def find_all(self):
        async with async_session_maker() as session:
            stmt = select(self.model)
            res = await session.execute(stmt)
            return [row for row in res.all()]

    async def find(self, filter):
        async with async_session_maker() as session:
            stmt = select(self.model).filter_by(**filter)
            res = await session.execute(stmt)
            return [row for row in res.all()]
