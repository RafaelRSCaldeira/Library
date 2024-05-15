from Input import *
from Library import Library

class Interface():
    def __init__(self, inputType="terminal"):
        self.input = InputFactory.create(inputType)
        self.library = Library()
    
    def showMenu(self) -> None:
        menu = '''Opções:\n\
            (1) Adicionar usuário\n\
            (2) Adicionar livro\n\
            (3) Empréstimo de livro\n\
            (4) Devolução de livro\n\
            (5) Reserva de livro\n\
            (6) Revisar histórico de operações\n\
            (7) Desfazer operação'''
        print(menu)
    
    def getOption(self) -> None | str:
        option = self.input.getInteger("Escolha a opção desejada: ")
        if option is None:
            return "Valor inválido"
        self.doOption(option)
    
    def doOption(self, option: int) -> str:
        if option == 1:
            return self.registerUser()
        if option == 2:
            return self.registerBook()
        if option == 3:
            return self.loanBook()
        if option == 4:
            return self.returnBook()
        if option == 5:
            return self.reserveBook()
        if option == 6:
            return self.showHistory()
        if option == 7:
            return self.undoHistory()
        return "Opção inválida"
    
    def registerUser(self) -> str:
        name = self.input.get("Digite o nome do usuário: ")
        return self.library.registerUser(name)

    def registerBook(self) -> str:
        title = self.input.get("Digite o título do livro: ")
        author = self.input.get("Digite o nome do autor: ")
        ISBN = self.input.get("Digite o ISBN do livro: ")
        return self.library.registerBook(ISBN, title, author)
    
    def loanBook(self) -> str:
        userID = self.input.get("Digite o ID do usuário: ")
        try:
            userID = int(userID)
        except ValueError:
            return "ID inválido"
        bookISBN = self.input.get("Digite o ISBN do livro: ") 
        return self.library.loanBook(userID, bookISBN)

    def returnBook(self) -> str:
        bookISBN = self.input.get("Digite o ISBN do livro: ") 
        return self.library.returnBook(bookISBN)

    def reserveBook(self) -> str:
        userID = self.input.get("Digite o ID do usuário: ")
        try:
            userID = int(userID)
        except ValueError:
            return "ID inválido"
        bookISBN = self.input.get("Digite o ISBN do livro: ") 
        return self.library.reserveBook(userID, bookISBN)

    def showHistory(self) -> str:
        userID = self.input.get("Digite o ID do usuário: ")
        try:
            userID = int(userID)
        except ValueError:
            return "ID inválido"
        return self.library.showHistory(userID)

    def undoHistory(self) -> str:
        userID = self.input.get("Digite o ID do usuário: ")
        try:
            userID = int(userID)
        except ValueError:
            return "ID inválido"
        return self.library.undoHistory(userID)