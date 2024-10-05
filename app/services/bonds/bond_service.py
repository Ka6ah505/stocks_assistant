from abc import ABC, abstractmethod


class IBondService(ABC):

    @abstractmethod
    def add_bond(self):
        raise NotImplementedError
