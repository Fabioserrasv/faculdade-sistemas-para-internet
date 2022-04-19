# -*- coding: utf-8 -*-
import numpy as np 
import matplotlib.pyplot as plt

n = np.linspace(1,10,100)
labels = ['Constante','Logaritmico','Linear','nlog(n)', 'O(2^n)', 'O(n^2)', 'O(n^3)']
big_o = [np.ones(n.shape),np.log(n),n,np.multiply(np.log(n), n), 2**n, n**2, n**3]

plt.figure(figsize=(5,4))
plt.ylim(0,100)

for i in range(len(big_o)):
  plt.plot(n, big_o[i], label = labels[i])

plt.legend()
plt.ylabel('Tempo')
plt.xlabel('n')
plt.show()