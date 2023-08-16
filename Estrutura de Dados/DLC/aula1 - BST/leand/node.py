class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def values(self):
        return {
            "value": self.value,
            "left": self.left.values() if self.left is not None else None,
            "right": self.right.values() if self.right is not None else None,
        }