import torch
import torch.nn as nn
def neuron(x, w, b):
    z = w * x + b
    return torch.sigmoid(z)

class MyNeuron(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(1, 1)
    def forward(self, x):
        return torch.sigmoid(self.linear(x))

model = MyNeuron()
X = torch.tensor([10, 50, 90, 150], dtype=torch.float32)/150.0
Y = torch.tensor([0, 0, 1, 1], dtype=torch.float32)
X = X.unsqueeze(1)
Y = Y.unsqueeze(1)
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)
loss_fn = nn.BCELoss()
count = 10000

while count > 0:
    optimizer.zero_grad()
    y_pred = model(X)
    # L = torch.mean((y_pred - Y)**2)
    L = loss_fn(y_pred, Y)
    L.backward()
    optimizer.step()
    if count % 1000 == 0:
        print(f"iter {10000 - count}, L = {L:.4f}, y_pred = {torch.round(y_pred.detach(), decimals=2)}")
    count -= 1
