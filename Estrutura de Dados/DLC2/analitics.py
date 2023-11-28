from genetic_algo import GeneticAlgorithm
import matplotlib.pyplot as plt
from config import POPULATION_LENGTH, GENERATIONS, BAG_VOLUME, MUTATION_RATE

DATA_TESTS = [
  # BAG_VOLUME, MUTATION_RATE, POPULATION_LENGTH, GENERATION
  [20, 2, 300, 200],
  [20, 5, 300, 200],
  [20, 10, 300, 200],
  [20, 50, 300, 200],
]

class Analysis:

  @staticmethod
  def execute_analysis():
    fig, axes = plt.subplots(1, 4, figsize=(10, 5))
    
    for col, data in enumerate(DATA_TESTS):
      bag_volume = data[0]
      mutation_rate = data[1]
      population_length = data[2]
      generations = data[3]

      result, best = GeneticAlgorithm.execute(population_length, generations, bag_volume, mutation_rate)
      print(f"--------------------------\nTest {col}:\nValor: {best.get_solution_rating()}\nPeso: {best.solution_volume()}")
      axes[col].plot(
        [x for x in range(len(result))],
        [i.get_solution_rating() for i in result]
      )
      axes[col].set_title(f"Valor: {best.get_solution_rating()}\nPeso: {best.solution_volume()}")
    plt.show()
  
  @staticmethod
  def execute_single_analysis():
    result, best = GeneticAlgorithm.execute(POPULATION_LENGTH, GENERATIONS, BAG_VOLUME, MUTATION_RATE)

    plt.plot(
      [x for x in range(len(result))],
      [i.get_solution_rating() for i in result]
    )

    print(best)

    plt.show()

    