# -*- coding: utf-8 -*-
"""
Step 04:
Convert the generated dataset into PyTorch tensors.
"""
import torch

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

print("First line X_tensor:")
print(X_tensor[0])

print("First line Y_tensor:")
print(Y_tensor[0])
