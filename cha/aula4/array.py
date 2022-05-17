import numpy as np
class VetorOrdenado:

  def __init__(self, max):
    self.max = max
    self.last = -1
    self.l = [0] * max
    self.l[0] = 1
    self.l[1] = 2
    self.last = 1

  def addValue(self, x):
    

  def getValues(self):
    if(len(self.l) == 0):
      return None
    for i in range(len(self.l)):
      print(self.l[i])


sla = VetorOrdenado(10)
sla.addValue(4)

#sla.getValues()