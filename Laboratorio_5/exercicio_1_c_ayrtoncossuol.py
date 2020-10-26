# -*- coding: utf-8 -*-
"""exercicio_1_C_AyrtonCossuol.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1371vuzaujYWTWtZuTALqLbjSjNcx6Zda
"""

#Exercicio - 1, C
import numpy as np
import matplotlib.pyplot as plt
from numpy import pi
from numpy.fft import fft, ifft, fftfreq, fftshift

def cria_funcao(N, periodo):
  x = []
  cont_1 = 2
  cont_2 = 0
  for i in range(0, (periodo * N)):
    if cont_1 == 4 and cont_2 == 0:
      x.append(1)
      cont_1 = 1
      cont_2 = 1
    elif cont_1 == 4 and cont_2 == 1:
      x.append(-1)
      cont_1 = 1
      cont_2 = 0
    else:
      x.append(0)
      cont_1 += 1
  
  return x

def calculo_DTFS(x):
  return fft(x)/len(x)

def shift_sinal(X, w):
  return fftshift(X), fftshift(w)

def retorna_sinal(X, x):
  return np.real(ifft(X)*len(x))

def main():
  # criando o vetor de amostra com tamanho nper  periodos do sinal
  # periodo do sinal e quantidade de periodos em x[n]
  N, nper = 8, 3 
  n = np.arange(0, nper*N)

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
  phasX[ModX < 0.00001] = 0 #  cuidado com isso aqui, isso depende do previo conhecimento do sinal

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