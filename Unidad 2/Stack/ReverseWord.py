from SimpleStack import Stack
import string

def is_palindrome(phrase):
    # Crear una pila para almacenar las letras de la frase
    stack = Stack(100)
    
    # Filtrar la frase para eliminar espacios, puntuación y dígitos, y convertir a minúsculas
    filtered_phrase = ''.join(char.lower() for char in phrase if char.isalpha())
    
    # Insertar cada letra en la pila
    for letter in filtered_phrase:
        stack.push(letter)
    
    # Construir la versión inversa de la frase usando la pila
    reversed_phrase = ''
    while not stack.isEmpty():
        reversed_phrase += stack.pop()
    
    # Verificar si la frase filtrada es igual a su reverso
    return filtered_phrase == reversed_phrase

# Probar el programa con una frase conocida
input_phrase = "A man, a plan, a canal, Panama"
if is_palindrome(input_phrase):
    print(f'"{input_phrase}" es un palíndromo.')
else:
    print(f'"{input_phrase}" no es un palíndromo.')

