import numpy as np
import timeit
from utils import debug

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

cinco_mil_valores = (np.random.randint(0,1000,(1,5000)))[0]
result = {}
print(len(cinco_mil_valores))

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
  result[i] = [start, end]

print(result)

# 
# 

# sort(np.array([8, 6, 9, 2, 10, 1]), "bubble")
# sort(np.array([1, 2, 3, 15, 0, 6]), "selection")
# sort(np.array([8, 6, 9, 2, 10, 1]), "insertion")