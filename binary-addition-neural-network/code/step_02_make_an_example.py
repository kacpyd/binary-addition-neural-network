# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 08:59:27 2026

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

x, y = make_example(11, 6)

print("x =", x)
print("y =", y)