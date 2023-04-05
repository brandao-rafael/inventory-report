from abc import ABC, abstractmethod


class Importer(ABC):
    def __init__(self, strategy) -> None:
        self.__strategy = strategy

    @abstractmethod
    def import_data(self, path):
        self.__strategy.import_data(path)
