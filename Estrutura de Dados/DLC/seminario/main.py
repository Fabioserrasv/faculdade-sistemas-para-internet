import copy
FINAL_BOARD = [
  [1,2,3],
  [4,5,6],
  [7,8,0]
]

def get_index_from_final_board(item: int):
  index = item - 1
  return index // 3, index % 3

def manhattan(board1):
  value = 0
  for rowIndex, row in enumerate(board1):
    for colIndex, cell in enumerate(row):
      if cell == 0:
        continue
      
      finalRow, finalCol = get_index_from_final_board(cell)

      value += abs(rowIndex - finalRow) + abs(colIndex - finalCol)
  return value
      

DIRECTIONS = [
  (1, 0),
  (-1, 0),
  (0, 1),
  (0, -1)
]  

def get_possible_boards(board):
  possibilities = []
  positionRow = None
  positionCol = None

  for rowIndex, row in enumerate(board):
    for colIndex, cell in enumerate(row):
      if cell == 0:
        positionRow, positionCol = rowIndex, colIndex
        break

    if (positionRow is not None):
      break
  # print(positionCol)
  for rowMove, colMove in DIRECTIONS:
    newRow = positionRow + (rowMove)
    newCol = positionCol + (colMove)

    if newRow >= len(FINAL_BOARD) or newRow < 0:
      continue
      
    if newCol >= len(FINAL_BOARD[0]) or newCol < 0:
      continue

    new_board = copy.deepcopy(board)
    
    aux = new_board[positionRow][positionCol]
    new_board[positionRow][positionCol] = new_board[newRow][newCol]
    new_board[newRow][newCol] = aux
    possibilities.append(new_board)
  return possibilities

def get_best_board(board):
  possibilities = get_possible_boards(board)
  best = None
  best_value = 0
  for current_board in possibilities:
    if best is None:
      best = current_board
      continue
    c_value = manhattan(current_board)
    if best_value > c_value:
      best_value = c_value
      best = current_board
  return best

def main(board):
  current_board = board

  while manhattan(current_board) != 0:
    current_board = get_best_board(current_board)
    print(current_board)

input = [
  [2,0,1],
  [4,6,5],
  [3,7,8]
]

main(input)
# print(get_possible_boards(input))
