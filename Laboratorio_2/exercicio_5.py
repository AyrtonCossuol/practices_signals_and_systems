# -*- coding: utf-8 -*-
"""exercicio_5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LfK1jYQbDAEhcMaHgEHyQxrPlzZSSlvw
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def plotar(w0n, n, title):
  
  plt.figure(figsize=(12, 6))
  plt.stem(n, w0n, use_line_collection=True)
  plt.title(title)
  plt.xlabel('[n]')
  plt.ylabel('y[n]')

  plt.show()

def deslocar(n0):
  n = np.linspace(0, 100, 150, endpoint=False)
  w0n = (np.pi/8) * n
  w0n = signal.sawtooth(w0n, width=0.5)

  plotar(w0n, n, title='Função triangular inicial sem o deslocamento.')

  n_2 = np.linspace((0 - n0), (100 - n0), 150, endpoint=False)
  w1n = (np.pi/8) * n_2
  w1n = signal.sawtooth(w1n, width=0.5)

  plotar(0.9 * w1n, n_2, title='Função triangular com o deslocamento determinado.')

  wfn = w0n + 0.9 * w1n
  plotar(wfn, n, title='Função triangular gerada aparti da soma.')


if __name__ == "__main__":
  n0 = int(input('Insira a quantidade de de deslocamento: '))

  deslocar(n0)

