import random
import matplotlib.pyplot as plt
from heuristics import heuristics
from utils import generate_initial_matrix, print_matrix
from board import Board
from astar import a_star_8_puzzle

def execute_single_board(heuristic, show_path):
  initial_matrix = generate_initial_matrix(MOVEMENTS=1000)
  board = Board(initial_matrix, None, heuristic)
  path, movements, time = a_star_8_puzzle(board)

  if show_path:
    for b in path:
      print_matrix(b)

  print(f"""
    Heuristic: {heuristic.__name__}
    Movements: {movements}
    Time: {time}
  """)

def execute_all_heuristics_and_analysis(amount_tests):
  results = []
  matrixes = []
  colors = [[]] * amount_tests
  for y in range(amount_tests):
    initial_matrix = generate_initial_matrix(MOVEMENTS=1000)
    matrixes.append(initial_matrix)
    colors[y] = [random.random() for _ in range(3)]
  for index, heuristic in heuristics.items():
    for j in range(amount_tests):
      color = colors[j]
      initial_board = Board(matrixes[j], None, heuristic)
      path, movements, time = a_star_8_puzzle(initial_board)

      results.append({
        "path": path,
        "heuristic": index,
        "movements": movements,
        "time": time,
        "color": color
      })

  results.sort(key=lambda x: x["time"])

  for result in results:
    plt.scatter(result["time"], result["movements"], label=(str(result["heuristic"]) + " " + "{:.4f}".format(result["time"])), color=result["color"])

  plt.ylabel('Movements')
  plt.xlabel('Time')
  plt.legend()
  plt.show()

