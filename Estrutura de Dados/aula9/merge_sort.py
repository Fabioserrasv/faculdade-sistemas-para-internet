import numpy as np

def merge_sort(vetor):
  # Separa os elementos do vetor , usando chamada recursiva
  if len(vetor) > 1:
    divisao = len(vetor) // 2
    esquerda = vetor[:divisao].copy()
    direita = vetor[divisao:].copy()

    merge_sort(esquerda)
    merge_sort(direita)

    i = j = k = 0

    while i < len(esquerda) and j < len(direita):
      if esquerda[i] < direita[j]:
        vetor[k] = esquerda[i]
        i += 1
      else:
        vetor[k] = direita[j]
        j += 1
      k += 1

    while i < len(esquerda):
      vetor[k] = esquerda[i]
      i += 1
      k += 1
    while j < len(direita):
      vetor[k] = direita[j]
      j += 1
      k += 1
    return vetor