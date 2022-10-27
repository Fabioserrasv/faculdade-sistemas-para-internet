class No:
  def __init__(self, valor):
    self.valor = valor
    self.anterior = None
    self.proximo = None

  def getValue(self):
    return self.valor

  def setBefore(self, anterior):
    self.anterior = anterior

  def getBefore(self):
    return self.anterior  

  def setNext(self, proximo):
    self.proximo = proximo

  def getNext(self):
    return self.proximo    

  def __str__(self):
    if not self.proximo:
      return str(self.valor)
    return f"{self.valor},{self.proximo}"

class FilaEncadeada:
  def __init__(self):
    self.first = None
    self.last = None

  def add(self, value):
    novoNo = No(value)
    if(self.first == None):
      self.first = novoNo
      self.last = novoNo
      return
    if(self.last == None):
      self.first.setNext(novoNo)
    novoNo.setBefore(self.last)
    self.last.setNext(novoNo)
    self.last = novoNo

  def addFirst(self, value):
    novoNo = No(value)
    if(self.first == None):
      self.first = novoNo
      self.last = novoNo
      return
    self.first.setBefore(novoNo)
    novoNo.setNext(self.first)
    self.first = novoNo

  def vazio(self):
    if(self.first == None):
      return True
    return False

  def deleteFirst(self):
    if (self.first == None):
      return
    newFirst = self.first.getNext()
    newFirst.setBefore(None)
    self.first = newFirst

  def search(self, value, parent = False):
    if not self.first:
      return
    toFind = self.first
    if(toFind.getValue() == value):
      if parent:
        return None, toFind
      return toFind
    while toFind.getNext():
      if(toFind.getNext().getValue() == value):
        if parent:
          return (toFind, toFind.getNext())
        return toFind.getNext()
      toFind = toFind.getNext()
    print("Não tem.")
    return None, None
  
  def delete(self, value):
    if not self.first:
      return
    parent, child = self.search(value, True)
    if parent:
      if child.getNext():
        child.getNext().setBefore(parent)
      parent.setNext(child.getNext())
      return
    self.deleteFirst()

  def __iter__(self):
    no = self.first
    while no:
      yield no
      no = no.getNext()

  def __str__(self):
    if not self.first:
      return "[]"
    return f"[{self.first}]"

lista = FilaEncadeada()
lista.add(1)
lista.add(2)
lista.add(3)
lista.add(4)
lista.add(5)


lista.delete(5)
lista.delete(10)

print(lista.search(2))

# for i in lista:
#   print(i.getValue())

# print(lista)