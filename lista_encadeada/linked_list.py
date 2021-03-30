from node import Node

class LinkedList:

    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, element):
        if self.head:
            # Verifica qual é o último elemento
            pointer =  self.head
            while(pointer.next):
                pointer = pointer.next
            # Adiciona o último nó criado como próximo nó do penúltimo
            pointer.next = Node(element)
        else:
            # Adiciona o primeiro nó
            self.head = Node(element)

        self._size += 1
    
    def insert(self, index, element):
        node = Node(element)

        if index == 0:
            node.next = self.head
            self.head = node
        else:
            # O último nó não conhece o próximo por isso - 1
            pointer = self._getNode(index-1)
            # Conecta o novo nó com a lista
            node.next = pointer.next
            pointer.next = node

        self._size += 1
    
    def remove(self, element):
        if self.head == None:
            raise ValueError("{} is not in list".format(element))
        elif self.head.data == element:
            self.head = self.head.next
            self._size -= 1
            return True
        else:
            ancestor = self.head
            pointer = self.head.next
            while(pointer):
                # Liga o antecessor ao sucessor
                if pointer.data == element:
                    ancestor.next = pointer.next
                    pointer.next = None
                ancestor = pointer
                pointer = pointer.next
                self._size -= 1
                return True
        raise ValueError("{} is not in list".format(element))
        
        
    def __len__(self):
        """
        Retorna o tamanho da lista
        """
        return self._size

    def _getNode(self, index):
        pointer = self.head
        # Andar até o index inserido
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        return pointer

    def __getitem__(self, index):
        pointer = self._getNode(index)

        if pointer:
            return pointer.data
        raise IndexError("list index out of range")

    def __setitem__(self, index, element):
        pointer = self._getNode(index)

        if pointer:
            pointer.data = element
        else:
            raise IndexError("list index out of range")

    
    def index(self, element):
        """
        Retorna o índice do elemento na lista
        """
        pointer = self.head
        i = 0
        while(pointer):
            if pointer.data == element:
                return i
            pointer = pointer.next
            i += 1
        
        raise ValueError("{} is not in list".format(elem))

    def __repr__(self):
        r = ""
        pointer = self.head
        while(pointer):
            r += str(pointer.data) + "->"
            pointer = pointer.next
        return r   
             
    def __str__(self):
        return self.__repr__()