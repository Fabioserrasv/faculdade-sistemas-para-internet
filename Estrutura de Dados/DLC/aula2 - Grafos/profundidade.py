from stack import Stack
class DFS:
  def __init__(self, initial):
    self.initial = initial
    self.__visited_array = {}
    self.__visited_array[initial.name] = True
    self.my_stack = Stack(100)
    self.my_stack.push(initial)
    