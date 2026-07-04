from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

data = load_breast_cancer()
X, y = data.data, data.target
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42
# )
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
X_val = scaler.transform(X_val)

class CancerDataset(Dataset):
    def __init__(self, X, y):
        self.X = torch.tensor(X, dtype=torch.float32)
        self.y = torch.tensor(y, dtype=torch.float32).unsqueeze(1)
    
    def __len__(self):
        return len(self.X)
    
    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]

train_dataset = CancerDataset(X_train, y_train)
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)

class MyNeuron(nn.Module):
    def __init__(self):
        super().__init__()
        self.hidden = nn.Linear(30,16)
        self.output = nn.Linear(16, 1)
        self.dropout = nn.Dropout(p=0.5)
    def forward(self, x):
        return torch.sigmoid(self.output(self.dropout(torch.relu(self.hidden(x)))))

model = MyNeuron()
# optimizer = torch.optim.SGD(model.parameters(), lr=0.1)
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
loss_fn = nn.BCELoss()
torch.manual_seed(42)
for epoch in range(50):
    train_loss = 0
    model.train()  # перед циклом обучения
    for X_batch, y_batch in train_loader:
            optimizer.zero_grad()
            y_pred = model(X_batch)
            L = loss_fn(y_pred, y_batch)
            L.backward()
            optimizer.step()
            with torch.no_grad():
                train_loss += L.item()
    model.eval()   # перед валидацией и тестом            
    with torch.no_grad():
        X_val_t = torch.tensor(X_val, dtype=torch.float32)
        y_val_t = torch.tensor(y_val, dtype=torch.float32).unsqueeze(1)
        y_val_pred = model(X_val_t)
        val_pred_labels = (y_val_pred >= 0.5).float()
        val_accuracy = (val_pred_labels == y_val_t).float().mean()
        print(f"Test accuracy: {val_accuracy:.4f}")  
    print(f"Train_loss: {train_loss/len(train_loader):.4f}")
    print(f"Номер эпохи: {epoch}, loss fn: {L:.4f}")

with torch.no_grad():
    X_test_t = torch.tensor(X_test, dtype=torch.float32)
    y_test_t = torch.tensor(y_test, dtype=torch.float32).unsqueeze(1)
    y_test_pred = model(X_test_t)
    test_pred_labels = (y_test_pred >= 0.5).float()
    accuracy = (test_pred_labels == y_test_t).float().mean()
    print(f"Test accuracy: {accuracy:.4f}")

