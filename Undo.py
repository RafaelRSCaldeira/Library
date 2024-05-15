from User import *
from Book import *
import re


class Undo():
    def __init__(self):
        self.userManager = UserManager()
        self.bookManager = BookManager()

    @staticmethod
    def undo(self, userID: int) -> str:
        user = self.userManager.search(userID)
        lastMessage = user.history.pop()
        last = lastMessage[:10]
        bookISBN = re.search("^.*ISBN:(.*)//", lastMessage).group(1).strip()
        book = self.bookManager.search(bookISBN)
        if last == "Empréstimo":
            return Undo.loan(userID, book)
        if last == "Devolução ":
            return Undo.devolution(userID, book)
        if last == "Reserva de":
            return Undo.reserve(userID, book)
        return "Mensagem não reconhecida"

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

