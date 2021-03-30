import random
from search_tree import Search_TreeBinary

random.seed(77)

def random_tree(size=42):
    values = random.sample(range(1, 1000), 42)
    tree = Search_TreeBinary()
    for v in values:
        tree.insert(v)
    return tree

def example_tree():
    values = [61, 89, 66, 43, 51, 16, 55, 11, 79, 77, 82, 32]
    tree = Search_TreeBinary()
    for v in values:
        tree.insert(v)
    return tree

def extended_tree():
    values = [61, 89, 66, 43, 51, 16, 55, 11, 79, 77, 82, 32, 100, 90]
    tree = Search_TreeBinary()
    for v in values:
        tree.insert(v)
    return tree

bst = extended_tree()
bst.inorder_traversal()

# testar remoção da árvore
print('\n----')
v = 61
bst.remove(v)
print("Após remover {}".format(v))
bst.inorder_traversal()
print('\n')
bst.levelorder_traversal()

print("\n-------")
print("Máximo:", bst.max())
print("Mínimo:", bst.min())

