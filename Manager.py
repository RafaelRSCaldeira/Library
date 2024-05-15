from abc import ABC, abstractmethod

class Manager(ABC):
    @abstractmethod
    def create() -> object:
        pass

    @abstractmethod
    def register(self, obj) -> str:
        pass

    @abstractmethod
    def has(self, id) -> bool:
        pass

    @abstractmethod
    def search(self, id) -> object | None:
        pass

    @abstractmethod
    def remove(self, id) -> str:
        pass