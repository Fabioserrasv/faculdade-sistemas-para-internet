class ItemException(Exception):
  pass

class Item:
  def __init__(self, value:float, description:str):
    self.__validate_value(value)
    self.__value = value
    self.__description = description

  def set_value(self, value: float):
    self.__validate_value(value)
    self.__value = value

  def set_description(self, description: str):
    self.__description = description

  def get_value(self) -> float:
    return self.__value
  
  def get_description(self) -> str:
    return self.__description
  
  def __validate_value(self, value):
    if value <= 0: 
      raise ItemException('The Equipment value has to higher than zero.') 