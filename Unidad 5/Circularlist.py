class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularList:
    def __init__(self):
        self.last = None

    def isEmpty(self):
        return self.last is None

    def insertEnd(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.last = new_node
            self.last.next = self.last
        else:
            new_node.next = self.last.next
            self.last.next = new_node
            self.last = new_node

    def insertFront(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.last = new_node
            self.last.next = self.last
        else:
            new_node.next = self.last.next
            self.last.next = new_node

    def removeFront(self):
        if self.isEmpty():
            raise IndexError("Circular list is empty, cannot remove element.")
        data = self.last.next.data
        if self.last.next == self.last:
            self.last = None
        else:
            self.last.next = self.last.next.next
        return data

    def peekFront(self):
        if self.isEmpty():
            raise IndexError("Circular list is empty, cannot peek element.")
        return self.last.next.data

class Stack:
    def __init__(self):
        self.circular_list = CircularList()

    def isEmpty(self):
        return self.circular_list.isEmpty()

    def push(self, data):
        self.circular_list.insertFront(data)

    def pop(self):
        return self.circular_list.removeFront()

    def peek(self):
        return self.circular_list.peekFront()
class Queue:
    def __init__(self):
        self.circular_list = CircularList()

    def isEmpty(self):
        return self.circular_list.isEmpty()

    def insert(self, data):
        self.circular_list.insertEnd(data)

    def remove(self):
        return self.circular_list.removeFront()

    def peek(self):
        return self.circular_list.peekFront()
# Uso de la pila (Stack)
stack = Stack()
stack.push(10)
stack.push(20)
print(stack.peek())  # Output: 20
print(stack.pop())   # Output: 20
print(stack.pop())   # Output: 10
print(stack.isEmpty())  # Output: True

# Uso de la cola (Queue)
queue = Queue()
queue.insert(10)
queue.insert(20)
print(queue.peek())  # Output: 10
print(queue.remove()) # Output: 10
print(queue.remove()) # Output: 20
print(queue.isEmpty())  # Output: True
