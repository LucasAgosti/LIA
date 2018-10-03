import numpy as np
import matplotlib.pyplot as plt

CONST_LEARNING_RATE = 0.05

training = np.array([[2.7810836	,   2.550537003	,   1],
                    [1.465489372,	2.362125076	,   1],
                    [3.396561688,	4.400293529	,   1],
                    [1.38807019	,	1.850220317	,   1],
                    [3.06407232	,	3.005305973	,   1],
                    [7.627531214,	2.759262235	,   1],
                    [5.332441248,	2.088626775	,   1],
                    [6.922596716,	1.77106367	,   1],
                    [8.675418651,	-0.242068655,   1],
                    [7.673756466,	3.508563011	,	1]])

yDesejada = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])

[tamLinha, tamColuna] = np.shape(training)
print("Tamanho da matriz = ", [tamLinha, tamColuna])
bias = 0

w = np.random.rand(tamColuna)
w[-1] = bias

print("Os pesos iniciais são: ", w)

def predict(u):
    if u >= 0.0:
        return 1
    else:
        return 0

def train():

    epochs = 0
    count_error = 1

    while count_error == 1:

        count_acerto = 0
        for x in range(tamLinha):
            print("Linha número: {}".format(x))
            #print("Treino: ", training[x])
            #print("Pesos = ", w)
            u = sum(np.multiply(training[x], w))

            print("u = ", u)
            yAtual = predict(u)
            print("Saida desejada = ", yDesejada[x])
            print("Saida atual = ", yAtual)
            error = yDesejada[x] - yAtual

            if(error != 0):
                print("Houve erro")
                for y in range(tamColuna - 1):
                    w[y] += CONST_LEARNING_RATE * error * training[x][y]
                    print("W = ", w[y])

            else:
                print("OK")
                count_acerto += 1

            if(count_acerto == tamLinha):
                count_error = 0
        print()
        epochs += 1
        print("Epocas = ", epochs)

train()
print()

def test(I, J):
    print("TESTANDO")
    uTest = [I, J, bias]

    print("Com o teste: ", predict(sum(np.multiply(uTest, w))))

test(2.1, 2.4)
test(6.4, 2.77106367)

plt.scatter(training[:, 0], training[:, 1], c=yDesejada)
plt.title("Setosa x versicolor")
plt.xlabel('Sepal.Width')
plt.ylabel('Sepal.Length')
plt.show()
