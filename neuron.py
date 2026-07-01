import numpy as np
def sigmoid(z):
    return 1/(1+np.exp(-z))

def neuron(x, w, b):
    z = w @ x + b
    return sigmoid(z)

x = np.array([30, 100, -0.5])
w = np.array([0.8, 1.5, 30])
b = 5

print(neuron(x, w, b))
w[2] = 400
print(neuron(x, w, b))
print(w)
print(w@x)