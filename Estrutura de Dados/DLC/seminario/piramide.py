
def get_value(row, element, triangle):
  value = 0
  prev_row = row - 1
  if prev_row >= 0:
    if element - 1 != -1:
      value += triangle[row - 1][element - 1]
    if element < row and element != -1:
      value += triangle[row - 1][element]
  else:
    return 1
  return value

def main(linhas):
  soma = 0
  triangle = []
  for row in range(linhas):
    elements = row+1
    triangle.append([0] * elements)
    if(elements == 1):
      triangle[0][0] = 1
    for e in range(elements):
      value = get_value(row, e, triangle)
      triangle[row][e] = value
      soma += value
  return soma
print(main(22))