from Rectangulo import *
rectangulo1 = Rectangulo(4,4)
rectangulo = Rectangulo(4,5)

print("Area del rectangulo 1", rectangulo1.getArea())
print("Area del rectangulo 2", rectangulo.getArea())
print("Perimetro del rectangulo 1", rectangulo1.getPerimetro())
print("Perimetro del rectangulo 2", rectangulo.getPerimetro())
print("Rectangulo 1", rectangulo1.escuadrado())
print("Rectangulo 2", rectangulo.escuadrado())

if rectangulo.largorectangulo()>rectangulo1.largorectangulo():
    print("Rectangulo 2 es mas largo que rectangulo 1")
elif rectangulo.largorectangulo()<rectangulo1.largorectangulo():
    print("Rectangulo 1 es mas largo que rectangulo 2")
else:
    print("Los dos son igual de largos >:(")        