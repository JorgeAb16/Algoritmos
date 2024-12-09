class Arreglo(object):
    def __init__(self, initialSize):
        self.__a = [None] * initialSize
        self.__nItems = 0
    
    def __len__(self):  
        return self.__nItems    

    def Maximo(self):
        a=0
        for i in range(self.__nItems):
            if self.__a[i] > a:
               a=self.__a[i]     
        return a
    def Minimo(self):
        a=self.__a[0]
        for i in range(self.__nItems):
            if self.__a[i] < a:
               a=self.__a[i]     
        return a
    
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
print("Maximo:\n",arr.Maximo())
print("Minimo:\n",arr.Minimo())