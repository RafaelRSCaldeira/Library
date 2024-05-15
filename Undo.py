from User import *
from Book import *


class Undo():
    def __init__(self):
        self.userManager = UserManager()
        self.bookManager = BookManager()

    '''@staticmethod
    def undo(self, userID: int) -> str:
        user = self.userManager.search(userID)
        lastMessage = user.history.pop()
        last = lastMessage[:10]
        if last == "Empréstimo":
            bookISBN = 
            return Undo.loan(userID, bookISBN, book)
        if last == "Devolução ":
            return Undo.devolution(userID, bookISBN, book)
        if last == "Reserva de":
            return Undo.reserve(userID, bookISBN, book)
        return "Mensagem não reconhecida"'''

    @staticmethod
    def loan(userID: int, book: Book) -> str:
        book.usersQueue.remove(userID)
        return "Empréstimo desfeito com sucesso"
    
    @staticmethod
    def devolution(userID: int, book: Book) -> str:
        book.usersQueue.insert(userID, 0)
        return "Devolução desfeita com sucesso"
    
    @staticmethod
    def reserve(userID: int, book: Book) -> str:
        book.usersQueue.remove(userID)
        return "Reserva desfeita com sucesso"

