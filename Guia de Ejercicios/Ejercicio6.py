class Arreglo():
    def __init__(self,Initialsize):
        self.__a=[None] * Initialsize
        self.__nItems=0
    
    def __len__(self):
        return self.__nItems
    
    def push(self,item):
        self.__a[self.__nItems]=item
        self.__nItems+=1
    
    def pop(self):
        item = self.__a[self.__nItems-1]
        self.__a[self.__nItems-1]= None 
        self.__nItems -= 1     
        return item
     
    def peek(self):
        return self.__a[self.__nItems-1]
    
    def traverse(self):
        for i in range(self.__nItems):
            print (self.__a[i])


MaxSize=10
arr = Arreglo(MaxSize)
arr.push(10)
arr.push(15)
arr.push(20)
arr.push(25)
arr.push(30)
arr.push(35)
print("Numeros del arreglo:")
arr.traverse()
print("Arreglo luego de usar pop:")
arr.pop()
arr.traverse()
print("Uso del peek:")
print(arr.peek())