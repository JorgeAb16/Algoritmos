class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Recorrido preorden: Raíz, Izquierda, Derecha
    def preorden(self):
        resultado = self.value
        if self.left:
            resultado += self.left.preorden()
        if self.right:
            resultado += self.right.preorden()
        return resultado

    # Recorrido inorden con paréntesis para claridad
    def inorden(self):
        if self.left and self.right:
            return f"({self.left.inorden()} {self.value} {self.right.inorden()})"
        return self.value

    # Recorrido posorden: Izquierda, Derecha, Raíz
    def posorden(self):
        resultado = ""
        if self.left:
            resultado += self.left.posorden()
        if self.right:
            resultado += self.right.posorden()
        resultado += self.value
        return resultado


class ExpressionTree:
    def __init__(self):
        self.operadores = {'+', '-', '*', '/'}

    def construir_arbol(self, expresion):
        pila = []
        tokens = expresion.split()

        for token in tokens:
            if token.isalnum() or token.isdigit():  # Operando: nodo hoja
                pila.append(BinaryTree(token))
            elif token in self.operadores:  # Operador: combinar los últimos dos árboles
                if len(pila) < 2:
                    raise Exception("Expresión no válida: faltan operandos para el operador")
                derecho = pila.pop()
                izquierdo = pila.pop()
                nodo = BinaryTree(token)
                nodo.left = izquierdo
                nodo.right = derecho
                pila.append(nodo)
            else:
                raise Exception(f"Token no válido: {token}")

        if len(pila) != 1:
            raise Exception("Expresión no válida: operandos o operadores adicionales")
        return pila[0]


def main():
    expresiones = [
        "91 95 + 15 + 19 + 4 *",
        "B B * A C 4 * * -",
        "42",
        "A 57",     # Inválida: falta operador
        "+ /",      # Inválida: solo operadores
    ]

    constructor = ExpressionTree()

    for expr in expresiones:
        print(f"\nExpresión: {expr}")
        try:
            arbol = constructor.construir_arbol(expr)
            print("Preorden:", arbol.preorden())
            print("Inorden:", arbol.inorden())
            print("Posorden:", arbol.posorden())
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
