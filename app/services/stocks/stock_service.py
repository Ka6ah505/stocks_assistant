from abc import ABC, abstractmethod


class IStockService(ABC):

    @abstractmethod
    def add_stocks(data):
        raise NotImplementedError

    @abstractmethod
    def load_stock_filter(filter):
        raise NotImplementedError

    @abstractmethod
    def load_stock_by_ticket(self: str):
        raise NotImplementedError
