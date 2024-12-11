class Nodo:
    def __init__(self, valor):
        self.valor = valor  # El valor del nodo
        self.siguiente = None  # Apuntador al siguiente nodo

class ListaEnlazada:
    def __init__(self):
        self.head = None  # La lista comienza vacía, por lo tanto, no hay nodos

    def agregar_al_final(self, valor):
        # Crear un nuevo nodo
        nuevo_nodo = Nodo(valor)
        if self.head is None:
            # Si la lista está vacía, el nuevo nodo es el primer nodo
            self.head = nuevo_nodo
        else:
            # Si la lista no está vacía, recorrerla hasta el último nodo
            actual = self.head
            while actual.siguiente:
                actual = actual.siguiente
            # Asignar el nuevo nodo al final de la lista
            actual.siguiente = nuevo_nodo

    def eliminar(self, valor):
        # Eliminar el primer nodo que contenga el valor dado
        if self.head is None:
            print("La lista está vacía")
            return
        if self.head.valor == valor:
            # Si el valor a eliminar está en el primer nodo
            self.head = self.head.siguiente
            return
        actual = self.head
        while actual.siguiente:
            if actual.siguiente.valor == valor:
                actual.siguiente = actual.siguiente.siguiente  # Eliminar el nodo
                return
            actual = actual.siguiente
        print(f"El valor {valor} no se encuentra en la lista.")

    def buscar(self, valor):
        # Buscar si un valor está presente en la lista
        actual = self.head
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False

    def imprimir(self):
        # Imprimir todos los elementos de la lista
        actual = self.head
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

# Ejemplo de uso:
lista = ListaEnlazada()

# Agregar elementos al final
lista.agregar_al_final(10)
lista.agregar_al_final(20)
lista.agregar_al_final(30)
lista.agregar_al_final(40)

print("Lista después de agregar elementos:")
lista.imprimir()

# Buscar un elemento
print("¿Existe el valor 20 en la lista?", lista.buscar(20))  # True
print("¿Existe el valor 50 en la lista?", lista.buscar(50))  # False

# Eliminar un elemento
lista.eliminar(20)
print("Lista después de eliminar el valor 20:")
lista.imprimir()

# Eliminar un elemento no presente
lista.eliminar(50)
