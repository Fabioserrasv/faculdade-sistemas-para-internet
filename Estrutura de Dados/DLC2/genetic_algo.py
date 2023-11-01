from entities.individual import Individual
from products import products
from ordened_vector import OrderedVector
from utils import compare, revert

BAG_VOLUME = 10

class GeneticAlgorithm:
  def __init__(self, population_length, amount_generation) -> None:
    self.__individuals = OrderedVector(10000, revert(compare))

    for x in range(population_length):
      self.__individuals.insert(Individual(products, BAG_VOLUME, 0))
    
    for i in range(amount_generation):
      for y in range(population_length):
        index = y
        index2 = y+1

        i1 = self.__individuals.get(index)
        i2 = self.__individuals.get(index2)
        
        f1, f2 = i1.crossover(i2)
        self.__individuals.insert(f1)
        self.__individuals.insert(f2)
    best = self.__individuals.pop(0)
    print(best)