def identidad(x):
    return x

class PriorityQueue:
    def __init__(self, tamano, prioridad=identidad):
        self.__maxSize = tamano
        self.__que = []
        self.__prioridad = prioridad

    def insert(self, item):
        if self.isFull():
            raise Exception("Desbordamiento de la cola")
        self.__que.append(item)
        return True

    def remove(self):
        if self.isEmpty():
            raise Exception("Subdesbordamiento de la cola")
        indice_mayor_prioridad = 0
        for i in range(1, len(self.__que)):
            if self.__prioridad(self.__que[i]) > self.__prioridad(self.__que[indice_mayor_prioridad]):
                indice_mayor_prioridad = i
        item_mayor_prioridad = self.__que.pop(indice_mayor_prioridad)
        return item_mayor_prioridad

    def peek(self):
        if self.isEmpty():
            return None
        indice_mayor_prioridad = 0
        for i in range(1, len(self.__que)):
            if self.__prioridad(self.__que[i]) > self.__prioridad(self.__que[indice_mayor_prioridad]):
                indice_mayor_prioridad = i
        return self.__que[indice_mayor_prioridad]

    def isEmpty(self):
        return len(self.__que) == 0

    def isFull(self):
        return len(self.__que) == self.__maxSize

    def __len__(self):
        return len(self.__que)

    def __str__(self):
        return "[" + ", ".join(str(item) for item in self.__que) + "]"


if __name__ == "__main__":
    pq = PriorityQueue(5, prioridad=lambda x: x)

    print("Insertando elementos (fuera de orden de prioridad):")
    pq.insert(3)
    pq.insert(5)
    pq.insert(1)
    pq.insert(4)
    pq.insert(2)
    print("Contenido de la cola:", pq)

    print("\nElemento de mayor prioridad (peek):", pq.peek())
    print("Removiendo el elemento de mayor prioridad:", pq.remove())
    print("Contenido de la cola después de remover:", pq)

    print("\nInsertando un elemento con baja prioridad (0):")
    pq.insert(0)
    print("Contenido de la cola:", pq)

    print("\nInsertando un elemento con alta prioridad (6):")
    pq.insert(6)
    print("Contenido de la cola:", pq)

    print("\nElemento de mayor prioridad (peek):", pq.peek())
    print("Removiendo el elemento de mayor prioridad:", pq.remove())
    print("Contenido de la cola después de remover:", pq)

    print("\n¿La cola está vacía?", pq.isEmpty())
    print("¿La cola está llena?", pq.isFull())

    print("\nRemoviendo todos los elementos en orden de prioridad:")
    while not pq.isEmpty():
        print("Removiendo:", pq.remove())
        print("Contenido de la cola:", pq)

    print("¿La cola está vacía después de todas las eliminaciones?", pq.isEmpty())
