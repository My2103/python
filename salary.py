"""
Program: salary.py
Author:
Last date modified:
The purpose of this program is takes as inputs the starting salary, the percentage increase, and the number 
of years in the schedule. Then displays a salary schedule, in tabular format, for teachers in a school 
district. Each row in the schedule should contain the year number and the salary for that year.

For example, a beginning teacher in the Lexington School District might be paid $30,000 the first year. 
For each year of experience after this first year, up to 10 years, the teacher receives a 2% increase over 
the preceding value. 
"""
#Declared the variables
starting_salary = int(input("Enter the starting salary: "))
PERCENTAGE_INCREASE_EACH_YEAR = 2
year_of_experience = int(input("Enter the number of year of experience: "))

year = 1 #Declared variable year

#Create a while loop to compute and print the salary for each year
while(year <= year_of_experience):
    increased_salary = starting_salary + (starting_salary * (PERCENTAGE_INCREASE_EACH_YEAR/100))
    starting_salary = increased_salary
    print("%-3d%12d" % (year, increased_salary))
    year += 1

    

# starting_salary*(PERCENTAGE_INCREASE_EACH_YEAR)**year_of_experience
