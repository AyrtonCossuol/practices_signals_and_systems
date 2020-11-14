# -*- coding: utf-8 -*-
"""exercicio_2_C_AyrtonCossuol.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LOftT3KOxUJZ2Ahf6XJNiQLxUcul39ZJ
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, ifft, fftfreq, fftshift

def main():
  w = 350
  w_amp = 120 * w  # frequencia de amostragem
  tam = (2 * np.pi) / w_amp
  t = np.arange(-0.7, 0.7 + tam, tam)

  # Criando o sinal
  x = np.sin(w * t)

  # N - tamanho da DTFS
  N = np.power(2, 12)

  # calculando a FT
  X = (tam * N) * fft(x, N) / N

  #criando o vetor de frequencia
  w = fftfreq(len(X), d=(tam)) * (2 * np.pi)

  # Os indices de frequencia são mudados de 0 a N-1 para -N/2 + 1 a N/2
  # posicionando a freq. zero no meio do gráfico
  wd, Xd = fftshift(w), fftshift(X)

  # calculando o modulo e a fase
  ModX, phasX = np.abs(Xd), np.angle(Xd)

  fig, ax = plt.subplots(3, 1)
  # Representação da função no tempo
  ax[0].plot(t, x, 'c-', linewidth=2, label="")
  ax[0].set_ylabel("Amplitude")
  ax[0].set_xlabel("t")
  ax[0].set_xlim(-0.40, 0.40)
  ax[0].set_title('x(t)')
  ax[0].grid(True)

  # Representação do modulo da ft
  ax[1].plot(wd, ModX, 'r-',linewidth=2, label="")
  ax[1].set_ylabel("Amplitude")
  ax[1].set_xlabel("rad/s")
  ax[1].set_xlim(-450, 450)
  ax[1].set_title('|Xa(e^jw)|')
  ax[1].grid(True)

  # Representação do angulo da ft
  ax[2].stem(wd, phasX, 'r-', label="", use_line_collection=True)
  ax[2].set_ylabel("Amplitude")
  ax[2].set_xlabel("rad/s")
  ax[2].set_xlim(-450, 450)
  ax[2].set_title('angle(Xa(e^jw))')
  ax[2].grid(True)

  plt.tight_layout()
  plt.show()

if __name__ == '__main__':
    main()

