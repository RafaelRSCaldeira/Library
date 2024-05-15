from User import UserManager
from Book import BookManager

class Library():
    def __init__(self) -> None:
        self.bookManager = BookManager()
        self.userManager = UserManager()
    
    def registerUser(self, name: str) -> str:
        user = self.userManager.create(name)
        self.userManager.register(user)

    def registerBook(self, ISBN: str, title: str, author: str) -> str:
        book = self.bookManager.create(ISBN, title, author)
        self.bookManager.register(book)
    
    def loanBook(self, userID: int, bookISBN: str) -> str:
        if self.userManager.has(userID):
            if self.bookManager.has(bookISBN):
                return self.loan(userID, bookISBN)
            return "Livro não encontrado"
        return "Usuário não encontrado"

    def loan(self, userID: int, bookISBN: str) -> str:
        book = self.bookManager.search(bookISBN)
        if self.bookManager.isAvailable(bookISBN):
            self.bookManager.enqueueUser(userID, book.ISBN)
            message = f"Empréstimo de livro - ISBN: {book.ISBN} // Título: {book.title}"
            self.userManager.addHistory(userID, message)
            return "Livro emprestado com sucesso"
        return "Livro indisponível"

    
    def returnBook(self, bookISBN: str) -> str:
        if self.bookManager.has(bookISBN):
            if self.bookManager.isAvailable(bookISBN):
                return "O livro não foi emprestado"
            book = self.bookManager.search(bookISBN)
            userID = book.usersQueue.dequeue()
            message = f"Devolução de livro - ISBN: {book.ISBN} // Título: {book.title}"
            self.userManager.addHistory(userID, message)
            return "Livro devolvido com sucesso"
        return "Livro não encontrado"
    
    def reserveBook(self, userID: int, bookISBN: str) -> str:
        if self.bookManager.has(bookISBN):
            if self.userManager.has(userID):
                book = self.bookManager.search(bookISBN)
                self.bookManager.enqueueUser(userID, bookISBN)
                message = f"Reserva de livro - ISBN: {book.ISBN} // Título: {book.title}"
                self.userManager.addHistory(userID, message)
                return "Livro reservado com sucesso"
            return "Usuário não encontrado"
        return "Livro não encontrado"

    def showHistory(self, userID: int) -> str:
        self.userManager.showHistory(userID)
        return "Histórico exibido com sucesso"
    
    def undoHistory(self, userID: int) -> str:
        return self.userManager.undoHistory(userID)