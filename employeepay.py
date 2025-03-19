"""
Program: momentum.py
Author:
Last date modified:
The purpose of this program is takes as inputs the hourly wage, total regular hours, and total overtime hour
and display an employee's total weekly pay.

An employee's total weekly pay equals the hourly wage multiplied by the total number of regular hours 
plus any over time pay. Overtime pay equals the total overtime hours multiplied by 1.5 times the hourly wage
"""

# Prompt the values from users
hourly_wage = float(input("Enter your hourly wage: "))
total_regular_hours = float(input("Enter your total regular hours: "))
total_overtime_hours = float(input("Enter your total overtime hours: "))

# Compute the total pay
total_pay = (hourly_wage * total_regular_hours) + (total_overtime_hours * hourly_wage * 1.5)

# Output the result
print("Total weekly pay is:", total_pay)