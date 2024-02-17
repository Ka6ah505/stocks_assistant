from abc import ABC, abstractmethod


class AbstractRepository(ABC):

    @abstractmethod
    def add_one(self):
        raise NotImplementedError

    @abstractmethod
    def find_all(self):
        raise NotImplementedError
