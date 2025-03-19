"""
Program: momentum.py
Author:
Last date modified:
The purpose of this program is to accepts an object's mass (in kilograms) and velocity (in meters per second) 
as inputs and then outputs its momentum
"""
# Prompt the values of mass and velocity from user
mass = float(input("Enter the object's mass (in kilograms): "))
velocity = float(input("Enter the velocity (in meters per second): "))

# Compute the momentum
momentum = mass * velocity

# Output the result
print("The momentum is:", momentum, "kg·m/s")
