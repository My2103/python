"""
Program: minutes.py
Author:
Last date modified:
The purpose of this program is to takes number of years as input and calculates and displays the value of distance traveled in meters
"""

# Input: number of kilometers
kilometers = float(input("Enter the number of kilometers: "))

# Calculate the total number of minutes of arc between the North Pole and the equator
total_minutes_of_arc = 90 * 60

# Calculate the distance between the North Pole and the equator in kilometers
distance_pole_to_equator_km = 10002  # More accurate value

# Calculate the number of kilometers per minute of arc
km_per_minute_of_arc = distance_pole_to_equator_km / total_minutes_of_arc

# Calculate the number of nautical miles
nautical_miles = kilometers / km_per_minute_of_arc

# Print the result
print(f"{kilometers} kilometers is approximately {nautical_miles:.2f} nautical miles.")