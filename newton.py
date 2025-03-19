"""
Program: newton.py
Author: Ken

This program computes the square root of a number using Newton's method
of successive approximations and compares it with Python's built-in math.sqrt function.

1. Input: A positive number from the user.
2. Outputs:
   - The program's estimate of the square root using Newton's method.
   - Python's estimate of the square root using math.sqrt.
"""

import math

# Receive the input number from the user as a float
x = float(input("Enter a positive number: "))

# Initialize the tolerance and estimate
tolerance = 0.000001
estimate = 1.0

# Perform the successive approximations using Newton's method
while True:
    estimate = (estimate + x / estimate) / 2
    difference = abs(x - estimate**2)
    if difference <= tolerance:
        break

# Output the program's estimate and Python's estimate
print("The program's estimate:", estimate)
print("Python's estimate:", math.sqrt(x))

