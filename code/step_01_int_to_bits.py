# -*- coding: utf-8 -*-
"""
Step 01:
Create a helper function that converts an integer into a fixed-length binary list.
"""

def int_to_bits(n, width):
    binary = format(n, f'0{width}b')
    return [int(bit) for bit in binary]

print(int_to_bits(5, 4))
print(int_to_bits(17, 5))
print(int_to_bits(0, 4))
print(int_to_bits(15, 4))
