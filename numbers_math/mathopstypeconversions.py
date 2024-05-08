# Basic Math Operations and Type Conversions

# Integer division: This operation divides one number by another and then rounds down to the nearest integer.
# It is useful when you need the whole number result of division, without the remainder.
print("Integer division (5 // 3):", 5 // 3, "which is the floor result of 5 divided by 3.")

# Complex division: Demonstrates division when working with complex numbers (numbers with both real and imaginary parts).
# In Python, imaginary numbers are denoted by 'j' or 'J'.
print("Complex division (5j / 2j):", 5j / 2j, "which is the result of dividing two imaginary numbers.")

# Exponents: Using the exponentiation operator '**' to calculate powers.
# This operation raises the first number to the power of the second number.
print("Exponents (2**3):", 2**3, "which calculates 2 raised to the power of 3.")

# Modulus: This operation finds the remainder of the division of one number by another.
# It is useful for determining if a number is divisible by another (if the modulus is zero).
print("Modulus (5 % 3):", 5 % 3, "which is the remainder when 5 is divided by 3.")

# Convert float to int: Demonstrates conversion from a floating-point number to an integer.
# This conversion truncates (removes) the decimal part of the float, providing just the integer portion.
print("\nType Conversions:")
x = 5.5  # A floating-point number.
print("Convert float to int:", int(x), "where the decimal part is truncated.")

# Convert int to float: Shows how an integer can be converted back to a float.
# This might be necessary when floating-point precision is required in calculations.
print("Convert int to float:", float(int(x)), "which makes the integer a floating-point number.")

# Convert number to complex: Converts a real number to a complex number by adding a zero imaginary part.
# Complex numbers are used in various scientific calculations and typically consist of a real and an imaginary part.
# Here we convert the number x to a complex number with zero as the imaginary part.
print("Convert number to complex:", complex(x), "which adds a zero imaginary part to create a complex number.")
