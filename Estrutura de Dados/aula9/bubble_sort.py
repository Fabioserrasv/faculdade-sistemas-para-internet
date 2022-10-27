def bubble_sort(_array):
  last_index = len(_array) - 1
  
  while 0 != last_index:
    index = 0
    while index < last_index:

      if _array[index] > _array[index + 1]:
        aux = _array[index]
        _array[index] = _array[index + 1]
        _array[index + 1] = aux

      
      index +=1
    last_index -= 1
    
  return _array