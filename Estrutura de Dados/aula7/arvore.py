class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def __str__(self):
    return "{" + f" value: {self.value}, left: {self.left}, rigth: {self.right} " + "}" 

class TreeBinary: 
  def __init__(self):
    self.root = None

  def add(self, value):
    if not self.root:
      self.root = Node(value)
    else:
      self.__addNode(self.root, value)

  def __addNode(self, node: Node, value):
    if node.value > value:
      if not node.left:
        node.left = Node(value)
      else:
        self.__addNode(node.left, value)
    else:
      if not node.right:
        node.right = Node(value)
      else:
        self.__addNode(node.right, value)

  def show(self):
    if not self.root:
      return []

    return self.__showNode(self.root)

  def __showNode(self, node):
    if not node:
      return []

    return [ *self.__showNode(node.left), node.value, *self.__showNode(node.right) ]

  def showRoot(self):
    return self.root.__str__()
  

        

treebinary = TreeBinary()
treebinary.add(15)
treebinary.add(5)
treebinary.add(7)
treebinary.add(9)
treebinary.add(1)

print(treebinary.show())
print(treebinary.showRoot())