from Manager import Manager
from Queue import Queue

class Book():
    def __init__(self, ISBN: str, title: str, author: str) -> None:
        self.ISBN = ISBN
        self.title = title
        self.author = author
        self.usersQueue = Queue()


class BookManager(Manager):
    def __init__(self):
        self.books = dict()

    def create(self, ISBN: str, title: str, author: str) -> Book:
        return Book(ISBN, title, author)

    def register(self, book: Book) -> str:
        if self.hasBook(book.ISBN):
            return "Livro já cadastrado"
        self.books[book.ISBN] = book
        return "Livro cadastrado com sucesso"
    
    def has(self, bookISBN: Book) -> bool:
        if bookISBN in self.books:
            return True
        return False

    def search(self, bookISBN: str) -> Book | str:
        if self.has(bookISBN):
            return self.books[bookISBN]
        return "Livro não encontrado"
    
    def remove(self, bookISBN: str) -> str:
        if self.has(bookISBN):
            del self.books[bookISBN]
            return "Livro removido com sucesso"
        return "Livro não encontrado"

    def isAvailable(self, bookISBN: str) -> str | bool:
        if self.has(bookISBN):
            if len(self.books[bookISBN].usersQueue) == 0:
                return True
            return False
        return "Livro não encontrado"

    def enqueueUser(self, userID: int, bookISBN: str) -> str:
        if self.has(bookISBN):
            book = self.books[bookISBN]
            book.usersQueue.enqueue(userID)
            return "Enfileirado com sucesso"
        return "Livro não encontrado"
    
    def dequeueUser(self, bookISBN: str) -> str:
        if self.has(bookISBN):
            if self.isAvailable(bookISBN):
                return "Nenhum usuário na fila"
            book = self.books[bookISBN]
            book.usersQueue.dequeue()
            return "Usuário removido com sucesso"
        return "Livro não encontrado"
