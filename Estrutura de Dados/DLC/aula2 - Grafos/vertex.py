class Vertex:
  def __init__(self, name) -> None:
    self.name = name
    self.__visited = False
    self.__neighbours = []
  
  def add_neighbour(self, neighbour):
    self.__neighbours.append(neighbour)
  
  def get_neighbours(self):
    return self.__neighbours

  def visit(self):
    self.__visited = True

  def visited(self):
    return self.__visited