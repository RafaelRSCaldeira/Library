from Manager import Manager
from Undo import Undo

class User():
    id = 1

    def __init__(self, name: str) -> None:
        self.id = User.id
        self.name = name
        self.history = list()
        User.id += 1

class UserManager(Manager):
    def __init__(self):
        self.users = dict()

    def register(self, user: User) -> str:
        if self.has(user.id):
            return "Usuário já cadastrado"
        self.users[user.id] = user
        return "Usuário cadastrado com sucesso"

    def has(self, userID: int) -> bool:
        if userID in self.users:
            return True
        return False
    
    def search(self, userID: int) -> User | str:
        if self.has(userID):
            return self.users[userID]
        return "Usuário não encontrado"
    
    def remove(self, userID: int) -> str:
        if self.has(userID):
            del self.users[userID]
            return "Usuário removido com sucesso"
        return "Usuário não encontrado"

    def addHistory(self, userID: int, message: str) -> str:
        user = self.users[userID]
        user.history.append(message)
        return "Histórico atualizado"
    
    def undoHistory(self, userID: int) -> str:
        if self.has(userID):
            user = self.search(userID)
            if len(user.history) == 0:
                return "Histórico vazio"
            Undo.undo(userID)
            return "Última ação desfeita com sucesso"
        return "Usuário não encontrado"

    def showHistory(self, userID: int) -> None:
        if self.has(userID):
            user = self.search(userID)
            for i in range(len(user.history)):
                print(f"{i}: {user.history[i]}")
            