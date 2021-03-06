# -*- coding: utf-8 -*-
"""exercicio_2_B_AyrtonCossuol.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FwOyhO10ytpCkbBIfeGf4WkqtnmUwM0I
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, ifft, fftfreq, fftshift

def cria_sinal(t):
  x = []

  for i in t:
    x.append(100 * np.cos(2 * np.pi * 100 * i) * np.exp(-100 * i)) if i >= 0 else x.append(0)

  return x

def main():
  L, Ts = 256, 1/1000
  t = np.arange(0, L, Ts)

  x2 = cria_sinal(t)

  X2 = Ts * fft(x2)

  w = fftfreq(len(X2), d=1.0) * (2 * np.pi)
  
  wdh = fftshift(w / (Ts * 2 * np.pi))
  X2_d = fftshift(X2)
  
  Mod_X2 = np.abs(X2_d)
  phas_X2 = np.angle(X2_d)

  phas_X2[Mod_X2 < 0.00001] = 0

  fig1, ax = plt.subplots(3, 1)
  ax[0].stem(t, x2, 'r-', use_line_collection = True)
  ax[0].set_title('x2[n]=x(nTs)')
  ax[0].set_ylabel("Amplitude")
  ax[0].set_xlabel("nTs [s]")
  ax[0].set_xlim(0, 0.04)
  ax[0].grid(True)

  ax[1].plot(wdh, Mod_X2, 'r-', linewidth=2)
  ax[1].set_title('|X2[k]|')
  ax[1].set_ylabel("Amplitude")
  ax[1].set_xlabel("[Hz]")
  ax[1].grid(True)

  ax[2].plot(wdh, phas_X2, 'r-', linewidth=2)
  ax[2].set_title('angle(X2[k])')
  ax[2].set_ylabel("Amplitude")
  ax[2].set_xlabel("[Hz]")
  ax[2].grid(True)

  fig1.tight_layout()
  plt.show()

if __name__ == "__main__":
  main()

