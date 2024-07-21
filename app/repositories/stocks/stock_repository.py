from sqlalchemy import select
from app.db.schemas import Record
from app.db.models import stock_prices
from app.db.database import async_session_maker
from app.repositories.sql_alchemy_repository import SqlAlchemyRepository


class StockRepository(SqlAlchemyRepository):
    model = stock_prices

    async def add_row(self, data: dict):
        res = await self.add_one(data)
        return res

    async def load_candle_by_ticket(self, ticket: str):
        async with async_session_maker() as session:
            stmt = select(self.model).where(Record.ticket == ticket)
            res = await session.execute(stmt)
            return [row for row in res.all()]
