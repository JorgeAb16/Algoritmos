class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def merge_sorted_lists(list1, list2):
  
    dummy = ListNode()
    current = dummy

   
    while list1 and list2:
        if list1.value < list2.value:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

   
    if list1:
        current.next = list1
    if list2:
        current.next = list2

    
    return dummy.next


def print_list(head):
    while head:
        print(head.value, end=" -> ")
        head = head.next
    print("None")


list1 = ListNode(1, ListNode(3, ListNode(5)))
list2 = ListNode(2, ListNode(4, ListNode(6)))


merged_list = merge_sorted_lists(list1, list2)


print_list(merged_list)

class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = NodoArbol(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierdo is None:
                nodo.izquierdo = NodoArbol(valor)
            else:
                self._insertar_recursivo(nodo.izquierdo, valor)
        else:
            if nodo.derecho is None:
                nodo.derecho = NodoArbol(valor)
            else:
                self._insertar_recursivo(nodo.derecho, valor)

    def inorder(self):
        resultado = []
        self._inorder_recursivo(self.raiz, resultado)
        return resultado

    def _inorder_recursivo(self, nodo, resultado):
        if nodo is not None:
            self._inorder_recursivo(nodo.izquierdo, resultado)
            resultado.append(nodo.valor)
            self._inorder_recursivo(nodo.derecho, resultado)

    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, nodo, valor):
        if nodo is None:
            return False
        if nodo.valor == valor:
            return True
        elif valor < nodo.valor:
            return self._buscar_recursivo(nodo.izquierdo, valor)
        else:
            return self._buscar_recursivo(nodo.derecho, valor)

    def altura(self):
        return self._altura_recursiva(self.raiz)

    def _altura_recursiva(self, nodo):
        if nodo is None:
            return 0
        izquierdo_altura = self._altura_recursiva(nodo.izquierdo)
        derecho_altura = self._altura_recursiva(nodo.derecho)
        return 1 + max(izquierdo_altura, derecho_altura)

    def recorrido_por_niveles(self):
        if not self.raiz:
            return []

        resultado = []
        cola = [self.raiz]

        while cola:
            nodo_actual = cola.pop(0)
            resultado.append(nodo_actual.valor)

            if nodo_actual.izquierdo:
                cola.append(nodo_actual.izquierdo)
            if nodo_actual.derecho:
                cola.append(nodo_actual.derecho)

        return resultado

    def contar_hojas(self):
        return self._contar_hojas_recursivo(self.raiz)

    def _contar_hojas_recursivo(self, nodo):
        if nodo is None:
            return 0
        if nodo.izquierdo is None and nodo.derecho is None:
            return 1
        return self._contar_hojas_recursivo(nodo.izquierdo) + self._contar_hojas_recursivo(nodo.derecho)


arbol = ArbolBinario()
arbol.insertar(5)
arbol.insertar(3)
arbol.insertar(7)
arbol.insertar(2)
arbol.insertar(4)

print("Recorrido inorder:", arbol.inorder())
print("Buscar 4:", arbol.buscar(4))
print("Buscar 6:", arbol.buscar(6))
print("Altura del árbol:", arbol.altura())
print("Recorrido por niveles:", arbol.recorrido_por_niveles())
print("Número de nodos hoja:", arbol.contar_hojas())
