from app.db.models import bonds
from app.repositories.sql_alchemy_repository import SqlAlchemyRepository


class BondRepository(SqlAlchemyRepository):
    model = bonds

    async def add_row(self, data: dict):
        res = await self.add_one(data)
        return res
