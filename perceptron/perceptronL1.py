import numpy as np

CONST_LEARNING_RATE = 0.005

training = ([1, 0, 0],
            [1, 0, 1],
            [1, 1, 0],
            [1, 1, 1])

yDesejada = np.array([0, 0, 0, 1])

bias = 1
w = [bias, np.random.uniform(-1, 1), np.random.uniform(-1, 1)]
#w = [bias, 0.2, 0.1]
test = 1
print("Os pesos iniciais são: ", w)

def predict(u):
    if u >= 0.0:
        return 1
    else:
        return 0

def train(bias, w):

    count_error = 1
    epochs = 0
    while count_error == 1:
        error = 0
        count_acerto = 0
        for x in range(4):
            print("Linha número: {}".format(x))
            #print("Treino: ", training[x])
            #print("Pesos = ", w)
            u = np.multiply(training[x], w)

            print("u = ", sum(u))
            yAtual = predict(sum(u))
            print("Saida atual = ", yAtual)
            error = yDesejada[x] - yAtual

            if(error == 1):
                print("Houve erro")
                w[0] += CONST_LEARNING_RATE * error
                w[1] += (CONST_LEARNING_RATE * error * training[x][1], [0]) + w[0]
                w[2] += (CONST_LEARNING_RATE * error * training[x][2], [1]) + w[0]

            else:
                print("OK")
                count_acerto += 1

            if(count_acerto == 4):
                count_error = 0
        epochs += + 1
        print("Epocas = ", epochs)


train(bias, w)


