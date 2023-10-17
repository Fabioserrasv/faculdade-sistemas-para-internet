from heuristics import manhattan, out_of_place
from board import Board
from utils import generate_initial_matrix
from astar import a_star_8_puzzle
import sys

sys.setrecursionlimit(2000)

heuristic = out_of_place
# heuristic = manhattan


def main(board):
  pass

initial_matrix = generate_initial_matrix(MOVEMENTS=1000)

initial_matrix = [[7, 2, 4],
              [6, 5, 3],
              [8, 1, 0]]

initial_board = Board(
  initial_matrix
, None, heuristic)

a_star_8_puzzle(initial_board)
print(initial_matrix)
# print(get_possible_boards(input))
