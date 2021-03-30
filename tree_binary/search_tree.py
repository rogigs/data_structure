from tree_binary import TreeBinary
from node import Node

ROOT = "root"

class Search_TreeBinary(TreeBinary):
    
    def insert(self, value):
      
        parent = None
        aux_parent = self.root

        # Percorre a árvore para saber quem é folha
        while aux_parent:
            # Adiciona folha a parent
            parent = aux_parent
            # Caminha para esquerda ou direita
            if value < aux_parent.data:
                aux_parent = aux_parent.left
            else:
                aux_parent = aux_parent.right

        # Insere o nó na direita ou esquera ou inicia arvore
        if parent is None:
            self.root = Node(value)
        elif value < parent.data:
            parent.left = Node(value)
        else:
            parent.right = Node(value)

    def search(self, value):
        return self._search(value, self.root)

    def _search(self, value, node=0):
        if node == 0:
            node = self.root
        #Retorna o nó
        if node is None:
            return node
        if node.data == value:
            return Search_TreeBinary(node)
        # Percorre árvore
        if value < node.data:
            return self.search(value, node.left)
        return self.search(value, node.right)

    def min(self, node=ROOT):
        if node == ROOT:
            node = self.root
        if node.left:
            return self.min(node.left)
        return node.data

    def max(self, node=ROOT):
        if node == ROOT:
            node = self.root
        if node.right:
            return self.max(node.right)
        return node.data

    def remove(self, value, node=ROOT):
         # Se for o valor padrão, executa a partir da raiz
        if node == ROOT:
            node = self.root
        # Se desceu até um ramo nulo, não há nada a fazer
        if node is None:
            return node
        # Se o valor for menor, desce à esquerda
        if value < node.data:
            node.left = self.remove(value, node.left)
        # Se o valor for maior, desce à direita
        elif value > node.data:
            node.right = self.remove(value, node.right)
        # Se não for nem menor, nem maior, encontramos! Vamos remover...
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                # Substituto é o sucessor do valor a ser removido
                substitute = self.min(node.right)
                # Ao invés de trocar a posição dos nós, troca o valor
                node.data = substitute
                # Depois, remove o substituto da subárvore à direita
                node.right = self.remove(substitute, node.right)
        return node
    
