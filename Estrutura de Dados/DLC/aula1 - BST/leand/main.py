import random
from bst_leand import BinarySearchTree

b = BinarySearchTree()
list_values = []
for i in range(0, 7):
    value = random.randint(0, 30)
    b.add(value)
    list_values.append(value)

b.show_graph()

b.remove(list_values[2])

b.show_graph()