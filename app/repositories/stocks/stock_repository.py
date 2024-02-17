from app.db.schemas import Record
from app.repositories.sql_alchemy_repository import SqlAlchemyRepository
from app.db.models import stock_prices


class StockRepository(SqlAlchemyRepository):
    model = stock_prices
