import random

zero_or_one = lambda _x: random.choice([0, 1])

class Individual:
  def __init__(self, items, limit, generation = 0, chromossomes = None) -> None:
    self.__items = items
    self.__limit = limit
    self.__generation = generation
    self.__value = 0
    self.__volume = 0
    self.__score = 1

    if chromossomes is None:
      self.__chromossomes = [None] * len(items)
      self.__generate_chromossomes()
    else:
      self.__chromossomes = chromossomes

    self.__generate_values()

  def get_chromossomes(self):
    return self.__chromossomes

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

    self.__score = self.__value
    return self.__score

  def crossover(self, other_individual):
    crossover_point = random.randrange(0, len(self.__items), 1)
    chromossomes2 = other_individual.get_chromossomes()

    c1 = self.mutation(self.__chromossomes[:crossover_point] + chromossomes2[crossover_point:])
    c2 = self.mutation(chromossomes2[:crossover_point] + self.__chromossomes[crossover_point:])

    return Individual(
      self.__items,
      self.__limit,
      self.__generation + 1,
      c1
    ), Individual(
      self.__items,
      self.__limit,
      self.__generation + 1,
      c2
    )

  def mutation(self, chromossomes):
    mutation_rate = 5
    for i in range(len(chromossomes)):
      if random.randrange(0, 100) < mutation_rate:
        chromossomes[i] = 0 if chromossomes[i] == 1 else 1
    return chromossomes

  def __str__(self) -> str:
    return f"Price: {self.__value}, Volume: {self.__volume} Generation: {self.__generation},C:" + self.__chromossomes.__str__()

  def __eq__(self, individual) -> bool:
    if not isinstance(individual, Individual):
      return False
    return self.__score == individual.get_solution_rating();

  # def rate_solution(self):
