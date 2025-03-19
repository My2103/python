"""
Program: minutes.py
Author:
Last date modified:
The purpose of this program is to takes as input a number of years and caculate 
and prints the number of minutes in that period of time
"""

MINUTES_PER_YEAR = 525600  # Constant variable for minutes in a year

# Prompt the number of years from user
years = int(input("Enter the number of years: "))

# Compute the number of minutes in that period
number_of_minutes = years * MINUTES_PER_YEAR

# Output the result
print("The number of minutes in that period of time is:", number_of_minutes)
