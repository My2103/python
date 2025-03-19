"""
Program: minutes.py
Author:
Last date modified:
The purpose of this program is to takes number of years as input and calculates and 
displays the value of distance traveled in meters
"""
# Speed of light in meters per second
LIGHT_TRAVEL = 3 * (10**8)

# Number of seconds in a year
SECONDS_PER_YEAR = 365 * 24 * 60 * 60

# Prompt the number of years from user
years = int(input("Enter the number of years: "))

# Compute the distance light travels in that period
distance = years * LIGHT_TRAVEL * SECONDS_PER_YEAR

# Output the result
print("The distance light travels in that period is:", distance, "meters")