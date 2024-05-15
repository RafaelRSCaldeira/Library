from abc import ABC, abstractmethod

class InputInterface(ABC):
    @abstractmethod
    def get():
        pass

class InputNone(InputInterface):
    def get(self) -> None:
        return None

class InputTerminal(InputInterface):
    def get(self, message=""):
        return input(message)
    
    def getInteger(self, message="") -> None | int:
        userInput = input(message)
        try:
            userInput = int(userInput)
            return userInput
        except ValueError:
            return None

class InputFactory():
    @staticmethod
    def create(type: str) -> InputInterface:
        if type == "terminal":
            return InputTerminal()
        return InputNone()