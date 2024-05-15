from Queue import Queue

class Book():
    def __init__(self, ISBN: str, title: str, author: str) -> None:
        self.ISBN = ISBN
        self.title = title
        self.author = author
        self.usersQueue = Queue()



