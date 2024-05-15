class Queue():
    def __init__(self) -> None:
        self.queue = list()
    
    def enqueue(self, item) -> None:
        self.queue.append(item)
    
    def dequeue(self):
        return self.queue.pop(0)

    def isEmpty(self) -> bool:
        return len(self.queue) == 0

    def insert(self, item, index: int) -> None:
        self.queue.insert(item, index)
    
    def remove(self, item) -> None:
        self.queue.remove(item)