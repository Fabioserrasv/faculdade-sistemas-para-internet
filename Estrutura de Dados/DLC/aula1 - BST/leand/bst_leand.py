# import json
from node import Node
from show_tree import ShowTree


class BinarySearchTree:

    def __init__(self):
        self.__root = None

    def add(self, new_value):
        new_node = Node(new_value)
        if not self.__root:
            self.__root = new_node
            return

        current_node = self.__root

        while current_node:
            if current_node.value == new_value:
                return

            if current_node.value > new_value:
                if current_node.left:
                    current_node = current_node.left
                    continue

                current_node.left = new_node
                return

            if current_node.right:
                current_node = current_node.right
                continue

            current_node.right = new_node
            return

    def search(self, value):
        current_node = self.__root
        while current_node:
            if current_node.value == value:
                return current_node

            if current_node.value > value:
                current_node = current_node.left
            else:
                current_node = current_node.right

        return None

    def pre_order(self, callback):
        return self.__pre_order(self.__root, callback)

    def __pre_order(self, node, callback):
        if node is None:
            return

        callback(node)
        self.__pre_order(node.left, callback)
        self.__pre_order(node.right, callback)

    def in_order(self, callback):
        return self.__in_order(self.__root, callback)

    def __in_order(self, node, callback):
        if node is None:
            return

        self.__in_order(node.left, callback)
        callback(node)
        self.__in_order(node.right, callback)

    def post_order(self, callback):
        return self.__post_order(self.__root, callback)

    def __post_order(self, node, callback):
        if node is None:
            return

        self.__post_order(node.left, callback)
        callback(node)
        self.__post_order(node.right, callback)

    def show_graph(self):
        if not self.__root:
            return ""

        show_tree = ShowTree()
        return show_tree.display_tree(self.__root)

        # return json.dumps(self.__root.values(), indent=4)

    def __min_node(self, node):
        if node is None:
            return None

        current = node
        while current.left is not None:
            current = current.left

        return current

    def remove(self, value):
        self.__root = self.__remove_node(self.__root, value)

    def __remove_node(self, node, value):
        if node is None:
            return None

        if value < node.value:
            node.left = self.__remove_node(node.left, value)
            return node

        if value > node.value:
            node.right = self.__remove_node(node.right, value)
            return node

        if node.left is None and node.right is None:
            return None

        if node.left is None or node.right is None:
            return node.right if node.left is None else node.left

        aux = self.__min_node(node.right)
        aux_value = aux.value

        result_remove_node = self.__remove_node(node.right, aux_value)

        new_node = Node(aux_value)
        new_node.left = node.left
        new_node.right = result_remove_node
        return new_node
