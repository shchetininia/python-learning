import numpy as np
def sigmoid(z):
    return 1/(1+np.exp(-z))

def neuron(x, w, b):
    z = w @ x + b
    return sigmoid(z)

def layer(x, W, b):
        z = W @ x + b
        return sigmoid(z)

x = np.array([30, 100, -0.5])
w = np.array([0.8, 1.5, 30])
b = 5

print(neuron(x, w, b))
w[2] = 400
print(neuron(x, w, b))
print(w)
print(w@x)
w[2] = 30

W = np.array([w,w-1.22,-w*1.5])
print(W)
B = np.array([5,10,15])
print(layer(x,W,B))
print(np.shape(x), np.shape(W))