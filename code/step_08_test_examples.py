# -*- coding: utf-8 -*-
"""
Step 08:
Test the trained model on selected examples of binary addition.
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


def bits_to_int(bits):
    bits = [int(b) for b in bits]
    bit_string = ''.join(str(b) for b in bits)
    return int(bit_string, 2)


def test_example(a, b, model, input_width=4):
    x, y_true = make_example(a, b, input_width)

    x_tensor = torch.tensor([x], dtype=torch.float32)

    with torch.no_grad():
        y_pred = model(x_tensor)
        y_pred_rounded = (y_pred >= 0.5).float()[0].tolist()

    a_bits = int_to_bits(a, input_width)
    b_bits = int_to_bits(b, input_width)

    true_value = bits_to_int(y_true)
    pred_value = bits_to_int(y_pred_rounded)

    print(f"a = {a} -> {a_bits}")
    print(f"b = {b} -> {b_bits}")
    print(f"true sum = {y_true} -> {true_value}")
    print(f"predicted   = {y_pred_rounded} -> {pred_value}")
    print()


# -------------------------
# 1. Budowa danych
# -------------------------
X, Y = build_dataset(4)

X_tensor = torch.tensor(X, dtype=torch.float32)
Y_tensor = torch.tensor(Y, dtype=torch.float32)

print("Shape of X:", X_tensor.shape)
print("Shape of Y:", Y_tensor.shape)


# -------------------------
# 2. Model
# -------------------------
model = nn.Sequential(
    nn.Linear(8, 32),
    nn.ReLU(),
    nn.Linear(32, 32),
    nn.ReLU(),
    nn.Linear(32, 5),
    nn.Sigmoid()
)


# -------------------------
# 3. Uczenie
# -------------------------
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.1)

epochs = 3000

for epoch in range(epochs):
    outputs = model(X_tensor)
    loss = criterion(outputs, Y_tensor)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 300 == 0:
        print(f"Epoch {epoch}, loss = {loss.item():.6f}")


# -------------------------
# 4. Ocena na całym zbiorze
# -------------------------
with torch.no_grad():
    predictions = model(X_tensor)
    predictions_rounded = (predictions >= 0.5).float()

print("\nFew examples:\n")

for i in range(10):
    print("Input:   ", X_tensor[i].tolist())
    print("True:    ", Y_tensor[i].tolist())
    print("Predicted: ", predictions_rounded[i].tolist())
    print()

correct_rows = (predictions_rounded == Y_tensor).all(dim=1)
accuracy = correct_rows.float().mean()

print("Final accuracy:", accuracy.item())
print()


# -------------------------
# 5. Test konkretnych sum
# -------------------------
test_example(1, 1, model)
test_example(2, 3, model)
test_example(9, 4, model)
test_example(14, 1, model)
