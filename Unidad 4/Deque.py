class Deque:
    def __init__(self, max_size):
        self.max_size = max_size
        self.deque = [None] * max_size
        self.front = -1
        self.rear = 0
        self.size = 0

    def insertLeft(self, item):
        if self.isFull():
            raise OverflowError("Deque llena")
        self.front = (self.front - 1) % self.max_size
        self.deque[self.front] = item
        self.size += 1

    def insertRight(self, item):
        if self.isFull():
            raise OverflowError("Deque llena")
        self.deque[self.rear] = item
        self.rear = (self.rear + 1) % self.max_size
        self.size += 1

    def removeLeft(self):
        if self.isEmpty():
            raise IndexError("Deque vacia")
        item = self.deque[self.front]
        self.deque[self.front] = None
        self.front = (self.front + 1) % self.max_size
        self.size -= 1
        return item

    def removeRight(self):
        if self.isEmpty():
            raise IndexError("Deque vacia")
        self.rear = (self.rear - 1) % self.max_size
        item = self.deque[self.rear]
        self.deque[self.rear] = None
        self.size -= 1
        return item

    def peekLeft(self):
        if self.isEmpty():
            raise IndexError("Deque vacia")
        return self.deque[self.front]

    def peekRight(self):
        if self.isEmpty():
            raise IndexError("Deque vacia")
        return self.deque[(self.rear - 1) % self.max_size]

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.max_size

    def __str__(self):
        return str(self.deque)
