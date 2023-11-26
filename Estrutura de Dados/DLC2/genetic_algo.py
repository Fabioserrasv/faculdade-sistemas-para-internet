from entities.individual import Individual
from entities.products import products
from entities.ordened_vector import OrderedVector
from utils import compare, revert
import random
import math

class GeneticAlgorithm:
  @staticmethod
  def execute(population_length, amount_generation, bag_volume, mutation_rate):
    individuals = OrderedVector(population_length * amount_generation, revert(compare))
    best_individuals = []
    
    for x in range(population_length):
      individuals.insert(Individual(products, bag_volume, 0, mutation_rate))
    
    for i in range(amount_generation):
      # best_individuals.insert(individuals.get(0))
      best_individuals.append(individuals.get(0))
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
    best = best_individuals[0]
    for i in best_individuals:
      if i.get_solution_rating() > best.get_solution_rating():
        best = i
    return best_individuals, best

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