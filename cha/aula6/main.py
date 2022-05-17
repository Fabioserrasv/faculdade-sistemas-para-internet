class Fila:

  def __init__(self, max):
    self.max = max
    self.quantidade = 0
    self.l = [0] * max
    self.last = -1
    self.first_position = 0

  def enfileirar(self, value):
    if(self.quantidade == self.max):
      print('Cheio')
      return False
    if(self.quantidade+1 > self.max):
      self.l[0] = value
      self.last = -1
      return
    self.l[self.last+1] = value
    self.last = self.last+1
    self.quantidade = self.quantidade+1

  def desenfileirar(self):
    if(self.first_position+1 > self.max):
      self.first_position = 0
    self.first_position = self.first_position+1
    self.quantidade = self.quantidade-1

  def verInicio(self):
    print(self.l[self.first_position])
  
  def verFila(self):
    string = ''
    for i in self.l:
      string += str(i) + ','
    print(string)

sla = Fila(2)
sla.enfileirar(4)
sla.enfileirar(2)
sla.enfileirar(2)
sla.desenfileirar()
sla.verFila()
sla.verInicio()