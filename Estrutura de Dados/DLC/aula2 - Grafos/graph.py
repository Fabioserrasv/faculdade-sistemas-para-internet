from neighbours import Neighbour
from vertex import Vertex

class Graph:
  def __init__(self) -> None:
    self.__vertexes = {}
    self.__visited_array = {}

  def add_vertex(self, name):
    if not self.__vertexes.get(name, None):
      new_vertex = Vertex(name)
      self.__vertexes[name] = new_vertex
  
  def add_connection(self, vertex_from: Vertex, vertex_to: Vertex, weight):
    v1 = self.__vertexes.get(vertex_from, None)
    v2 = self.__vertexes.get(vertex_to, None)
    
    new_neighbour = Neighbour(v2, weight)
    v1.add_neighbour(new_neighbour)

    # if v1 and v2:
    #   new_neighbour = Neighbour(v2, weight)
    #   self.__vertexes[vertex_from].add_neighbour(new_neighbour)

    #   new_neighbour2 = Neighbour(v1, weight)
    #   self.__vertexes[vertex_to].add_neighbour(new_neighbour2)

  def get_vertex(self, name):
    return self.__vertexes.get(name, None)
  
  def search_node(self, vertex_from, vertex_to):
    if vertex_from.name in self.__visited_array:
      return None

    self.__visited_array[vertex_from.name] = True
    for neighbour in vertex_from.get_neighbours():
      if neighbour.vertex.name == vertex_to.name:
        return [vertex_from.name, neighbour.vertex.name]

    l = []

    for neighbour in vertex_from.get_neighbours():
      result = self.search_node(neighbour.vertex, vertex_to)

      if result:
        l.append([vertex_from.name] + result)
    max = None
    for x in l:
      if max is None or len(x) < len(max):
        max = x
    if max:
      return max
    return None

  def search(self, vertex_from: Vertex, vertex_to: Vertex):
    v1 = self.__vertexes.get(vertex_from, None)
    v2 = self.__vertexes.get(vertex_to, None)
    self.__visited_array = {}
    for neighbour in v1.get_neighbours():
      if neighbour.vertex.name == v2.name:
        return [v1.name, v2.name]

      result = self.search_node(neighbour.vertex, v2)
      if result:
        return [v1.name] + result
    
    return None
