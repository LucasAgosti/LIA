import numpy as np
import pandas as pd

uf = 5
days = 5

ufWeights = np.matrix([[10], [20], [50], [250], [10000]])

amostras = np.random.rand(uf, days)
print(amostras)
print("------------------------------------")
print(ufWeights)
newAmostras = np.multiply(amostras, ufWeights)

print("--------------------------------------\nTOTAL:\n")
print("Obs: Linhas = UF's\n\t Colunas = dias")
print(newAmostras.astype(int))
