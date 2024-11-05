def key_function(x):  # Función clave por defecto
    return x

class OrderedRecordArray(object):
    def __init__(self, initialSize, key=key_function):  # Constructor
        self.__a = [None] * initialSize  # El array almacenado como una lista
        self.__nItems = 0  # No hay elementos en el array inicialmente
        self.__key = key  # La función clave para obtener la clave del registro

    def __len__(self):  # Función especial para len()
        return self.__nItems  # Retorna el número de elementos

    def get(self, n):  # Devuelve el valor en el índice n
        if n >= 0 and n < self.__nItems:  # Verifica si n está en los límites
            return self.__a[n]  # Solo devuelve el ítem si está en los límites
        raise IndexError("Índice " + str(n) + " está fuera de rango")

    def traverse(self, function=print):  # Recorre todos los ítems y aplica una función
        for j in range(self.__nItems):  # Entre los ítems actuales
            function(self.__a[j])

    def __str__(self):  # Función especial para str()
        ans = "["  # Envolver con corchetes
        for i in range(self.__nItems):  # Recorre los elementos
            if len(ans) > 1:  # Excepto junto al corchete izquierdo,
                ans += ", "  # Separar ítems con coma
            ans += str(self.__a[i])  # Agrega la forma en string del ítem
        ans += "]"  # Cierra con corchete derecho
        return ans

    def find(self, key):  # Busca el índice para la clave o punto de inserción
        lo = 0
        hi = self.__nItems - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if self.__key(self.__a[mid]) == key:
                return mid  # Devuelve la ubicación si lo encuentra
            elif self.__key(self.__a[mid]) < key:
                lo = mid + 1  # Elevar el límite inferior
            else:
                hi = mid - 1  # Bajar el límite superior
        return lo  # Si no se encuentra, devuelve el punto de inserción

    def search(self, key):  # Busca un registro por su clave
        idx = self.find(key)
        if idx < self.__nItems and self.__key(self.__a[idx]) == key:
            return self.__a[idx]  # Devuelve el ítem si lo encuentra

    def insert(self, item):  # Inserta un ítem en la posición correcta
        if self.__nItems >= len(self.__a):  # Si el array está lleno,
            raise Exception("Desbordamiento de array")  # Levanta una excepción
        j = self.find(self.__key(item))  # Encuentra dónde debe ir el ítem
        for k in range(self.__nItems, j, -1):  # Mueve los elementos más grandes a la derecha
            self.__a[k] = self.__a[k - 1]
        self.__a[j] = item  # Inserta el ítem
        self.__nItems += 1  # Incrementa el número de elementos

    def delete(self, item):  # Elimina todas las ocurrencias de un ítem con clave duplicada
        j = self.find(self.__key(item))  # Encuentra la posición donde debería estar el ítem
        deleted = False  # Bandera para indicar si se eliminó algún ítem

        # Recorre hacia adelante para eliminar todas las ocurrencias del ítem
        while j < self.__nItems and self.__key(self.__a[j]) == self.__key(item):
            self.__nItems -= 1  # Reduce el tamaño del array
            for k in range(j, self.__nItems):  # Mueve los elementos restantes a la izquierda
                self.__a[k] = self.__a[k + 1]
            deleted = True  # Se ha eliminado al menos una ocurrencia

        return deleted  # Devuelve True si se eliminó al menos un ítem, False en caso contrario

    def merge(self, other):  # Método para fusionar dos arrays ordenados
        if self.__key != other.__key:
            raise ValueError("Las funciones clave no coinciden, no se puede realizar la fusión")

        merged_size = self.__nItems + other.__nItems
        merged_array = [None] * merged_size

        i = j = k = 0

        # Comparar y fusionar los elementos
        while i < self.__nItems and j < other.__nItems:
            if self.__key(self.__a[i]) <= self.__key(other.__a[j]):
                merged_array[k] = self.__a[i]
                i += 1
            else:
                merged_array[k] = other.__a[j]
                j += 1
            k += 1

        # Copiar los elementos restantes, si los hay
        while i < self.__nItems:
            merged_array[k] = self.__a[i]
            i += 1
            k += 1

        while j < other.__nItems:
            merged_array[k] = other.__a[j]
            j += 1
            k += 1

        # Asignar el array fusionado al objeto actual
        self.__a = merged_array
        self.__nItems = merged_size


# Pruebas para verificar el funcionamiento
if __name__ == "__main__":
    # Crear un array ordenado
    arr = OrderedRecordArray(20)

    # Insertar elementos, incluyendo duplicados
    arr.insert(10)
    arr.insert(20)
    arr.insert(20)
    arr.insert(30)
    arr.insert(20)
    arr.insert(40)

    # Imprimir el array original
    print("Array original con duplicados:")
    arr.traverse()

    # Eliminar todos los ítems con valor 20
    arr.delete(20)

    # Imprimir el array después de eliminar los duplicados
    print("\nArray después de eliminar el 20:")
    arr.traverse()

    # Intentar eliminar un ítem que no existe
    result = arr.delete(50)
    print("\nResultado de eliminar 50:", result)

    # Crear otro array para la fusión
    arr2 = OrderedRecordArray(20)
    arr2.insert(15)
    arr2.insert(25)
    arr2.insert(35)

    # Fusionar arr2 con arr
    arr.merge(arr2)

    # Imprimir el array después de la fusión
    print("\nArray después de la fusión con arr2:")
    arr.traverse()
