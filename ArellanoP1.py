# ArellanoP1
# Programmer: Alonzo Arellano
# Email: aarellano34@cnm.edu
# Purpose: Provides user capability to calculate
# Volume of a pyramid

# call internal functions
import math

# Given inputs
base = float(input('Please enter the length of the pyramid: '))
height = float(input('Please enter the height of the pyramid: '))
slantHeight = math.sqrt(height ** 2 + (base / 2 ) ** 2)

# Calculate volume of pyramid
volume = base ** 2 * height / 3

# Calculate slant height of pyramid
slantHeight = math.sqrt(height ** 2 + (base / 2) ** 2)

# Calculate area of side of pyramid
area = slantHeight * base / 2
total_SA = area * 4

# Display results
print("\n The surface area of the pyramid = %.2f" %total_SA)
print("\n The volume of the pyramid = %.2f" %volume)