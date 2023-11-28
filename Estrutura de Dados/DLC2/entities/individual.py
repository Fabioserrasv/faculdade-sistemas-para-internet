import random
zero_or_one = lambda _x: random.choice([0, 1])

class Individual:
  def __init__(self, items, limit, generation = 0, mutation_rate = 5, chromossomes = None) -> None:
    self.__items = items
    self.__limit = limit
    self.__mutation_rate = mutation_rate
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

  def solution_volume(self):
    return self.__volume

  def get_solution_rating(self):
    if self.__volume > self.__limit:
      return self.__score

    self.__score = self.__value
    return self.__score

  def crossover(self, other_individual):
    c1,c2 = self.__random_point(other_individual) # SORTEADO PONTO
    # c1,c2 = self.__four_points(other_individual) # 4 PONTOS
    
    return Individual(
      self.__items,
      self.__limit,
      self.__generation + 1,
      self.__mutation_rate,
      c1
    ), Individual(
      self.__items,
      self.__limit,
      self.__generation + 1,
      self.__mutation_rate,
      c2
    )

  def mutation(self, chromossomes):
    for i in range(len(chromossomes)):
      if random.randrange(0, 100) < self.__mutation_rate:
        chromossomes[i] = 0 if chromossomes[i] == 1 else 1
    return chromossomes

  def __str__(self) -> str:
    return f"Price: {self.__value}, Volume: {self.__volume} Generation: {self.__generation},C:" + self.__chromossomes.__str__()

  def __eq__(self, individual) -> bool:
    if not isinstance(individual, Individual):
      return False
    return self.__score == individual.get_solution_rating();

  def __random_point(self, other_individual):
    crossover_point = random.randrange(0, len(self.__items), 1)
    chromossomes2 = other_individual.get_chromossomes()

    c1 = self.mutation(self.__chromossomes[:crossover_point] + chromossomes2[crossover_point:])
    c2 = self.mutation(chromossomes2[:crossover_point] + self.__chromossomes[crossover_point:])

    return c1, c2

  def __four_points(self, other_individual):
    points = sorted(random.sample(range(len(self.__items)), 4))
    chromossomes2 = other_individual.get_chromossomes()

    c1 = self.mutation(self.__chromossomes[:points[0]] +
                       chromossomes2[points[0]:points[1]] +
                       self.__chromossomes[points[1]:points[2]] +
                       chromossomes2[points[2]:points[3]] +
                       self.__chromossomes[points[3]:])

    c2 = self.mutation(chromossomes2[:points[0]] +
                       self.__chromossomes[points[0]:points[1]] +
                       chromossomes2[points[1]:points[2]] +
                       self.__chromossomes[points[2]:points[3]] +
                       chromossomes2[points[3]:])
    
    return c1, c2