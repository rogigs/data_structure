#LFO(last in first out)
from node import Node

class Stack:

    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, element):
        node = Node(element)
        # Conecta ao penultimo elemento
        node.next = self.top
        # Adiciona ao topo
        self.top = node
        self._size += 1

    def pop(self):
        if self._size > 0:
            # O topo vira o next de topo
            node = self.top
            self.top = self.top.next
            self._size -= 1
            return node
        raise IndexError("The stack is empty")
        
    def peek(self):
        """
        Retorna quem é o toppo
        """
        if self._size > 0:
            return self.top.data
        raise IndexError("The stack is empty")

    def __len__(self):
        """
        Retorna o tamanho da lista
        """
        return self._size

    def __repr__(self):
        r = ""
        pointer = self.top
        while(pointer):
            r += str(pointer.data) + "\n"
            pointer = pointer.next
        return r   
             
    def __str__(self):
        return self.__repr__()