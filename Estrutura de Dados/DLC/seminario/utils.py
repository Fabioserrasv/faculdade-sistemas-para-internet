import random
from config import FINAL_BOARD_MATRIX
from board import Board
FINAL_BOARD = Board(FINAL_BOARD_MATRIX, None)

def get_index_from_final_board(item: int):
  index = item - 1
  return index // 3, index % 3

def compare_board(b1, b2):
    if b1.get_value() == b2.get_value():
        return 0   
    return 1 if b1.get_value() > b2.get_value() else -1

def generate_initial_matrix(MOVEMENTS = 50):
  final_board = FINAL_BOARD
  BOARD_PASSED = [final_board]
  current_board = final_board

  movements = 0
  for _m in range(0, MOVEMENTS):      
    boards = [ board for board in current_board.get_possible_boards() if board not in BOARD_PASSED ]
    if len(boards) == 0:
      break

    board = random.choice(boards)
    BOARD_PASSED.append(board)
    current_board = board
    movements += 1
    
  print(f"Board gerado com {movements} movimentos")  
  return current_board.get_matrix()

def print_matrix(m):
    print("-=-=-=-")

    for row in m:
        print(" " + " ".join([str(col) for col in row]))
    print("-=-=-=-")