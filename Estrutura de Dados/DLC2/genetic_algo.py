from entities.individual import Individual
from products import products
from ordened_vector import OrderedVector
from utils import compare, revert
import random
import math

BAG_VOLUME = 5

class GeneticAlgorithm:
  @staticmethod
  def execute(population_length, amount_generation):
    individuals = OrderedVector(population_length * amount_generation, revert(compare))
    best_individuals = OrderedVector(amount_generation + 1, revert(compare))
    
    for x in range(population_length):
      individuals.insert(Individual(products, BAG_VOLUME, 0))
    
    for i in range(amount_generation):
      best_individuals.insert(individuals.get(0))
      child_individuals = OrderedVector(population_length * amount_generation, revert(compare))

      population_score = GeneticAlgorithm.get_population_sum(individuals)
      new_individuals = GeneticAlgorithm.get_new_random_population(individuals, population_score)

      for y in range(population_length // 2):
        index = y
        index2 = y+1

        i1 = new_individuals[index]
        i2 = new_individuals[index2]
        
        f1, f2 = i1.crossover(i2)
        child_individuals.insert(f1)
        child_individuals.insert(f2)
      individuals = child_individuals
    return best_individuals

  @staticmethod
  def get_population_sum(population):
    return sum([x.get_solution_rating() for x in population])
  
  @staticmethod
  def russian_roullete(population, population_score):
    random_value = random.randrange(0,math.floor(population_score))
    sum = 0
    for i in population:
      if sum + i.get_solution_rating() >= random_value:
        return i
      sum += i.get_solution_rating()
    
  def get_new_random_population(population, population_score):
    return [
      GeneticAlgorithm.russian_roullete(population, population_score)
      for _ in range(len(population))
    ]