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

# Recursive Approach
def newton(estimate, x):
    """
    Recursive function that implements Newton's method for approximating square roots.

    Args:
        estimate (float): Initial estimate of the square root.
        x (float): The number for which the square root is being calculated.

    Returns:
        float: The approximate square root of x.
    """
    new_estimate = (estimate + x / estimate) / 2
    difference = abs(x - new_estimate**2)

    if difference <= tolerance:
        return new_estimate #base case: the recursive stop when the different <= tolerance
    else:
        return newton(new_estimate, x)  # Recursive call with updated estimate


# Calculate and output the program's estimate
program_estimate = newton(estimate, x)
print("The program's estimate:", program_estimate)

# Print Python's estimate using math.sqrt
print("Python's estimate:", math.sqrt(x))