# -*- coding: utf-8 -*-
"""exercicio_4_B_AyrtonCossuol.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11E7Zd8Y4Bk3ja7uwyAgHvBE2iStFHyeV
"""

#Atividade 4 - B
import numpy as np
import matplotlib.pyplot as plt

def impulso(n0, sinal):
  imp = []

  for i in range(-2, 21):
    if i == n0:
      if sinal == 1:
        imp.append(1)
      else:
        imp.append(-1)
    else:
      imp.append(0)

  return imp

def soma_impulso(i_1, i_2):
  i_total = []

  j = 0
  for i in range(-2, 21):
    soma = i_1[j] + i_2[j]
    i_total.append(soma)
    j += 1

  return i_total

def degrau():
  u = []

  for i in range(-2, 21):
    u.append(1) if i >= 0 else u.append(0)

  return u

def main():
  n = np.linspace(-2, 20, 23)
  n_2 = np.linspace(-4, 40, 45)

  imp = impulso(0, 1)
  imp_2 = impulso(1, 0)

  h = soma_impulso(imp, imp_2)
  x = degrau()

  y = np.convolve(x, h)

  plt.figure(figsize=(12, 6))
  plt.stem(n, h, use_line_collection = True)
  plt.xlabel("[n]")
  plt.ylabel("h[n]")
  plt.title('Sinal h[n]')
  plt.show()

  plt.figure(figsize=(12, 6))
  plt.stem(n, x, use_line_collection = True)
  plt.xlabel("[n]")
  plt.ylabel("x[n]")
  plt.title('Sinal x[n]')
  plt.show()

  plt.figure(figsize=(12, 6))
  plt.stem(n_2, y, use_line_collection = True)
  plt.xlabel("[n]")
  plt.ylabel("y[n]")
  plt.title('Sinal y[n]')
  plt.show()

if __name__ == "__main__":
  main()