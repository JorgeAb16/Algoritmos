class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front is None

    def insertLeft(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node

    def insertRight(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node

    def removeLeft(self):
        if self.isEmpty():
            raise IndexError("Deque is empty, cannot remove from left.")
        data = self.front.data
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None
        return data

    def removeRight(self):
        if self.isEmpty():
            raise IndexError("Deque is empty, cannot remove from right.")
        data = self.rear.data
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        return data

    def peekLeft(self):
        if self.isEmpty():
            raise IndexError("Deque is empty, cannot peek left.")
        return self.front.data

    def peekRight(self):
        if self.isEmpty():
            raise IndexError("Deque is empty, cannot peek right.")
        return self.rear.data
dq = Deque()
dq.insertLeft(10)
dq.insertRight(20)
dq.insertLeft(5)

print(dq.peekLeft())   # Output: 5
print(dq.peekRight())  # Output: 20

print(dq.removeLeft()) # Output: 5
print(dq.removeRight()) # Output: 20
print(dq.isEmpty())     # Output: False (still has 10)

print(dq.removeLeft())  # Output: 10
print(dq.isEmpty())     # Output: True
