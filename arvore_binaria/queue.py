#FIFO(First in first out)
from node import Node

class Queue:

    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    def push(self, element):
        node = Node(element)
        
        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last = node

        if self.first is None:
            self.first = node 

        self._size += 1

    def pop(self):
        """Remove o elemento do topo da pilha""" 
        if self._size > 0:
            elem = self.first.data
            self.first = self.first.next
            # faltou tratar este caso no vídeo #
            if self.first is None:
                self.last = None
            ####################################
            self._size = self._size - 1
            return elem
        raise IndexError("The queue is empty")
        
    def peek(self):
        if self.first is not None:
            element = self.first.data
            return element

        raise IndexError("The queue is empty")        
    
    def __len__(self):
        return self._size

    def __repr__(self):
        if self.first is not None:
            r = ""
            pointer = self.first
            while pointer:
                r += str(pointer.data) + " "
                pointer = pointer.next       
            return r
        return "Empty queue"

    def __str__(self):
        return self.__repr__()