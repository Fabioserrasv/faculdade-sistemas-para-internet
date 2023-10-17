from utils import get_index_from_final_board

def manhattan(board):
  value = 0
  for rowIndex, row in enumerate(board):
    for colIndex, cell in enumerate(row):
      if cell == 0:
        continue
      finalRow, finalCol = get_index_from_final_board(cell)
      value += abs(rowIndex - finalRow) + abs(colIndex - finalCol)
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
  # Calcula a heurística de Distância Linear Conflict
  distance = manhattan(board)
  for i in range(3):
    for j in range(3):
      if board[i][j] != 0:
        finalRow, finalCol = get_index_from_final_board(board[i][j])
        print(board[i][j])
        if i == finalRow:
          for k in range(j + 1, 3):
            if board[i][k] != 0 and divmod(board[i][k] - 1, 3)[0] == i and board[i][j] > board[i][k]:
              distance += 2  # Conflito linear
        if j == finalCol:
          for k in range(i + 1, 3):
            if board[k][j] != 0 and divmod(board[k][j] - 1, 3)[1] == j and board[i][j] > board[k][j]:
              distance += 2  # Conflito linear
  return distance

heuristics = {
  "manhattan": manhattan,
  "out_of_place": out_of_place,
  "linear_conflict": linear_conflict
}

