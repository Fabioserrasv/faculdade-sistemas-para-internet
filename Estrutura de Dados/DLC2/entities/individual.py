import random

zero_or_one = lambda _x: random.choice([0, 1])

class Individual:
  def __init__(self, items, limit, generation = 0) -> None:
    self.__items = items
    self.__limit = limit
    self.__generation = generation
    self.__value = 0
    self.__volume = 0
    self.__score = 0

    self.__chromossomes = [None] * len(items)
    self.__generate_chromossomes()
    self.__generate_values()

  def __generate_chromossomes(self):
    self.__chromossomes = [zero_or_one(i) for i in self.__items]

  def __generate_values(self):
    for index, i in enumerate(self.__chromossomes):
      if i == 1:
        self.__value += self.__items[index].get_value()
        self.__volume += self.__items[index].get_volume()

  def get_solution_rating(self):
    if self.__volume > self.__limit:
      return self.__score

    
  # def rate_solution(self):


