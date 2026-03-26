# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 09:01:29 2026

@author: kacpe
"""

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

print("Number of examples:", len(X))
print("First example:")
print("X[0] =", X[0])
print("Y[0] =", Y[0])

print("Last example:")
print("X[-1] =", X[-1])
print("Y[-1] =", Y[-1])