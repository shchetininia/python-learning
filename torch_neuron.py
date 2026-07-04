import torch
def neuron(x, w, b):
    z = w * x + b
    return torch.sigmoid(z)

X = torch.tensor([10, 50, 90, 150], dtype=torch.float32)/150.0
Y = torch.tensor([0, 0, 1, 1], dtype=torch.float32)

w = torch.randn(1, requires_grad = True)
b = torch.randn(1, requires_grad = True)
alpha = 0.1
count = 10000
print(w, b)

while count > 0:
    y_pred = neuron(X, w, b)
    L = torch.mean((y_pred - Y)**2)
    L.backward() 
    with torch.no_grad(): 
        w -= alpha * w.grad 
        b -= alpha * b.grad 
    w.grad.zero_() 
    b.grad.zero_() 
    if count % 1000 == 0:
        print(f"iter {10000 - count}, L = {L:.4f}, y_pred = {torch.round(y_pred.detach(), decimals=2)}")
    count -= 1
