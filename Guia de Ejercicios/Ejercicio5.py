class Arreglo(object):
    def __init__(self, initialSize):
        self.__a = [None] * initialSize
        self.__nItems = 0
    def __len__(self):  
        return self.__nItems 

    def delete(self, item):  # Borra la primera ocurrencia de un ítem
        for j in range(self.__nItems):  # Entre los ítems actuales
            if self.__a[j] == item:  # Encuentra el ítem
                self.__nItems -= 1  # Un ítem menos al final
                for k in range(j, self.__nItems):  # Mueve los ítems de la derecha
                    self.__a[k] = self.__a[k + 1]  # Mueve los elementos a la izquierda
                return True  # Retorna éxito
        return False  # No se encontró el ítem          

    def Duplicados(self):
        for i in range(self.__nItems):
           if self.__a[i]==self.__a[i+1]:
               self.delete(self.__a[i])    
         
    
    def traverse(self, function=print): 
        for j in range(self.__nItems):  
            function(self.__a[j]) 
    
    def insert(self, item):
        if self.__nItems < len(self.__a):
            self.__a[self.__nItems] = item
            self.__nItems += 1
    
     

maxSize = 10  
arr = Arreglo(maxSize)
arr.insert(10)
arr.insert(14)
arr.insert(21)
arr.insert(11)
arr.insert(31)
arr.insert(51)
arr.insert(6)
arr.insert(6)
arr.insert(6)
print("Numeros del arreglo con posibles duplicados:")
arr.traverse()
arr.Duplicados()
print("Numeros del arreglo sin duplicados:")
arr.traverse()
