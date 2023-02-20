import numpy as np
import matplotlib.pyplot as plt

a = int(input("Entera:"))
b = int(input("Enterb:"))
c = int(input("Enterc:"))

def funkcija_parametri():
  x = np.arange(1, 21)
  x = np.linspace(-10, 10, 1000)
  y = a * x **2 + b * x + c 
  plt.title("Line graph")
  plt.xlabel("X axis")
  plt.ylabel("Y axis")
  plt.plot(x, y, color ="red")
  plt.show()
funkcija_parametri()