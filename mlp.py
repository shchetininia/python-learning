import torch
import torch.nn as nn
class MyNeuron(nn.Module):
    def __init__(self):
        super().__init__()
        self.hidden = nn.Linear(1, 4)
        self.output = nn.Linear(4, 1)
    def forward(self,x):
        x = torch.relu(self.hidden(x))
        return torch.sigmoid(self.output(x))
    


model = MyNeuron()
X = torch.tensor([10, 50, 90, 150], dtype=torch.float32)/150.0
Y = torch.tensor([0, 0, 1, 1], dtype=torch.float32)
X = X.unsqueeze(1)
Y = Y.unsqueeze(1)
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)
loss_fn = nn.BCELoss()
count = 10000

while count > 0:
    torch.manual_seed(42)
    optimizer.zero_grad()
    y_pred = model(X)
    # L = torch.mean((y_pred - Y)**2)
    L = loss_fn(y_pred, Y)
    L.backward()
    optimizer.step()
    if count % 1000 == 0:
        print(f"iter {10000 - count}, L = {L:.4f}, y_pred = {torch.round(y_pred.detach(), decimals=2)}")
    count -= 1
