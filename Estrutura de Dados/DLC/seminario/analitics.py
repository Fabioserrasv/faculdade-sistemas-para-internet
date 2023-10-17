import timeit
import random
import matplotlib.pyplot as plt
from heuristics import heuristics
from utils import generate_initial_matrix
from board import Board
from astar import a_star_8_puzzle


def execute_all_heuristics_and_analysis(amount_tests):
  results = []
  matrixes = []
  colors = [[]] * amount_tests
  for y in range(amount_tests):
    initial_matrix = generate_initial_matrix(MOVEMENTS=1000)
    matrixes.append(initial_matrix)
    colors[y] = [random.random() for _ in range(3)]
  print(colors)
  for index, heuristic in heuristics.items():
    for j in range(amount_tests):
      color = colors[j]
      initial_board = Board(matrixes[j], None, heuristic)
      start = timeit.default_timer()
      path = a_star_8_puzzle(initial_board)
      end = timeit.default_timer()

      results.append({
        "path": "",
        "heuristic": index,
        "movements": len(path),
        "time": end - start,
        "color": color
      })

  results.sort(key=lambda x: x["time"])

  for result in results:
    plt.scatter(result["time"], result["movements"], label=(str(result["heuristic"]) + " " + "{:.2f}".format(result["time"])), color=result["color"])

  plt.ylabel('Movements')
  plt.xlabel('Time')
  plt.legend()
  plt.show()


  # print(results)
execute_all_heuristics_and_analysis(3)