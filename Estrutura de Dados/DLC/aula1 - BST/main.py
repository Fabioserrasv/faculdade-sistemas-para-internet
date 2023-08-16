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
    
    def __min_node(self, node):
        if node is None:
            return None

        current = node
        while current.left is not None:
            current = current.left

        return current

    def deleteNode(self, node, value):
        if node is None:
            return None

        if value < node.value:
            node.left = self.deleteNode(node.left, value)
            return node

        if value > node.value:
            node.right = self.deleteNode(node.right, value)
            return node

        if node.left is None and node.right is None:
            return None

        if node.left is None or node.right is None:
            return node.right if node.left is None else node.left

        aux = self.__min_node(node.right)
        aux_value = aux.value

        result_remove_node = self.deleteNode(node.right, aux_value)

        new_node = Node(aux_value)
        new_node.left = node.left
        new_node.right = result_remove_node
        return new_node

bst = Bst()

valores = (np.random.randint(0,99,(1,8)))[0]

# for i in range(0, 6):
#     bst.add_value(valores[i])


#75,42,82,11,74,32,69,56
bst.add_value(75)
bst.add_value(42)
bst.add_value(82)
bst.add_value(11)
bst.add_value(74)
bst.add_value(32)
bst.add_value(69)
bst.add_value(56)


tree_printer(bst)
print("-"*8)
bst.deleteNode(bst.root, 42)
tree_printer(bst)

print("deleted:" + str(42))