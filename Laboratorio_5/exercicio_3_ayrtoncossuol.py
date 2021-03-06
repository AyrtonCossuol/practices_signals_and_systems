# -*- coding: utf-8 -*-
"""exercicio_3_AyrtonCossuol.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1371vuzaujYWTWtZuTALqLbjSjNcx6Zda
"""

#Atividade 3
import numpy as np
import matplotlib.pyplot as plt
from numpy import pi
from scipy import signal 
from numpy.fft import fft, ifft, fftfreq, fftshift

def cria_sinal(t):
  return signal.sawtooth(1.3 * np.pi * t)*0.75 + 0.25

def calculo_DTFS(x):
  return fft(x)/len(x)

def shift_sinal(X, w):
  return fftshift(X), fftshift(w)

def retorna_sinal(X, x):
  return np.real(ifft(X)*len(x))

def main():
  # definindo o sinal continuo periódico
  fs = 1            # freq. do sinal periódico
  w0 = 2 * pi * fs  # frequencia angular
  Ts = 1/fs         # período fundamental do sinal
  Tam = Ts/100   	  # período de amostragem 100 vezes menor que o período do sinal

  # Criando o vetor de tempo,5 períodos, e intervalo de Tam
  t = np.arange(0, Ts, Tam)

  #criando o vetor do sinal x[n]
  x = cria_sinal(t)

  # calculando a DTFS
  X = calculo_DTFS(x)

  #criando o vetor de frequencia
  w = fftfreq(len(t), d=1/Ts)

  # Os indices de frequencia são mudados de 0 a N-1 para -N/2 + 1 a N/2
  # posicionando a freq. zero no meio do gráfico
  Xd, w = shift_sinal(X, w)

  # calculando o modulo - magnitude do espectro e calculando a fase do espectro
  ModX, phasX = np.abs(Xd), np.angle(Xd)

  # devido a erros de arredondamentos numericos da fft devemos filtrar os sinais muito pequenos!
  # cuidado com isso aqui, isso depende do previo conhecimento do sinal
  phasX[ModX < 0.00001] = 0 

  # retornando o sinal ao dominio do tempo e ainda ignorando os erros 
  # de arrendondamento do fft e ifft
  xr = retorna_sinal(X, x)

  plt.figure(figsize=(12, 8))
  plt.stem(w, ModX, use_line_collection=True)
  plt.title('|X[k]|')
  plt.xlabel('k')
  plt.ylabel('Amplitude')
  plt.show()

  plt.figure(figsize=(12, 8))
  plt.stem(w, phasX, use_line_collection=True)
  plt.title('angle(X[k])')
  plt.xlabel('k')
  plt.ylabel('Amplitude')
  plt.show()

if __name__ == "__main__":
  main()

