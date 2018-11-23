import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

UFS = 27
months = 12
pesosAno = np.array([1.7, 1.2, 1, 1, 1, 1, 1.3, 1, 1, 1.2, 1.7, 2])


empresas = []


def criaEmpresa(produtos):

    mean = np.matrix([100, 150, 500]*9)
    '''mean = np.matrix([100, 150, 500, 500,
                         500, 500, 500, 800,
                        800, 1000, 1000, 1000,
                         1000, 2000, 2000, 10000])'''

    mean = mean.T
    #print(mean)

    mean2 = np.random.random((produtos, UFS, months))

    #print("NOVOS VALORES:\n", mean2)
    #print()

    amostras = np.ones((produtos, UFS, months))

    for i in range(UFS):
        for j in range(produtos):
            amostras[j][i] = amostras[j][i] * float(mean[i])
            amostras[j][i] = np.multiply(amostras[j][i], pesosAno)

    amostras = np.multiply(amostras, 1 - mean2 / 2)
    amostras = amostras.astype(int)
    print("AMOSTRAS:\n", amostras)
    print()
    #print(amostras.shape)

    plt.ylim(0, 200)

    for i in range(produtos):
        plt.plot(amostras[i, 0, :])

    #plt.show()

    return amostras


empresas.append(criaEmpresa(2))
empresas.append(criaEmpresa(3))
empresas.append(criaEmpresa(1))
empresas.append(criaEmpresa(1))

print(empresas)

