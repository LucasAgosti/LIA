import numpy as np

CONST_LEARNING_RATE = 0.05

training = np.array([[1, 0, 0],
                    [1, 0, 1],
                    [1, 1, 0],
                    [1, 1, 1]])

yDesejada = np.array([0, 0, 0, 1])

bias = 0
w = np.array([bias, np.random.uniform(-1, 1), np.random.uniform(-1, 1)])
test = 1
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
        for x in range(4):
            print("Linha número: {}".format(x))

            u = sum(np.multiply(training[x], w))
            print("u = ", u)
            yAtual = predict(u)
            print("Saida desejada = ", yDesejada[x])
            print("Saida atual = ", yAtual)
            error = yDesejada[x] - yAtual

            if(error != 0):
                print("Houve erro")
                w[0] += CONST_LEARNING_RATE * error
                w[1] += CONST_LEARNING_RATE * error * training[x][1]
                w[2] += CONST_LEARNING_RATE * error * training[x][2]

            else:
                print("OK")
                count_acerto += 1
            print("W = ", w[0])

            if(count_acerto == 4):
                count_error = 0



        print()
        epochs += 1
        print("Epocas = ", epochs)


train()

print("Digite as duas entradas da porta AND")

x1 = float(input())
x2 = float(input())

print("O resultado e =", predict(np.dot(A, w)))
