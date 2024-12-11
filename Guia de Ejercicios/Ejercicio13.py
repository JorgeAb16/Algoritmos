class ColaCircular:
    def __init__(self, size):
        self.__a = [None] * size  
        self.__size = size  
        self.__front = 0  
        self.__rear = -1  
        self.__count = 0  
        
    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("La cola está llena")
        self.__rear = (self.__rear + 1) % self.__size  
        self.__a[self.__rear] = item
        self.__count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("La cola está vacía")
        item = self.__a[self.__front]
        self.__a[self.__front] = None  
        self.__front = (self.__front + 1) % self.__size  
        self.__count -= 1
        return item

    def is_empty(self):
        return self.__count == 0

    def is_full(self):
        return self.__count == self.__size

    def peek(self):
        if self.is_empty():
            return None
        return self.__a[self.__front]

    def size(self):
        return self.__count

    def traverse(self):
        print("Elementos en la cola:")
        index = self.__front
        for _ in range(self.__count):
            print(self.__a[index], end=" ")
            index = (index + 1) % self.__size
        print()

cola = ColaCircular(5)


cola.enqueue(10)
cola.enqueue(20)
cola.enqueue(30)
cola.traverse() 


print("Dequeue:", cola.dequeue())  
cola.traverse()  

cola.enqueue(40)
cola.enqueue(50)
cola.enqueue(60)
cola.traverse()  

print("Is full:", cola.is_full())  


print("Dequeue:", cola.dequeue())  
print("Dequeue:", cola.dequeue())  
cola.traverse()  
