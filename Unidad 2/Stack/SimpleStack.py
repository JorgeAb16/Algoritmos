class Stack(object):
    def __init__(self, max):  # Constructor
        self.__stackList = [None] * max  # La pila almacenada como una lista
        self.__top = -1  # Sin elementos inicialmente

    def push(self, item):  # Insertar un elemento en la parte superior de la pila
        if self.isFull():
            raise IndexError("Push en pila llena")  # Lanzar excepción si la pila está llena
        self.__top += 1  # Avanzar el puntero
        self.__stackList[self.__top] = item  # Almacenar el elemento

    def pop(self):  # Eliminar el elemento superior de la pila
        if self.isEmpty():
            raise IndexError("Pop en pila vacía")  # Lanzar excepción si la pila está vacía
        top = self.__stackList[self.__top]  # Elemento en la parte superior
        self.__stackList[self.__top] = None  # Eliminar referencia al elemento
        self.__top -= 1  # Reducir el puntero
        return top  # Retornar el elemento superior

    def peek(self):  # Retornar el elemento superior sin eliminarlo
        if not self.isEmpty():  # Si la pila no está vacía
            return self.__stackList[self.__top]  # Retornar el elemento superior

    def isEmpty(self):  # Verificar si la pila está vacía
        return self.__top < 0

    def isFull(self):  # Verificar si la pila está llena
        return self.__top >= len(self.__stackList) - 1

    def __len__(self):  # Retornar el número de elementos en la pila
        return self.__top + 1

    def __str__(self):  # Convertir la pila a una cadena
        ans = "["  # Empezar con un corchete izquierdo
        for i in range(self.__top + 1):  # Recorrer los elementos actuales
            if len(ans) > 1:  # Excepto al lado del corchete izquierdo,
                ans += ", "  # separar elementos con coma
            ans += str(self.__stackList[i])  # Añadir el elemento como cadena
        ans += "]"  # Cerrar con corchete derecho
        return ans



