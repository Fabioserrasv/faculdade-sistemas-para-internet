from utils import get_index_from_final_board

def manhattan(board):
  value = 0
  for board_row, row in enumerate(board):
    for board_col, cell in enumerate(row):
      if cell == 0:
        continue
      finalRow, finalCol = get_index_from_final_board(cell)
      value += abs(board_row - finalRow) + abs(board_col - finalCol)
  return value

def out_of_place(board):
  value = 0
  for board_row, row in enumerate(board):
    for board_col, cell in enumerate(row):
      if cell == 0:
        continue

      final_board_row, final_board_col = get_index_from_final_board(cell)
      d = abs(board_row - final_board_row) + abs(board_col - final_board_col)
      value += 0 if d == 0 else 1
  return value

def linear_conflict(board):
  distance = manhattan(board)
  for board_row, row in enumerate(board):
    for board_col, cell in enumerate(row):
      if cell != 0:
        finalRow, finalCol = get_index_from_final_board(cell)
        if board_row == finalRow:
          for k in range(board_col + 1, 3):
            k_final_row, k_final_col = get_index_from_final_board(board[board_row][k])
            if board[board_row][k] != 0 and k_final_row == board_row and cell > board[board_row][k]:
              distance += 2
        if board_col == finalCol:
          for k in range(board_row + 1, 3):
            k_final_row, k_final_col = get_index_from_final_board(board[k][board_col])
            if board[k][board_col] != 0 and k_final_col == board_col and cell > board[k][board_col]:
              distance += 2
  return distance

heuristics = {
  "manhattan": manhattan,
  "out_of_place": out_of_place,
  "linear_conflict": linear_conflict
}

