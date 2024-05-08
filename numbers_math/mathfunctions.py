# Importing the math module to gain access to advanced mathematical functions and constants.
import math

# Introduction to using mathematical functions from the math module.
print("Using math module for Mathematical Functions:")

# The abs() function returns the absolute value of a number, removing any negative sign.
print("Absolute value of -10 is:", abs(-10), "shows the non-negative value of -10.")

# The math.exp(x) function returns e raised to the power of x, where e is the base of natural logarithms.
print("Exponential of 1 (math.exp(1)):", math.exp(1), "which is e to the power of 1, approximately 2.71828.")

# The math.e constant represents the base of natural logarithms, known as Euler's number.
print("Euler's number (math.e):", math.e, "is a fundamental constant used in mathematics.")

# The math.pi constant is the value of π (pi), which is the ratio of a circle's circumference to its diameter.
print("Value of PI (math.pi):", math.pi, "is the ratio of the circumference of any circle to its diameter.")

# The math.sqrt(x) function calculates the square root of x.
print("Square root of 16 (math.sqrt(16)):", math.sqrt(16), "which calculates to 4, as 4 times 4 equals 16.")

# Demonstrating the max() and min() functions to find the maximum and minimum values in a list.
print("\nMax and Min Functions:")
numbers = [5, 9, 23, -1, 34, 76]
# The max() function returns the largest item in an iterable or the largest of two or more arguments.
print("Maximum value in the list:", max(numbers), "is the largest number among the list items.")

# The min() function returns the smallest item in an iterable or the smallest of two or more arguments.
print("Minimum value in the list:", min(numbers), "is the smallest number among the list items.")

# Starting the demonstration of various mathematical functions.
print("Further Demonstrations:")

# Demonstrating rounding operations on a floating point number.
num = 13.67

# The round() function rounds a number to the nearest integer. If the fractional part is exactly 0.5, it rounds to the nearest even number.
print("Rounding 13.67 using round():", round(num), "rounds to the nearest integer.")

# The math.floor() function returns the largest integer less than or equal to the given number, effectively rounding down.
print("Using floor() which rounds down:", math.floor(num), "rounds 13.67 down to 13.")

# The math.ceil() function returns the smallest integer greater than or equal to the given number, effectively rounding up.
print("Using ceil() which rounds up:", math.ceil(num), "rounds 13.67 up to 14.")

# Demonstrating trigonometric functions.
# First, converting an angle from degrees to radians since trigonometric functions in Python require angles in radians.
angle = math.radians(90)  # Convert 90 degrees to radians.
# The math.sin() function returns the sine of the specified angle.
print("Sin of 90 degrees:", math.sin(angle), "is the trigonometric sine of 90 degrees.")

# Additional demonstrations of mathematical functions from the math module.

# Demonstrating the math.log() function, which calculates the natural logarithm of a specified number.
# Adding a check to ensure the logarithm is not taken of a non-positive number.
positive_num = 10
print("Natural logarithm of 10:", math.log(positive_num), "is the log base e of 10.")

# The math.pow() function raises a number to the power of another specified number.
base, exponent = 2, 3
print("2 raised to the power of 3 using math.pow():", math.pow(base, exponent), "equals 8.")

# Showing the use of math.fabs() which returns the absolute value of a number but always as a float.
negative_number = -10.5
print("Absolute value using math.fabs():", math.fabs(negative_number), "returns 10.5 as a positive float.")

# Demonstrating the math.copysign() function, which returns a float consisting of the magnitude of the first parameter and the sign of the second parameter.
print("Copy sign from -3 to 2 using math.copysign():", math.copysign(2, -3), "results in -2.")
