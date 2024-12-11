class Pila:
    def __init__(self, size):
        self.__a = [None] * size
        self.__Nitems = 0

    def __len__(self):
        return self.__Nitems

    def push(self, item):
        if self.__Nitems < len(self.__a):
            self.__a[self.__Nitems] = item
            self.__Nitems += 1
        else:
            raise OverflowError("La pila está llena")

    def pop(self):
        if self.__Nitems > 0:
            item = self.__a[self.__Nitems - 1]
            self.__a[self.__Nitems - 1] = None
            self.__Nitems -= 1
            return item
        else:
            raise IndexError("La pila está vacía")

    def top(self):
        if self.__Nitems > 0:
            return self.__a[self.__Nitems - 1]
        else:
            raise IndexError("La pila está vacía")

# Calculadora basada en pila
def calculadora_pila(entrada):
    pila = Pila(len(entrada))
    for item in entrada:
        if isinstance(item, (int, float)):  # Si el elemento es un número, se apila
            pila.push(item)
        elif item in ['+', '-', '*', '/']:  # Si es un operador, realiza la operación
            if len(pila) < 2:
                raise ValueError("No hay suficientes operandos en la pila para realizar la operación")
            b = pila.pop()
            a = pila.pop()
            if item == '+':
                pila.push(a + b)
            elif item == '-':
                pila.push(a - b)
            elif item == '*':
                pila.push(a * b)
            elif item == '/':
                if b == 0:
                    raise ZeroDivisionError("División entre cero no permitida")
                pila.push(a / b)
        else:
            raise ValueError(f"Elemento no reconocido: {item}")

    # Al final, debería quedar un solo resultado en la pila
    if len(pila) != 1:
        raise ValueError("La entrada no es válida, hay elementos sobrantes en la pila")
    return pila.pop()

# Prueba de la calculadora
entrada = [5, 3, '+', 2, '*', 4, '/']  # (5 + 3) * 2 / 4 = 4.0
resultado = calculadora_pila(entrada)
print(f"Resultado: {resultado}")
