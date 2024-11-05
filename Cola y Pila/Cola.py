
class Cola(object):
    
    def __init__(self, initialSize):  # Constructor
        self.__a = [None] * initialSize  # El array almacenado como una lista
        self.__nItems = 0  # No hay elementos en el array inicialmente
    def removeDupes(self):
        
        new_array = []  
        for j in range(self.__nItems):
            if self.__a[j] not in new_array:  
                new_array.append(self.__a[j])
        
        self.__a = new_array + [None] * (len(self.__a) - len(new_array))  # Ajustamos el tamaño
        self.__nItems = len(new_array)  # Actualizamos el número de elementos

    def __init__(self, initialSize):  # Constructor
        self.__a = [None] * initialSize  # El array almacenado como una lista
        self.__nItems = 0  # No h
    def __len__(self):  # Función especial para len()
        return self.__nItems  # Retorna el número de elementos

    def get(self, n):  # Devuelve el valor en el índice n
        if 0 <= n < self.__nItems:  # Verifica si n está en los límites
            return self.__a[n]  # Solo devuelve el ítem si está en los límites

    def set(self, n, value):  # Establece el valor en el índice n
        if 0 <= n < self.__nItems:  # Verifica si n está en los límites
            self.__a[n] = value  # Solo establece el ítem si está en los límites

    def insert(self, item):  # Inserta un ítem al final
        if self.__nItems < len(self.__a):  # Verificar espacio disponible
            self.__a[self.__nItems] = item  # El ítem va al final actual
            self.__nItems += 1  # Incrementa el número de elementos

    def find(self, item):  # Encuentra el índice del ítem
        for j in range(self.__nItems):  # Entre los ítems actuales
            if self.__a[j] == item:  # Si lo encuentra
                return j  # Entonces retorna el índice del ítem
        return -1  # No encontrado -> retorna -1

    def search(self, item):  # Busca un ítem
        return self.get(self.find(item))  # Y lo retorna si lo encuentra

    def deleter(self, item):  # Borra la primera ocurrencia de un ítem
        for j in range(self.__nItems):  # Entre los ítems actuales
            if self.__a[j] == item:  # Encuentra el ítem
                self.__nItems -= 1  # Un ítem menos al final
                for k in range(j, self.__nItems):  # Mueve los ítems de la derecha
                    self.__a[k] = self.__a[k + 1]  # Mueve los elementos a la izquierda
                return True  # Retorna éxito
        return False  # No se encontró el ítem

    def getMaxNum(self):  
        maxNum = None  
        for j in range(self.__nItems):  
            if isinstance(self.__a[j], (int, float)):  
                if maxNum is None or self.__a[j] > maxNum:  
                    maxNum = self.__a[j]
        return maxNum  

    def deleteMaxNum(self): 
        maxNum = self.getMaxNum()  
        if maxNum is not None:  
            self.delete(maxNum) 
            return maxNum  
        return None  

    def traverse(self, function=print): 
        for j in range(self.__nItems):  
            function(self.__a[j])

    def prom(self):  
        sum = 0
        cont=0
        for j in range(self.__nItems):  
            if isinstance(self.__a[j], (int, float)):
                cont +=1 
                sum += self.__a[j]
        return sum/cont   
        
    def cuenta(self,tipo):
        par = 0
        impar=0
        for j in range(self.__nItems):  
            if isinstance(self.__a[j], (int, float)):
                if (self.__a[j])% 2 == 0:
                    par+=1 
                else:
                    impar+=1
        if tipo==0:
            return impar
        if tipo==1:
            return par
       
    def letras(self):
        lista= []
        for j in range(self.__nItems):  
            if isinstance(self.__a[j], (str)):
               lista.append(self.__a[j])
        return lista 

        
    def push(self, item):            
        self.__a[self.__nItems]=item
        self.__nItems+=1
    
    def pop(self):
        item = self.__a[0]
        for i in range(1, self.__nItems): 
          self.__a[i - 1] = self.__a[i]
        self.__a[self.__nItems-1]= None 
        self.__nItems -= 1
        return item
    
    
      
        

        
        




         
    
         
    
    
                
    
 







        
    
         
            
            
        
         
                   
 
    
        
