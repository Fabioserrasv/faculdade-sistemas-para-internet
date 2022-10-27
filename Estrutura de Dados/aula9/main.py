from time import time
import numpy as np
import timeit
from utils import debug
import matplotlib.pyplot as plt
from vetor_ordenado import VetorOrdenado

from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from shell_sort import shell_sort
from merge_sort import merge_sort
from quick_sort import quick_sort

algorithms = {
  "bubble": bubble_sort,
  "selection": selection_sort,
  "insertion": insertion_sort,
  "shell_sort": shell_sort,
  "merge_sort": merge_sort,
  "quick_sort": quick_sort
}

@debug
def sort(array, type_algorithm = "bubble"):
  algorithm_sort = algorithms.get(type_algorithm, None)
  if not algorithm_sort:
    raise Exception("Type Algorithm Not Found")

  return algorithm_sort(array)


result = {}

for i in range(1,6):
  cinco_mil_valores = (np.random.randint(0,1000,(1,5000)))[0]
  for i in algorithms:
    start = 0
    end   = 0
    if(i == 'quick_sort'):
      start = timeit.default_timer()
      algorithms[i](cinco_mil_valores, 0, len(cinco_mil_valores) - 1)
      end = timeit.default_timer()
    else:
      start = timeit.default_timer()
      sort(cinco_mil_valores, i)
      end = timeit.default_timer()
    if i in result.values():
      result[i] = result[i] + (end - start)
    else:
      result[i] = end-start
  #Vetor Ordenado
  vOrdenado = VetorOrdenado(5000)
  start = timeit.default_timer()
  for i in cinco_mil_valores:
    vOrdenado.insere(i)
  if 'vetor_ordenado' in result.values():
      result['vetor_ordenado'] = result['vetor_ordenado'] + (end - start)
  else:
      result['vetor_ordenado'] = timeit.default_timer() - start
  
result = dict(sorted(result.items(), key=lambda item: item[1]))

for i in result:
    plt.scatter(i, result[i], label = str(i) + str(end-start))

plt.ylabel('Tempo')
plt.xlabel('Algoritmo')
plt.show()

print(result)
