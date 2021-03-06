# -*- coding: utf-8 -*-
"""exercicio_1_AyrtonCossuol.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hMH0kO5IbhYABBGnRHNjsAh2g8Q-HhXr
"""

#Atividade 1
import numpy as np
import matplotlib.pyplot as plt

#Função que gera o sinal x[n] proposto na atividade.
def sinal_x():
  x = []

  for i in range(-2, 5):
    if i == 0:
      x.append(0.5)
    
    elif i == 1:
      x.append(2)
    
    else:
      x.append(0)
  
  return x

#Função que gera o sinal h[n] proposto na atividade.
def sinal_h():
  h = []

  for i in range(-2, 5):
    h.append(1) if i >= 0 and i <= 2 else h.append(0)
  
  return h

#Função que faz a convolução entre dois sinais 
#OBS.: A função nao faz a convolução para deslocamento negativo (n-n0, tendo n0
#com o valor negativo)
def conv(x, h):
    P, Q, N = len(x), len(h), len(x) + len(h) - 1
    z = []
    for k in range(N):
        t, lower, upper = 0, max(0, k - (Q - 1)), min(P - 1, k)
        for i in range(lower, upper + 1):
            t = t + x[i] * h[k-i]
        z.append(t)
    
    return z

#Função main que faz a criação dos n's e dos sinais e tambem a chamada das 
#convoluções tanto criadas quanto a convolução do numpy junto dos plot dos 
#graficos
def main():
  n = np.linspace(-2, 5, 7, endpoint=False)
  n2 = np.linspace(-4, 9, 13, endpoint=False)
  
  x = sinal_x()
  h = sinal_h()

  c2 = conv(x, h)
  c = np.convolve(x, h)

  plt.figure(figsize=(12, 6))
  plt.stem(n, x, use_line_collection = True)
  plt.xlabel("[n]")
  plt.ylabel("x[n]")
  plt.title('Sinal x[n]')
  plt.show()

  plt.figure(figsize=(12, 6))
  plt.stem(n, h, use_line_collection = True)
  plt.xlabel("[n]")
  plt.ylabel("h[n]")
  plt.title('Sinal h[n]')
  plt.show()
  
  plt.figure(figsize=(12, 6))
  plt.stem(n2, c, use_line_collection = True)
  plt.xlabel("[n]")
  plt.ylabel("y1[n]")
  plt.title('Sinal y1[n] utilizando a funcao conv criada')
  plt.show()

  plt.figure(figsize=(12, 6))
  plt.stem(n2, c2, use_line_collection = True)
  plt.xlabel("[n]")
  plt.ylabel("y2[n]")
  plt.title('Sinal y2[n] utilizando a funcao np.convolve()')
  plt.show()

if __name__ == "__main__":
  main()

