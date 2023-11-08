from entities.individual import Individual
from products import products
from ordened_vector import OrderedVector
from utils import compare, revert
import random
import math

BAG_VOLUME = 10

class GeneticAlgorithm:
  def __init__(self, population_length, amount_generation) -> None:
    individuals = OrderedVector(population_length * amount_generation, revert(compare))
    best_individuals = OrderedVector(amount_generation + 1, revert(compare))
    
    for x in range(population_length):
      individuals.insert(Individual(products, BAG_VOLUME, 0))
    
    for i in range(amount_generation):
      best_individuals.insert(individuals.get(0))
      child_individuals = OrderedVector(population_length * amount_generation, revert(compare))
      population_score = self.get_population_sum(individuals)
      new_individuals = self.get_new_random_population(individuals, population_score)
      
      for y in range(population_length // 2):
        index = y
        index2 = y+1

        i1 = new_individuals[index]
        i2 = new_individuals[index2]
        
        f1, f2 = i1.crossover(i2)
        child_individuals.insert(f1)
        child_individuals.insert(f2)
      individuals = child_individuals
    print(self.russian_roullete(individuals, self.get_population_sum(individuals)))
    
  
  def get_population_sum(self, population):
    return sum([x.get_solution_rating() for x in population])

  def russian_roullete(self, population, population_score):
    random_value = random.randrange(0,math.floor(population_score))
    sum = 0
    for x in range(len(population) -1 , -1, -1):
      i = population.get(x)
      if sum + i.get_solution_rating() >= random_value:
        return i
      sum += i.get_solution_rating();
    
  def get_new_random_population(self, population, population_score):
    return [
      self.russian_roullete(population, population_score)
      for _ in range(len(population))
    ]