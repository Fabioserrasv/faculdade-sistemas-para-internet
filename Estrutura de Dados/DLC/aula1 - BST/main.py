import json
from tree_printer import tree_printer
import numpy as np

COUNT = [10]
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def print_node(self):
        return {
            "value": self.value,
            "left": self.left.print_node() if self.left is not None else None,
            "right": self.right.print_node() if self.right is not None else None
        }
    
    def __str__(self):
        return(f"(Value: {self.value}, Children Nodes: Left: [{self.left}], ------------------ Right: [{self.right}])")

class Bst:
    def __init__(self):
        self.root = None

    def print_values(self):
        if self.root:
            print(json.dumps(bst.root.print_node(), indent=4))

    def search(self, value):
        aux = self.root
        while aux:
            if value == aux.value:
                return aux
            if value > aux.value:
                aux = aux.right
            else:
                aux = aux.left
        return None

    def add_value(self, value):
        if not self.root:
            self.root = Node(value)
            return

        aux = self.root
        while aux:
            if aux:
                if value == aux.value:
                    return
                if value > aux.value:
                    if aux.right:
                        aux = aux.right
                        continue
                    aux.right = Node(value)
                    break
                else:
                    if aux.left:
                        aux = aux.left
                        continue
                    aux.left = Node(value)
                    break

bst = Bst()

valores = (np.random.randint(0,1000,(1,8)))[0]

for i in range(0, 8):
    bst.add_value(valores[i])

tree_printer(bst)