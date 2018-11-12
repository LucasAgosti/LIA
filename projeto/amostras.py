import numpy as np
import pandas as pd

cities = 16
days = 21

Weights = np.matrix([2000, 500, 500, 500, #MG
                    10000, 1000, 1000, 800, #SP
                    2000, 500, 350, 250, #BA
                    2000, 400, 350, 280]) #PR
Weights = Weights.T
amostras = np.random.rand(cities, days)
print("AMOSTRAS:\n", amostras)
print("------------------------------------------")
print("PESOS:\n", Weights)
newAmostras = np.multiply(amostras, Weights)

print("--------------------------------------\nTOTAL:\n")
print("Obs: Linhas = UF's\n\t Colunas = dias\n")
print(newAmostras.astype(int))
newAmostras = newAmostras.astype(int)

data = pd.DataFrame(newAmostras, columns=['DIA 1','DIA 2','DIA 3', "DIA 4", "DIA 5", "DIA 6", "DIA 7", "DIA 8", "DIA 9", "DIA 10",
                                          "DIA 11", "DIA 12", "DIA 13", "DIA 14", "DIA 15", "DIA 16", "DIA 17", "DIA 18", "DIA 19", "DIA 20", "DIA 21"])

print("--------------------------------------\nDATAFRAME:\n")
print(data)

data.to_csv("AMOSTRAS", sep='\t', encoding='utf-8')
