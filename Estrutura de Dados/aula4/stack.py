import numpy as np

class StackException(Exception):
  pass

class Stack:
  def __init__(self, max_elements: int) -> None:
    if max_elements < 0:
      raise StackException("Minimum value of elements in invalid Stack")

    self.elements = np.array([None] * max_elements)
    self.max_elements = max_elements
    self.index_last_element = -1

  def full(self): 
    new_index_last_element = self.index_last_element + 1
    return new_index_last_element == self.max_elements

  def empty(self):
    return self.index_last_element == -1

  def push(self, new_value) -> None:
    if self.full():
      raise StackException("Maximum elements in Stack")
    
    new_index_last_element = self.index_last_element + 1
    self.elements[new_index_last_element] = new_value
    self.index_last_element = new_index_last_element

  def pop(self):
    if self.empty():
      return None

    item = self.elements[self.index_last_element]
    self.elements[self.index_last_element] = None
    self.index_last_element -= 1

    return item

  def __str__(self) -> str:
    str_list = " ".join([ str(x) for x in self.elements if not x == None ])
    return f"[ {str_list} ]"