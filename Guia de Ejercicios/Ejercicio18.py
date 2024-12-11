class Nodo:
    def __init__(self, valor):
        self.valor = valor  
        self.siguiente = None  

class ListaEnlazada:
    def __init__(self):
        self.head = None  

    def agregar_al_final(self, valor):
       
        nuevo_nodo = Nodo(valor)
        if self.head is None:
           
            self.head = nuevo_nodo
        else:
           
            actual = self.head
            while actual.siguiente:
                actual = actual.siguiente
           
            actual.siguiente = nuevo_nodo

    def eliminar(self, valor):
        
        if self.head is None:
            print("La lista está vacía")
            return
        if self.head.valor == valor:
           
            self.head = self.head.siguiente
            return
        actual = self.head
        while actual.siguiente:
            if actual.siguiente.valor == valor:
                actual.siguiente = actual.siguiente.siguiente  
                return
            actual = actual.siguiente
        print(f"El valor {valor} no se encuentra en la lista.")

    def buscar(self, valor):
       
        actual = self.head
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False

    def imprimir(self):
     
        actual = self.head
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

    def invertir(self):
        # Método para invertir el orden de los nodos
        anterior = None
        actual = self.head
        while actual:
            siguiente = actual.siguiente  # Guardamos el siguiente nodo
            actual.siguiente = anterior  # Invertimos el puntero
            anterior = actual  # Avanzamos uno paso
            actual = siguiente  # Avanzamos al siguiente nodo
        self.head = anterior  # La nueva cabeza será el nodo que antes era el último
    def eliminar_duplicados(self):
        # Método para eliminar nodos con valores duplicados
        if self.head is None:
            print("La lista está vacía")
            return
        
        valores_vistos = set()  # Conjunto para almacenar los valores únicos
        actual = self.head
        anterior = None

        while actual:
            if actual.valor in valores_vistos:
                # Si el valor ya fue visto, eliminar el nodo actual
                anterior.siguiente = actual.siguiente
            else:
                # Si el valor no fue visto, agregarlo al conjunto y continuar
                valores_vistos.add(actual.valor)
                anterior = actual
            actual = actual.siguiente

lista = ListaEnlazada()

lista.agregar_al_final(10)
lista.agregar_al_final(20)
lista.agregar_al_final(30)
lista.agregar_al_final(40)
lista.agregar_al_final(40)
print("Lista después de agregar elementos:")
lista.imprimir()
print("Lista después de eliminar duplicados:")
lista.eliminar_duplicados()
lista.imprimir()