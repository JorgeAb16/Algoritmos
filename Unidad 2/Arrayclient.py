import Array

maxSize = 10  # Tamaño máximo del array
arr = Array.Array(maxSize)  # Crear un objeto Array

# Insertar algunos elementos
arr.insert(77)
arr.insert(99)
arr.insert("foo")
arr.insert("bar")
arr.insert(44)
arr.insert(55)
arr.insert(12.34)
arr.insert(0)
arr.insert("foo")  # Duplicado
arr.insert("bar")  # Duplicado

# Imprimir el array original
print("Array containing", len(arr), "items:")
arr.traverse()

# Buscar algunos elementos
print("Search for 12 returns:", arr.search(12))
print("Search for 12.34 returns:", arr.search(12.34))

# Eliminar algunos elementos
print("Deleting 0 returns:", arr.delete(0))
print("Deleting 17 returns:", arr.delete(17))

# Modificar un elemento
print("Setting item at index 3 to 33")
arr.set(3, 33)

# Imprimir el estado del array después de las operaciones
print("Array after deletions has", len(arr), "items:")
arr.traverse()

# Obtener y eliminar el número máximo
max_num = arr.getMaxNum()
if max_num is not None:
    arr.delete(max_num)  # Eliminar el número máximo
    print(f"Número máximo ({max_num}) eliminado del array.")
else:
    print("No hay números en el array para eliminar.")

# Mostrar el array después de la eliminación del número máximo
print("Array sin el número máximo:")
arr.traverse()

# Obtener el nuevo número máximo
max_num = arr.getMaxNum()
print(f"Número máximo actual del array: {max_num}")

sorted_numbers = []

# Ordenar el array eliminando el máximo repetidamente


# Imprimir el array ordenado
print("Array ordenado por valor numérico (de mayor a menor):")
print(sorted_numbers)

# Imprimir el estado final del array
print("Estado final del array:")
arr.traverse()

print("Array original con posibles duplicados:")
arr.traverse()

# Eliminar duplicados
arr.removeDupes()

# Imprimir el array después de eliminar duplicados
print("Array después de eliminar duplicados:")
arr.traverse()

print("promedio es : ", arr.prom())
print("pares e impares son : ","(", arr.cuenta(1),",",arr.cuenta(0),")" )
print("lista solo letras : ", arr.letras())

