import math

#Gives the volume of a tire based on user input

width= float(input("Enter the width of the tire in mm (e.g., 205): "))
aspect_ratio= float(input("Enter the aspect ratio of the tire (e.g., 60): "))
diameter= float(input("Enter the diameter of the wheel in inches (e.g., 15): "))

# 2. Perform the arithmetic
# Use math.pi for the constant PI.
term1 = math.pi * (width ** 2) * aspect_ratio
term2 = (width * aspect_ratio) + (2540 * diameter)
volume = (term1 * term2) / 10000000000

# 3. Display results
# We use an f-string to round the result to 2 decimal places.
print(f"\nThe approximate volume is {volume:.2f} liters")