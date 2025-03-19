"""
Program: stats.py
Author: Mai Ngoc Diem My
Last date modified: 19/09/2024
The purpose of this program is create a set of functions that compute median and mode of a set of numbers.
Also include a function named mean, which computes the average of a set of numbers. Each function should 
expect a list of numbers as an argument and return a single number. Each function should return 0 if the 
list is empty. Include a main function that tests the three statistical functions with a given list. 
"""

def findMedian(arr):
    if not arr:
        print("The median is 0")
        return 0
        
    arr.sort()
    midpoint = len(arr) // 2
    print("The median is", end = " ")
    if len(arr) % 2 == 1:
        print(arr[midpoint])
    else:
        print((arr[midpoint] + arr[midpoint - 1])/2)

def computeAverage(arr):
    count = 0
    sum = 0
    for i in arr:
        count += 1
    for j in arr:
        sum += j
    return sum/count

def countFrequent(arr):
    count = 0
    number = int(input("Enter the number you want to count frequent: "))
    for i in arr:
        if(i == number):
            count += 1
    return count

def findMode(arr):
    count_dict = {}
    for i in arr:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    mode = max(count_dict, key=count_dict.get)
    return mode, count_dict[mode]

array = [2, 4, 9, 9, 9, 11, 11]
mode, frequency = findMode(array)
print(f"Mode: {mode}, Frequency: {frequency}")


