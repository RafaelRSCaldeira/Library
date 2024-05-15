from abc import ABC, abstractmethod

class InputInterface(ABC):
    @abstractmethod
    def get():
        pass

class InputNone(InputInterface):
    def get(self) -> None:
        return None

class InputTerminal(InputInterface):
    def get(self):
        return input()

class InputFactory():
    @staticmethod
    def create(type: str) -> InputInterface:
        if type == "terminal":
            return InputTerminal()