"""
Program: population.py
Author:
Last date modified:
The purpose of this program is takes as inputs the initial number of organisms, the rate of growth 
(a real number greater than 0), the number of hours it takes to achieve this rate, and a number of 
hours during which the population grows. Then displays a prediction of the total population.
"""

#Declare the variable
initial_number_organism = int(input("Enter the initial number of organisms: "))
rate_of_grow = float(input("Enter the rate of growth: "))
hours_achieve_rate = int(input("Enter the hours it takes to achieve this rate: "))
hours_population_grow = int(input("Enter a number of hours during which the population grows: "))

#Compute the prediction of the total population
prediction_total_population = initial_number_organism * rate_of_grow * (hours_population_grow/hours_achieve_rate)
print("Prediction of the total population:", prediction_total_population)
