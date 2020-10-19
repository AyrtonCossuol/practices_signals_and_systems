# -*- coding: utf-8 -*-
"""exercicio_5_B_AyrtonCossuol.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BRaYDthRlrFi_O-PrVump_FoVbS0lIUO
"""

#Atividade 5 - B
import numpy as np
import matplotlib.pyplot as plt

def trem_impulso():
  imp = []

  for i in range(-4, 5):
    imp.append(1) if i == -4 or i == -2 or i == 0 or i == 2 or i == 4 else imp.append(0)

  return imp

def pulso_triangulo():
  t = []

  for i in range(-2, 3):
    if i == -1:
      t.append(0)
    elif i == 0:
      t.append(1)
    elif i == 1:
      t.append(0)
    else:
      t.append(0)

  return t

def main():
  n = np.linspace(-4, 4, 9)
  n_2 = np.linspace(-2, 2, 5)
  n_3 = np.linspace(-6, 6, 13)

  x = trem_impulso()
  h = pulso_triangulo()

  y = np.convolve(x, h) 

  plt.figure(figsize=(12, 6))
  plt.stem(n, x, use_line_collection = True)
  plt.xlabel("[n]")
  plt.ylabel("x[n]")
  plt.title('Sinal x[n] para T = 2')
  plt.show()

  plt.figure(figsize=(12, 6))
  plt.plot(n_2, h)
  plt.xlabel("[n]")
  plt.ylabel("h[n]")
  plt.title('Sinal h[n]')
  plt.show()

  plt.figure(figsize=(12, 6))
  plt.plot(n_3, y)
  plt.xlabel("[n]")
  plt.ylabel("y[n]")
  plt.title('Sinal y[n]')
  plt.show()

if __name__ == "__main__":
  main()
