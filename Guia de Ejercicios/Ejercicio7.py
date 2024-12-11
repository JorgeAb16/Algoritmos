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

    def parentesis(self):
        a=b=c=d=e=f=0
        for j in range(self.__Nitems-1,-1,-1):
            if self.__a[j] == "(":
                a += 1
            if self.__a[j] == ")":
                b += 1    
            if self.__a[j] == "[":
                c += 1
            if self.__a[j] == "]":
                d += 1
            if self.__a[j] == "{":
                e += 1
            if self.__a[j] == "}":
                f += 1    
        if a==b and c!=d and e!=f:
            return "Parentesis Balanceados\nCorchetes no Balanceados\nLlaves no balanceadas"
        if a==b and c==d and e==f :
            return "Parentesis Balanceados\nCorchetes Balanceados\nLlaves balanceadas"
        if c==d and a!=b and e!=f:
            return "Parentesis no Balanceados\nCorchetes Balanceados\nLlaves no balanceadas"
        elif c!=d and a!=b and e!=f:
            return "Parentesis no Balanceados\nCorchetes no Balanceados\nLlaves no balanceadas"
        elif c!=d and a!=b and e==f:
            return "Parentesis no Balanceados\nCorchetes no Balanceados\nLlaves balanceadas"
        elif c==d and a!=b and e==f:
            return "Parentesis no Balanceados\nCorchetes Balanceados\nLlaves balanceadas"
        elif c!=d and a==b and e==f:
            return "Parentesis Balanceados\nCorchetes no Balanceados\nLlaves balanceadas"
        elif c==d and a==b and e!=f:
            return "Parentesis Balanceados\nCorchetes Balanceados\nLlaves no balanceadas"
        
MaxSize=100
arr = pila(MaxSize)
frase = "{[(2+3)*5] - (4/2)} + [(8-6)*(7+1)]"
for item in frase:
    if not item.isspace():
       arr.push(item)
arr.traverse()
print(arr.parentesis()) 


