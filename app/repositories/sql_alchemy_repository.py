from sqlalchemy import insert, select

from app.db.database import async_session_maker
from app.repositories.abstract_repository import AbstractRepository


class SqlAlchemyRepository(AbstractRepository):
    model = None

    async def add_one(self, data: dict) -> dict:
        async with async_session_maker() as session:
            stmt = insert(self.model).values(**data).returning(self.model)
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one()

    async def find_all(self):
        async with async_session_maker() as session:
            stmt = select(self.model)
            res = await session.execute(stmt)
            return [row for row in res.all()]
