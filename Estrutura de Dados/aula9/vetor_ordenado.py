import numpy as np

class VetorOrdenado:
  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.ultima_posicao = -1
    self.valores = np.empty(self.capacidade, dtype=int)

  def imprime(self):
    if self.ultima_posicao == -1:
      print("Vetor vazio!")
    else:
      for i in range(self.ultima_posicao + 1):
        print(f'[{i}] - {self.valores[i]}')

  # O(n)
  def insere(self, valor):
    # Verifica se o vetor esta cheio
    if self.ultima_posicao == self.capacidade - 1:
      print('Capacidade maxima atingida')
      return

    # Encontra a posicao onde devera ser feita a insercao
    posicao = 0
    for i in range(self.ultima_posicao + 1):
      posicao = i
      # Compara cada posicao com o valor a ser inserido 
      if self.valores[i] > valor:
        # Se o valor for maior, termina o laco
        break
      # Caso especial para a ultima posicao
      if i == self.ultima_posicao:
        posicao = i + 1

    # Faz o remanejamento das posicoes 
    x = self.ultima_posicao
    while x >= posicao:
      self.valores[x + 1] = self.valores[x]
      x -= 1

    # Faz a insercao do novo valor na posicao correta
    self.valores[posicao] = valor
    self.ultima_posicao += 1

  # O(n)
  def pesquisa_linear(self, valor):
    for i in range(self.ultima_posicao + 1):
      # Se o valor for maior a pesquisa retorna -1
      if self.valores[i] > valor:
        return -1
      # Situacao em que encontra o valor no vetor
      if self.valores[i] == valor:
        return i
      # Caso especial para a ultima posicao
      if i == self.ultima_posicao:
        return -1

  # O(n)
  # Mesma logica da funcao excluir dos vetores nao ordenados.
  # Nesse caso, a pesquisa e otimizada.
  def excluir(self, valor):
    posicao = self.pesquisar(valor)
    if posicao == -1:
      return -1
    else:
      # Faz o remanejamento dos valores, decrementando a ultima posicao
      for i in range(posicao, self.ultima_posicao):
        self.valores[i] = self.valores[i + 1]
      
      self.ultima_posicao -= 1

  def pesquisa_binaria(self, valor):
    limite_inferior = 0
    limite_superior = self.ultima_posicao
    
    while True:
      posicao_atual = int((limite_inferior + limite_superior) / 2)
      if self.valores[posicao_atual] == valor:
        return posicao_atual              
      elif limite_inferior > limite_superior:
        return -1
      else:
        if self.valores[posicao_atual] < valor:
          limite_inferior = posicao_atual + 1
        else:
          limite_superior = posicao_atual - 1