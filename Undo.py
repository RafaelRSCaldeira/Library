from UserManagerWithoutUndo import UserManagerWithoutUndo
from User import User
from Book import Book
from BookManager import BookManager
import re


class Undo():
    @staticmethod
    def undo(userID: int, users: dict, books: dict) -> str:
        userManager = UserManagerWithoutUndo(users)
        bookManager = BookManager(books)
        user = userManager.search(userID)
        lastMessage = user.history.pop()
        last = lastMessage[:10]
        bookISBN = re.search("^.*ISBN:(.*)//", lastMessage).group(1).strip()
        book = bookManager.search(bookISBN)
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

