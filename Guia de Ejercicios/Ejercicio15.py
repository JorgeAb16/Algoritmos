class Cola:
    def __init__(self, size):
        self.__a = [None] * size
        self.__front = 0
        self.__rear = 0
        self.__size = size
        self.__count = 0

    def enqueue(self, item):
        if self.__count < self.__size:
            self.__a[self.__rear] = item
            self.__rear = (self.__rear + 1) % self.__size
            self.__count += 1
        else:
            raise OverflowError("Cola llena")

    def dequeue(self):
        if self.__count > 0:
            item = self.__a[self.__front]
            self.__a[self.__front] = None
            self.__front = (self.__front + 1) % self.__size
            self.__count -= 1
            return item
        else:
            raise IndexError("Cola vacía")

    def size(self):
        return self.__count

    def traverse(self):
        elements = []
        for i in range(self.__count):
            elements.append(self.__a[(self.__front + i) % self.__size])
        return elements

    def is_empty(self):
        return self.__count == 0

    def ordenar(self):
    
        elements = []
        while not self.is_empty():
            elements.append(self.dequeue())

      
        elements.sort()

        for element in elements:
            self.enqueue(element)


col = Cola(10)
col.enqueue(5)
col.enqueue(1)
col.enqueue(4)
col.enqueue(2)
col.enqueue(3)

print("Antes de ordenar:")
print(col.traverse())

col.ordenar()

print("Después de ordenar:")
print(col.traverse())

