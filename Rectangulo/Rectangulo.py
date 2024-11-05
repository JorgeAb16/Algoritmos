class Rectangulo():
    def __init__(self,largo,ancho): 
        self._ancho = ancho
        self._largo = largo
    def getArea(self):  
            return self._ancho*self._largo
    def getPerimetro(self):  
            return self._ancho*2+self._largo*2
    def escuadrado(self):
        if self._ancho == self._largo:
            return ("Esto es un cuadrado >:(")
        if self._ancho != self._largo:
            return ("Es un rectangulo :)")
    def largorectangulo(self):
        return self._largo   
        