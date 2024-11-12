class LinkedList(object):

    def traverse(self):
        elementos = []
        for data in self:  
            elementos.append(data)
        return elementos

    def __str__(self):
        return ' -> '.join(str(data) for data in self)  

    def __len__(self):
        contador = 0
        for _ in self: 
            contador += 1
        return contador
