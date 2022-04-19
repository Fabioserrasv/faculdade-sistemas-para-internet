# -*- coding: utf-8 -*-
import numpy as np
##Ler dois números inteiros, executar e mostrar o resultado das seguintes operações: adição,
##subtração, multiplicação e divisão.
def um():
  x = int(input('Digite o valor 1'))
  y = int(input('Digite o valor 2'))
  print('Adição:' , (x + y) , '\nSubtração: ' , (x - y) , '\nMultiplicação: ' , (x*y) , '\nDivisão: ' , (x/y))

def dois():
  valorKm = 12
  tempo = float(input('Tempo da viagem (hora):\n'))
  velocidadeMedia = float(input('Velocidade Média (km/h)'))
  
  distanciaPercorrida = tempo * velocidadeMedia
  litrosGas = distanciaPercorrida/valorKm

  print('Velocidade Média: ' , velocidadeMedia  , '\nTempo Gasto: ' , tempo , '\nDistância Percorrida: ',distanciaPercorrida, '\nQuantidade de litros: ', litrosGas)

def tres():
  idade = int(input('Digite a Idade\n'))
  if(idade<0):
    print('Idade Inválida')
    return
  if(idade<=12):
    print('Criança')
    return
  if(idade<=17):
    print('Adolescente')
    return
  print('Adulto')
  
def quatro():
  n = int(input('Digite o número'))
  
  for i in range(1, 11):
    print(str(n)+' * '+str(i), str((i*n)))

def cinco():
  array = []
  for i in range(5):
    array.append(int(input('Digite um número:\n')))
  print(sum(array))

def seis():
  aluno = {}
  for i in range(3):
    aluno[i] = float(input('Digite a nota do aluno\n'))
  media = (aluno[0] + aluno[1] + aluno[2])/3
  print('Média: ', str(media))

def sete():
  matriz = np.array([[3, 4, 1], [3, 1, 5]])
  soma = 0
  for i in range(len(matriz)):
    soma += (sum(matriz[i]))
  print(soma)

class Aluno:
  def __init__(self, nome, notas):
    self.nome = nome
    self.notas = notas

  def calculaMedia(self):
    return np.mean(self.notas)
  
  def __str__(self):
    string = "Nome: ", str(self.nome), "\nNotas: ", str(self.notas[0]),' ', str(self.notas[1])
    return str(string)
  
  def getSituacao(self):
    if self.calculaMedia() >= 6:
      return 'Aprovado'
    return 'Reprovado'

aluno1 = Aluno('Pedro', [7,8])
aluno2 = Aluno('Gustavo', [1,8])

print('Aluno 1', str(aluno1) , 'Situacao: ', str(aluno1.getSituacao()), ' Media:', str(aluno1.calculaMedia()))
print('Aluno 2', str(aluno2) , 'Situacao: ', str(aluno2.getSituacao()), ' Media:', str(aluno2.calculaMedia()))
um()