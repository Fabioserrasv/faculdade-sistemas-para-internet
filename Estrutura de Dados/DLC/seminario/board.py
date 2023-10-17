import copy

DIRECTIONS = [
  (1, 0),
  (-1, 0),
  (0, 1),
  (0, -1)
]

class Board:
  def __init__(self, matrix, parent, heuristic = None):
    self.__value = 0
    self.__heuristic = heuristic
    if heuristic is not None:
      self.__value = heuristic(matrix)
      self.__heuristic = heuristic
    self.__matrix = matrix
    self.__parent = parent
    self.visited = False
  
  def get_matrix(self):
    return self.__matrix
  
  def get_heuristic(self):
    return self.__heuristic

  def get_value(self):
    return self.__value
  
  def get_parent(self):
    return self.__parent 

  def get_possible_boards(self):
    possibilities = []
    positionRow = None
    positionCol = None

    for rowIndex, row in enumerate(self.__matrix):
      for colIndex, cell in enumerate(row):
        if cell == 0:
          positionRow, positionCol = rowIndex, colIndex
          break

      if (positionRow is not None):
        break
    
    for rowMove, colMove in DIRECTIONS:
      newRow = positionRow + (rowMove)
      newCol = positionCol + (colMove)

      if newRow >= 3 or newRow < 0:
        continue
        
      if newCol >= 3 or newCol < 0:
        continue

      new_matrix = copy.deepcopy(self.__matrix)
      
      aux = new_matrix[positionRow][positionCol]
      new_matrix[positionRow][positionCol] = new_matrix[newRow][newCol]
      new_matrix[newRow][newCol] = aux

      new_possibility_board = Board(new_matrix, self, self.__heuristic) 
      possibilities.append(new_possibility_board)
    return possibilities
  
  def path(self):
    result = []
    if self.__parent is not None:
      result = self.__parent.path()
    result.append(self.__matrix)
    return result

  def __eq__(self, board):
    if not isinstance(board, Board):
      return False

    return self.get_matrix() == board.get_matrix()