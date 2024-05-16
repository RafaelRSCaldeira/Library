from UserManagerWithoutUndo import UserManagerWithoutUndo
from User import User
from Undo import Undo

class UserManager(UserManagerWithoutUndo):
    def __init__(self):
        self.users = dict()

    def undoHistory(self, userID: int, users: dict, books: dict) -> str:
        if self.has(userID):
            user = self.search(userID)
            if len(user.history) == 0:
                return "Histórico vazio"
            return Undo.undo(userID, users, books)
        return "Usuário não encontrado"
