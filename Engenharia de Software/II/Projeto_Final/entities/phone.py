class Phone:

  def __init__(self, number):
    self.__number = number

  def set_number(self, number: str):
    self.__number = number

  def get_number(self):
    return self.__number