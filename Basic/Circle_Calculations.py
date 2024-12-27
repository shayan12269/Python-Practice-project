# Practice 11 | Circle Calculations (Area and Circumference)

import math

try:
    # Prompt the user to enter the diameter of the circle
    diameter_input = input("Enter the diameter of the circle: ")
    diameter = float(diameter_input)
    radius = diameter / 2
except ValueError:
    # Handle invalid input
    print("Invalid input. Please enter a valid number for the diameter.")
    # Exit the program since 'radius' is not defined
    exit()

# Calculate the area of the circle
surface_circle = math.pi * radius ** 2 

# Calculate the circumference of the circle
circumference = 2 * math.pi * radius

# Display the results
print(f"For the circle with radius {radius}, the area is {surface_circle:.2f} and the circumference is {circumference:.2f}")
