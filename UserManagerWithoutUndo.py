from User import User

class UserManagerWithoutUndo():
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance
    
    def __init__(self, users: dict):
        self.users = users

    def create(self, name: str) -> User:
        return User(name)

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
        if self.has(userID):
            user = self.users[userID]
            user.history.append(message)
            return "Histórico atualizado"
        return "Usuário não encontrado"

    def showHistory(self, userID: int) -> str:
        if self.has(userID):
            user = self.search(userID)
            for i in range(len(user.history)):
                print(f"{i+1}: {user.history[i]}")
            return "Histórico exibido com sucesso"
        return "Usuário não encontrado"
            