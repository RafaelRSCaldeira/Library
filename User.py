class User():
    id = 1

    def __init__(self, name: str) -> None:
        self.id = User.id
        self.name = name
        self.history = list()
        User.id += 1

