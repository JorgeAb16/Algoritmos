class pila():
    def __init__(self,Initialsize):
        self.__a= [None]*Initialsize
        self.__Nitems=0

    def __len__(self):
        return self.__Nitems
    
    def push(self,item):
        self.__a[self.__Nitems]=item
        self.__Nitems +=1
    
    def pop(self):
        item = self.__a[self.__Nitems-1]
        self.__a[self.__Nitems-1]=None
        self.__Nitems-=1
        return item
    
    def traverse(self):
        for i in range(self.__Nitems):
            print (self.__a[i])

    def invertir(self):
        invertido=[]
        for i in range(self.__Nitems-1,-1,-1):
           invertido.append(self.__a[i])
        return invertido

MaxSize=100
arr = pila(MaxSize)
frase = "Pasas"
for item in frase:
    if not item.isspace():
       arr.push(item)
arr.traverse()
print("Cadena invertida")
print(arr.invertir())