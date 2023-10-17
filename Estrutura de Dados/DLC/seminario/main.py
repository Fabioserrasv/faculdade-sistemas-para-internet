from heuristics import heuristics
from analitics import execute_all_heuristics_and_analysis, execute_single_board
import sys

sys.setrecursionlimit(2000)

def show_options():
    print("====================")
    i = 1
    for index in heuristics:
      print(i, "-", index)
      i += 1;
    print(i, "-", "Execute all and analyze")
    print("0", "-", "Quit")
    print("====================")

op = 999
options = list(heuristics.items())

while op != 0:
  show_options()
  op = int(input("Choose option:"))

  if op == len(heuristics) + 1:
    amount_tests = int(input("Number of tests:"))
    graph_type = int(input("Graph type:  0(Color by Heuristic) / 1(Color by Border)"))
    execute_all_heuristics_and_analysis(amount_tests, graph_type)

  if op > 0 and op <= len(heuristics):
    print(f"Selected {options[op-1][0]}")
    show_path = int(input("Show path? 1(yes) / 0(No)"))
    show_path = True if show_path == 1 else False
    heuristic = options[op-1][1]
    execute_single_board(heuristic, show_path) 
  elif op == 0:
    print("Bye~~")
  else:
    print("Option not found.")
