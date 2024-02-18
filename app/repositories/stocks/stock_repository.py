from app.db.models import stock_prices
from app.repositories.sql_alchemy_repository import SqlAlchemyRepository


class StockRepository(SqlAlchemyRepository):
    model = stock_prices
