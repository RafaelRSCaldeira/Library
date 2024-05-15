from Input import *

class Interface():
    def __init__(self, inputType="terminal"):
        self.input = InputFactory.create(inputType)
    
    def showMenu(self):
        '''Opções:\n\
            (1) Adicionar usuário\n\
            (2) Adicionar livro\n\
            (3) Empréstimo de livro\n\
            (4) Devolução de livro\n\
            (5) Reserva de livro\n\
            (6) Revisar histórico de operações\n\
            (7) Desfazer operação'''
