class Cola(object):
    def __init__(self, initialSize):  # Constructor
        self.__a = [None] * initialSize  # El array almacenado como una lista
        self.__nItems = 0
        
    def __init__(self, initialSize):  # Constructor
        self.__a = [None] * initialSize  # El array almacenado como una lista
        self.__nItems = 0  # No h
    def __len__(self):  # Función especial para len()
        return self.__nItems  # Retorna el número de elementos
    def delete(self, item):  # Delete first occurrence of an item
        for j in range(self.__nItems):  # Among current items
            if self.__a[j] == item:  # Found item
                self.__nItems -= 1  # One fewer at end
                for k in range(j, self.__nItems):  # Move items from right over 1
                    self.__a[k] = self.__a[k+1]
                return True  # Return success flag
        return False  # Made it here, so couldn't find the item
    
    def insert(self, item):  # Inserta un ítem al final
        if self.__nItems < len(self.__a):  # Verificar espacio disponible
            self.__a[self.__nItems] = item  # El ítem va al final actual
            self.__nItems += 1  # Incrementa el número de elementos
        else:
            i=10
            for j in range(self.__nItems):
                if self.__nItems >= len(self.__a):
                    i-=1
                    self.delete(self.__a[i])
                self.__a[self.__nItems] = item  
                self.__nItems += 1  
            
            
    
    def traverse(self, function=print): 
        for j in range(self.__nItems):  
            function(self.__a[j]) 
            
    def poppil(self):
        item = self.__a[self.__nItems-1]
        self.__a[self.__nItems-1]= None 
        self.__nItems -= 1
        return item        
            
    def popcol(self):
        item = self.__a[0]
        for i in range(1, self.__nItems): 
          self.__a[i - 1] = self.__a[i]
        self.__a[self.__nItems-1]= None 
        self.__nItems -= 1
        return item          
    
    