# -*- coding: utf-8 -*-
"""
Step 07:
Evaluate the trained model and measure accuracy on the full dataset.
"""

import torch
import torch.nn as nn
import torch.optim as optim

def int_to_bits(n, width):
    binary = format(n, f'0{width}b')
    return [int(bit) for bit in binary]

def make_example(a, b, input_width=4):
    a_bits = int_to_bits(a, input_width)
    b_bits = int_to_bits(b, input_width)
    
    x = a_bits + b_bits
    s = a + b
    y = int_to_bits(s, input_width + 1)
    
    return x, y

def build_dataset(input_width=4):
    X = []
    Y = []
    
    max_num = 2 ** input_width
    
    for a in range(max_num):
        for b in range(max_num):
            x, y = make_example(a, b, input_width)
            X.append(x)
            Y.append(y)
    
    return X, Y

X, Y = build_dataset(4)

X_tensor = torch.tensor(X, dtype=torch.float32)
Y_tensor = torch.tensor(Y, dtype=torch.float32)

model = nn.Sequential(
    nn.Linear(8, 32),
    nn.ReLU(),
    nn.Linear(32, 32),
    nn.ReLU(),
    nn.Linear(32, 5),
    nn.Sigmoid()
)

criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

epochs = 3000

for epoch in range(epochs):
    outputs = model(X_tensor)
    loss = criterion(outputs, Y_tensor)
    
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
    if epoch % 300 == 0:
        print(f"Epoch {epoch}, loss = {loss.item():.6f}")
        
with torch.no_grad():
    predictions = model(X_tensor)
    predictions_rounded = (predictions >= 0.5).float()

print("\nKilka przykładów:")

for i in range(10):
    print("Input:   ", X_tensor[i].tolist())
    print("True:    ", Y_tensor[i].tolist())
    print("Predicted: ", predictions_rounded[i].tolist())
    print()

correct_rows = (predictions_rounded == Y_tensor).all(dim=1)
accuracy = correct_rows.float().mean()

print("Dokładność pełnych wyników:", accuracy.item())      
