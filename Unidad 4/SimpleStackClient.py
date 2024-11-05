from SimpleStack import Stack

# Crear una pila con un tamaño máximo de 10
stack = Stack(10)

# Insertar palabras en la pila
for word in ['May', 'the', 'force', 'be', 'with', 'you']:
    stack.push(word)

# Mostrar el contenido de la pila después de insertar palabras
print('After pushing', len(stack), 'words on the stack, it contains:\n', stack)
print('Is stack full?', stack.isFull())

# Intentar hacer push adicional para verificar la excepción de pila llena
try:
    for extra_word in ['always', 'believe', 'in', 'yourself', 'young', 'padawan']:
        stack.push(extra_word)
except IndexError as e:
    print("Exception caught while pushing:", e)

# Eliminar elementos de la pila hasta que esté vacía
print('Popping items off the stack:')
while not stack.isEmpty():
    print(stack.pop(), end=' ')
print()

# Intentar hacer pop en la pila vacía para verificar la excepción
try:
    stack.pop()
except IndexError as e:
    print("Exception caught while popping:", e)

