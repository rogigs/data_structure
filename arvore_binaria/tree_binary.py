import queue
from node import Node
from queue import Queue

ROOT = "root"

class TreeBinary:

    def __init__(self, data=None, node=None):
        if node:
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    """
    Percuso em ordem simétrica
    """
    def simetric_traversal(self, node=None):
        if node is None:
            node = self.root

        # Mostro quem está a esquerda
        if node.left:
            print("(", end="")
            self.simetric_traversal(node.left)
        #Mostro quem está ao centro
        print(node, end= "")
        #Mostro quem está a direita
        if node.right:
            self.simetric_traversal(node.right)
            print(")", end="")

    def inorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.inorder_traversal(node.left)
        print(node, end=' ')
        if node.right:
            self.inorder_traversal(node.right)
    """
    Percurso pós ordem
    """
    def postorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.postorder_traversal(node.left)
        if node.right: 
            self.postorder_traversal(node.right)
        else:
            if not node.left and not node.right:
                pass
            else:
                print("-")

        print(node)

    """
    Percurso em nivel
    """
    def levelorder_traversal(self, node=ROOT):
        if node == ROOT:
            node = self.root
        
        queue = Queue()
        queue.push(node)

        #PERCORRE FILE
        while len(queue):
            node = queue.pop()
            #ADICIONA NÓS FILHOS A FILA
            if node.left:
                queue.push(node.left)
            if node.right:
                queue.push(node.right)

            print(node, end=" ")
            

    def height(self, node=None):
        if node is None:
            node = self.root
        h_left = 0
        h_right = 0
        if node.left:
            h_left = self.height(node.left)
        if node.right:
            h_right = self.height(node.right)
        
        if h_right > h_left:
            return h_right + 1
        return h_left + 1
        