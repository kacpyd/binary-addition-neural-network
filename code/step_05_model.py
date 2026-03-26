# -*- coding: utf-8 -*-
"""
Step 05:
Define the neural network model for binary addition.
"""

import torch
import torch.nn as nn

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

print("Shape of X:", X_tensor.shape)
print("Shape of Y:", Y_tensor.shape)

model = nn.Sequential(
    nn.Linear(8, 32),
    nn.ReLU(),
    nn.Linear(32, 32),
    nn.ReLU(),
    nn.Linear(32, 5),
    nn.Sigmoid()
)

sample_output = model(X_tensor[:3])

print("Output of model for three examples:")
print(sample_output)
print("Shape of output:", sample_output.shape)
