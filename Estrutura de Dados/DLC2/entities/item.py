class Item:
  def __init__(self, name, value, volume) -> None:
    self.__name = name
    self.__value = value
    self.__volume = volume

  def get_value(self):
    return self.__value
  
  def get_volume(self):
    return self.__volume
