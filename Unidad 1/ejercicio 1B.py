import random
cartas = {
    1: 'A',
    11: 'J',
    12: 'Q',
    13: 'K'
}
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
random.shuffle(lista)
listapro = [cartas.get(carta, carta) for carta in lista]
print(listapro)

var=0
for i in range(len(lista)):
     for j in range(len(lista)-i-1):
          if lista[j]>lista[j+1]:
               var=lista[j+1]
               lista[j+1]=lista[j]       
               lista[j]=var

listapro = [cartas.get(carta, carta) for carta in lista]
print(listapro)
