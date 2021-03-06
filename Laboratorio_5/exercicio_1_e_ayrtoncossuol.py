# -*- coding: utf-8 -*-
"""exercicio_1_E_AyrtonCossuol.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1371vuzaujYWTWtZuTALqLbjSjNcx6Zda
"""

#Exercicio - 1, E
import numpy as np
import matplotlib.pyplot as plt
from numpy import pi
from numpy.fft import fft, ifft, fftfreq, fftshift

def cria_funcao(N, periodo):
  x = []
  cont = 0
  for i in range(0, ((periodo * N))):
    if cont >= 1 and cont <= 4:
      x.append(1)
      cont += 1
    elif cont >= 5 and cont <= 8:
      x.append(-1)
      cont += 1
    else:
      x.append(0)
      cont = 1
  
  return x

def calculo_DTFS(x):
  return fft(x)/len(x)

def shift_sinal(X, w):
  return fftshift(X), fftshift(w)

def retorna_sinal(X, x):
  return np.real(ifft(X)*len(x))

def main():
  # criando o vetor de amostra com tamanho nper  periodos do sinal
  # periodo do sinal e a quantidade de periodos em x[n]
  N, nper = 9, 2
  n = np.arange(0, nper * N)

  #criando o vetor do sinal x[n]
  x = cria_funcao(N, nper)

  # calculando a DTFS
  X = calculo_DTFS(x)

  #criando o vetor de frequencia
  w = fftfreq(len(n), d=1/N)

  # Os indices de frequencia são mudados de 0 a N-1 para -N/2 + 1 a N/2
  # posicionando a freq. zero no meio do gráfico
  Xd, w = shift_sinal(X, w)

  # calculando o modulo - magnitude do espectro e calculando a fase do espectro
  ModX, phasX = np.abs(Xd), np.angle(Xd)

  # devido a erros de arredondamentos numericos da fft devemos filtrar os sinais muito pequenos!
  # cuidado com isso aqui, isso depende do previo conhecimento do sinal
  phasX[ModX < 0.00001] = 0 

  plt.figure(figsize=(12, 8))
  plt.stem(w, ModX, use_line_collection=True)
  plt.title('|X[n]|')
  plt.ylabel('Amplitude')
  plt.xlabel('k')
  plt.show()

  plt.figure(figsize=(12, 8))
  plt.stem(w, phasX, use_line_collection=True)
  plt.title('Angulo (X[n])')
  plt.ylabel('Amplitude')
  plt.xlabel('k')
  plt.show()

if __name__ == "__main__":
  main()

