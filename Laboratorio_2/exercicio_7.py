# -*- coding: utf-8 -*-
"""exercicio_7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LfK1jYQbDAEhcMaHgEHyQxrPlzZSSlvw
"""

import numpy as np
import matplotlib.pyplot as plt

def degrau(n0):
    n = np.linspace(-2, 5, 8)
    y = []

    if n0 == - 1:
        for i in range(len(n)):
            if i == 1 or i > 1:
                y.append(1)
            else:
                y.append(0)

    elif n0 == 0:
        for i in range(len(n)):
            if i == 2 or i > 2:
                y.append(1)
            else:
                y.append(0)
    
    elif n0 == 1:
        for i in range(len(n)):
            if i == 3 or i > 3:
                y.append(1)
            else:
                y.append(0)
    
    plt.figure(figsize=(12, 6))
    plt.stem(n, y, use_line_collection = True)
    plt.xlabel("[n]")
    plt.ylabel("x[n]")
    plt.legend(["Função Degrau"])
    plt.show()
    

if __name__ == "__main__":
  print('Escolha o deslocamento: ')
  print('1 - x[n] = u[n-1]')
  print('2 - x[n] = u[n]')
  print('3 - x[n] = u[n+1]')
  valor = int(input('Valor: '))

  if valor == 1:
    d = -1
    degrau(d)

  elif valor == 2:
    d = 0
    degrau(d)

  elif valor == 3:
    d = 1
    degrau(d)

  else:
    print('Valor informado nao existe')
