# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 08:47:01 2026

@author: kacpe
"""

def int_to_bits(n, width):
    binary = format(n, f'0{width}b')
    return [int(bit) for bit in binary]

print(int_to_bits(5, 4))
print(int_to_bits(17, 5))
print(int_to_bits(0, 4))
print(int_to_bits(15, 4))