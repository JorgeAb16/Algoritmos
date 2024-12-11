class Pila:
    def __init__(self):
        self.__a = []  # Usamos una lista dinámica para simular la pila

    def push(self, item):
        self.__a.append(item)  # Agrega un elemento a la pila

    def pop(self):
        if not self.is_empty():
            return self.__a.pop()  # Elimina y retorna el elemento superior
        else:
            raise IndexError("No hay más páginas en el historial para retroceder.")

    def top(self):
        if not self.is_empty():
            return self.__a[-1]  # Retorna el elemento superior sin eliminarlo
        else:
            return None

    def is_empty(self):
        return len(self.__a) == 0

class HistorialNavegacion:
    def __init__(self):
        self.historial = Pila()  # Pila para el historial de navegación
        self.pagina_actual = None  # Página actual

    def visitar_pagina(self, url):
        if self.pagina_actual:
            self.historial.push(self.pagina_actual)  # Guarda la página actual en el historial
        self.pagina_actual = url  # Actualiza la página actual
        print(f"Visita: {url}")

    def ir_atras(self):
        if not self.historial.is_empty():
            self.pagina_actual = self.historial.pop()  # Recupera la última página visitada
            print(f"Retrocede a: {self.pagina_actual}")
        else:
            print("No hay más páginas en el historial.")

    def mostrar_pagina_actual(self):
        if self.pagina_actual:
            print(f"Página actual: {self.pagina_actual}")
        else:
            print("No hay ninguna página cargada actualmente.")

# Prueba del historial de navegación
navegador = HistorialNavegacion()

# Navegar a varias páginas
navegador.visitar_pagina("https://www.google.com")
navegador.visitar_pagina("https://www.youtube.com")
navegador.visitar_pagina("https://www.github.com")

# Mostrar la página actual
navegador.mostrar_pagina_actual()

# Retroceder en el historial
navegador.ir_atras()
navegador.mostrar_pagina_actual()
navegador.ir_atras()
navegador.mostrar_pagina_actual()

# Intentar retroceder más allá del historial
navegador.ir_atras()
