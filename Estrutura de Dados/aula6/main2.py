import numpy as np

class PriorityQueueException(Exception):
  pass

class PriorityQueue:

  def __init__(self, max_elements: int) -> None:
    if max_elements < 0:
      raise PriorityQueueException("Minimum value of elements in invalid PriorityQueue")

    self.elements = np.array([None] * max_elements)
    self.max_elements = max_elements
    self.index_last_element = -1

  def full(self): 
    return self.max_elements == self.index_last_element + 1

  def empty(self):
    return self.index_last_element == -1

  def __get_index_of_first_element_with_highest_priority(self, value: int):
    if self.index_last_element == -1:
      return 0

    for index in range(self.index_last_element + 1):
      if value > self.elements[index]:
        return index

    return self.index_last_element + 1

  def push(self, new_value: int) -> None:
    if self.full():
      raise PriorityQueueException("Maximum elements in PriorityQueue")
    
    new_index_last_element = self.index_last_element + 1

    index_first_more = self.__get_index_of_first_element_with_highest_priority(new_value)
    if index_first_more == -1 or index_first_more == new_index_last_element:
        self.elements[new_index_last_element] = new_value
        self.index_last_element = new_index_last_element
        return

    
    for index in range(new_index_last_element, index_first_more, -1):
        self.elements[index] = self.elements[index - 1]

    self.elements[index_first_more] = new_value
    self.index_last_element = new_index_last_element



  def pop(self):
    if self.empty():
      return None

    item = self.elements[0]

    for index in range(0, self.index_last_element):
      self.elements[index] = self.elements[index + 1]

    self.elements[self.index_last_element] = None
    self.index_last_element -= 1

    return item


  def __str__(self) -> str:
    str_list = " ".join([ str(x) for x in self.elements if not x == None ])
    return f"[ {str_list} ]"