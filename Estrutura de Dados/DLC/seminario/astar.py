from ordened_vector import OrderedVector
from utils import compare_board, FINAL_BOARD
import timeit

def a_star_8_puzzle(board):
  start = timeit.default_timer()
  visited_boards = []
  v = OrderedVector(10000, compare_board)
  v.insert(board)
  while len(v) > 0:
    current_board = v.pop(0)
    visited_boards.append(current_board)

    if current_board == FINAL_BOARD:
      break
    
    possibilities = current_board.get_possible_boards();

    for b in possibilities:
      if b not in visited_boards:
        v.insert(b)

  if current_board != FINAL_BOARD:
    return None

  path = current_board.path()
  end = timeit.default_timer()
  return path, len(path), (end - start)
  