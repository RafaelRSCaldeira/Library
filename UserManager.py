from UserManagerWithoutUndo import UserManagerWithoutUndo
from User import User
from Undo import Undo

class UserManager(UserManagerWithoutUndo):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self):
        self.users = dict()

    def undoHistory(self, userID: int, users: dict, books: dict) -> str:
        if self.has(userID):
            user = self.search(userID)
            if len(user.history) == 0:
                return "Histórico vazio"
            return Undo.undo(userID, users, books)
        return "Usuário não encontrado"