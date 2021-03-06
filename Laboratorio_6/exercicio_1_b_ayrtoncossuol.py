# -*- coding: utf-8 -*-
"""exercicio_1_B_AyrtonCossuol.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1u4-Lwc12-k7XiPNEIfhz5Ft9D4cLSY1g
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy import pi
from numpy.fft import fft, ifft, fftfreq, fftshift
import scipy as sc
from scipy import signal

# Função para criar o sinal quadrado
def square(wt, duty = 0.5):
    sq = sc.signal.square(wt, duty=duty )
    return sq

def main():
  # definindo o sinal continuo periódico
  fs = 1              # freq. do sinal periódico
  w0 = 2*pi*fs        # frequencia angular
  Ts = 1/fs           # período fundamental do sinal
  Tam = 1/(100*fs)   	# período de amostragem 100 vezes menor que o período do sinal

  # quantidade de periodos no vetor do sinal
  Np = 4          
  # Criando o vetor de tempo,5 períodos, e intervalo de Tam
  t = np.arange(0,Ts*Np,Tam)
  
  # criando x(t)
  s = 0.5 * square(w0*t,duty = 0.25) + 0.5

  # Calculando a FS
  X = (fft(s)/len(s))

  # #criando o vetor de frequencia
  w = fftfreq(len(t), d=(1/Ts)*Tam)

  ##########################################################################################
  ##########################################################################################
  #Letra - B - i
  # Valor do Rc passado no exercicio
  RC = 0.01
  # Criação do sinal H(jw)
  H = (1/RC)/((1/RC) + 1j*w)

  # Geração do sinal Y(t)
  Y = X * H

  # Deslocamento dos sinais
  Yd = fftshift(Y)
  wd = fftshift(w)

  # Criando o sinal do modulo e do angulo
  ModY = np.abs(Yd)
  phaseY = np.angle(Yd)

  # Tratamento da fase
  phaseY[ModY < 0.00001] = 0

  # retornando o sinal ao dominio do tempo e ainda ignorando os erros 
  # de arrendondamento do FS
  y = np.real(ifft(Y)*len(s))

  plt.figure(figsize=(12, 8))
  plt.stem(wd, ModY, use_line_collection=True)
  plt.title('Representação |Y(t)| com RC=0.01s')
  plt.xlabel('t')
  plt.ylabel('|Y(t)|')
  plt.grid(True)
  plt.show()

  plt.figure(figsize=(12, 8))
  plt.stem(wd, phaseY, use_line_collection=True)
  plt.title('Representação angle(Y(t)) com RC=0.01s')
  plt.xlabel('t')
  plt.ylabel('angle(Y(t))')
  plt.grid(True)
  plt.show()

  plt.figure(figsize=(12, 8))
  plt.plot(t, y)
  plt.title('Representação do sinal y(t) com RC=0.01s')
  plt.xlabel('t')
  plt.ylabel('y(t)')
  plt.grid(True)
  plt.show()

  ##########################################################################################
  ##########################################################################################
  #Letra - B - ii
  RC = 0.1
  H = (1/RC)/((1/RC) + 1j*w)

  Y = X * H

  Yd = fftshift(Y)
  wd = fftshift(w)

  ModY = np.abs(Yd)
  phaseY = np.angle(Yd)

  phaseY[ModY < 0.00001] = 0

  y = np.real(ifft(Y)*len(s))

  plt.figure(figsize=(12, 8))
  plt.stem(wd, ModY, use_line_collection=True)
  plt.title('Representação |Y(t)| com RC=0.1s')
  plt.xlabel('t')
  plt.ylabel('|Y(t)|')
  plt.grid(True)
  plt.show()

  plt.figure(figsize=(12, 8))
  plt.stem(wd, phaseY, use_line_collection=True)
  plt.title('Representação angle(Y(t)) com RC=0.1s')
  plt.xlabel('t')
  plt.ylabel('angle(Y(t))')
  plt.grid(True)
  plt.show()

  plt.figure(figsize=(12, 8))
  plt.plot(t, y)
  plt.title('Representação do sinal y(t) com RC=0.1s')
  plt.xlabel('t')
  plt.ylabel('y(t)')
  plt.grid(True)
  plt.show()

  ##########################################################################################
  ##########################################################################################
  #Letra - B - iii
  RC = 1
  H = (1/RC)/((1/RC) + 1j*w)

  Y = X * H

  Yd = fftshift(Y)
  wd = fftshift(w)

  ModY = np.abs(Yd)
  phaseY = np.angle(Yd)

  phaseY[ModY < 0.00001] = 0

  y = np.real(ifft(Y)*len(s))

  plt.figure(figsize=(12, 8))
  plt.stem(wd, ModY, use_line_collection=True)
  plt.title('Representação |Y(t)| com RC=1s')
  plt.xlabel('t')
  plt.ylabel('|Y(t)|')
  plt.grid(True)
  plt.show()

  plt.figure(figsize=(12, 8))
  plt.stem(wd, phaseY, use_line_collection=True)
  plt.title('Representação angle(Y(t)) com RC=1s')
  plt.xlabel('t')
  plt.ylabel('angle(Y(t))')
  plt.grid(True)
  plt.show()

  plt.figure(figsize=(12, 8))
  plt.plot(t, y)
  plt.title('Representação do sinal y(t) com RC=1s')
  plt.xlabel('t')
  plt.ylabel('y(t)')
  plt.grid(True)
  plt.show()

if __name__ == "__main__":
  main()

