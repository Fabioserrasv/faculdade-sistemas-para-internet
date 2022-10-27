from array import array
import numpy as np

def sla():
  vetor = [10,11,12]
  print(vetor)
  print(vetor[2])

def sla2():
  vetor2 = array('i', [10,11,12])
  print(vetor2)
  print(vetor2[2])

def sla3():
  vetor3 = np.array([10,11,12])
  print(vetor3)
  print(vetor3[2])

import numpy as np
class VetorNaoOrdenado:

  def __init__(self, max):
    self.max = max
    self.last = -1
    self.l = np.array([])

  def addValue(self, x):
    if(len(self.l) == self.max):
      print('Cheio.')
      return False
    self.l = np.append(self.l, x)
    self.last = self.last+1
    if(self.last+1 == self.max):
      print('Encheu')

  def getValues(self):
    if(len(self.l) == 0):
      return None
    for i in range(len(self.l)):
      print(self.l[i])  
  
  def getLastIndex(self):
    return self.last

sla = VetorNaoOrdenado(2)
sla.addValue(727)
sla.addValue(123)
sla.getValues();
print(sla.getLastIndex())

sla.addValue(2)

# teste = np.array(0)
# teste = np.append(teste, 12)
# print(teste)

  

















