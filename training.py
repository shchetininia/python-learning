import numpy as np
def sigmoid(z):
    return 1/(1+np.exp(-z))

def neuron(x, w, b):
    z = w * x + b
    return sigmoid(z)

X = np.array([10, 50, 90, 150])/150.0
Y = np.array([0, 0, 1, 1])

w = np.random.randn()
b = np.random.randn()
count = 10000
alpha = 0.1
print(w, b)
while count > 0:
    y_pred = neuron(X, w, b)
    dL_dw = np.mean(2 * (y_pred - Y) * y_pred * (1 - y_pred) * X)
    dL_db = np.mean(2 * (y_pred - Y) * y_pred * (1 - y_pred))
    w = w - alpha * dL_dw
    b = b - alpha * dL_db
    L = np.mean((y_pred - Y)**2)
    if count % 1000 == 0:
        print(f"iter {10000 - count}, L = {L:.4f}, y_pred = {np.round(y_pred, 2)}")
    count -= 1
print(y_pred)



