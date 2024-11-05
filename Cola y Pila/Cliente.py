import Cola
import Pila
from random import *
maxSize = 100  # Tamaño máximo del array
col = Cola.Cola(maxSize)  # Crear un objeto Array
pil = Pila.Pila(maxSize)

op=input("Desea trabajar con una cola o una pila?\n1 para cola\n2 para pila\n")
op=int(op)

if op==1:
  for i in range(100):
    col.push(randint(0,300))
  print("La cola es:") 
  col.traverse()     
  sumPar=sumImpar=contPar=contImpar=promPar=promImpar=0
  for i in range(100):
    numberPop=col.pop() 
    if numberPop is not None:
        if numberPop % 2 == 0:
            sumPar+=numberPop
            contPar+=1
            promPar= sumPar/contPar
        else:
            sumImpar+=numberPop
            contImpar+=1
            promImpar = sumImpar / contImpar     

  print(f"La suma Par es {sumPar}, la cantidad de numeros pares: {contPar} y el promedio de los pares es: {promPar} ")
  print(f"La suma Impar es {sumImpar}, la cantidad de numeros impares: {contImpar} y el promedio de los impares es: {promImpar} ")
  col.traverse()
if op==2:
  for i in range(100):
    pil.push(randint(0,300))
  print("La Pila es:") 
  pil.traverse()     
  sumPar=sumImpar=contPar=contImpar=promPar=promImpar=0
  for i in range(100):
    numberPop=pil.pop() 
    if numberPop is not None:
        if numberPop % 2 == 0:
            sumPar+=numberPop
            contPar+=1
            promPar= sumPar/contPar
        else:
            sumImpar+=numberPop
            contImpar+=1
            promImpar = sumImpar / contImpar     

  print(f"La suma Par es {sumPar}, la cantidad de numeros pares: {contPar} y el promedio de los pares es: {promPar} ")
  print(f"La suma Impar es {sumImpar}, la cantidad de numeros impares: {contImpar} y el promedio de los impares es: {promImpar} ")
  pil.traverse() 


