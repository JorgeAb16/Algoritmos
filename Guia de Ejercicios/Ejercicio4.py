class Arreglo(object):
    def __init__(self, initialSize):
        self.__a = [None] * initialSize
        self.__nItems = 0
    def __len__(self):  
        return self.__nItems    

    def Buscar(self,a):
        x=0
        for i in range(self.__nItems):
           if a==self.__a[i]:
               x=1
               print("El elemento se encuentra en la posicion ",i+1)
        if x==0:
            print("El elemento no se encuentra en el arreglo")               
    
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
print("Numeros del arreglo:")
arr.traverse()
arr.Buscar(60)