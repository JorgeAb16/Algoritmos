class cola():
    def __init__(self,Initialsize):
        self.__a = [None]*Initialsize
        self.__Nitems=0

    def enqueue(self,item):
        self.__a [self.__Nitems]=item
        self.__Nitems+=1

    def dequeue(self):
        item= self.__a [0]
        for i in range(1, self.__Nitems):
            self.__a[i - 1] = self.__a[i]
        self.__a[self.__Nitems - 1] = None 
        self.__Nitems -= 1 
        return item
    
    def peek(self):
        return self.__a [0]
    
    def traverse(self):
        for i in range(self.__Nitems):
            print (self.__a[i])
    
    def ordenar(self):
        for j in range(self.__Nitems-1):
            for i in range(self.__Nitems - 1 - j):
                if self.__a [i]%2 !=0 and self.__a [i+1]%2 ==0:
                    self.__a [i],self.__a [i+1]=self.__a [i+1],self.__a [i]


Maxsize=10
col=cola(Maxsize)
a=[1,2,3,4,5,6,7,8,9]
for i in a:
    col.enqueue(i)
print("Cola")
col.traverse()
col.ordenar()
print("Cola despues de ordenar")
col.traverse()