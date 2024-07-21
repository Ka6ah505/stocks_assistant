from app.repositories.stocks.stock_repository import StockRepository
from app.services.stocks.stock_service import IStockService


class StockService(IStockService):

    async def add_stocks(self, data):
        cnt = await StockRepository().add(data)
        return cnt

    async def load_stock_by_ticket(self, ticket: str):
        res = await StockRepository().load_candle_by_ticket(ticket)
        return res

    async def load_stock_filter(self, filter):
        return super().load_stock_filter(filter)

    async def load_stocks(self):
        res = await StockRepository().find_all()
        return res
