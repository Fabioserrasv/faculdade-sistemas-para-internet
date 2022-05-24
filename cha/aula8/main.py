class No:
  def __init__(self, valor):
    self.valor = valor
    self.proximo = None

  def getValue(self):
    return self.valor

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
    self.last.setNext(novoNo)
    self.last = novoNo

  def addFirst(self, value):
    novoNo = No(value)
    if(self.first == None):
      self.first = novoNo
      self.last = novoNo
      return
    novoNo.setNext(self.first)
    self.first = novoNo

  def vazio(self):
    if(self.first == None):
      return True
    return False

  def addLast(self, value):
    if(self.last != None):
      novoNo = No(value)
      self.last.setNext(novoNo)
      self.last = novoNo
    return False

  def deleteFirst(self):
    if (self.first == None):
      return
    newFirst = self.first.getNext()
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
lista.add("""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  
</body>
</html>
""")

lista.delete(6)
lista.delete(5)
lista.delete(10)

for i in lista:
  print(i.getValue())

print(lista)