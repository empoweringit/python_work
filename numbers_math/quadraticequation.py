# Import the math library to access the sqrt (square root) function.
import math

# Introduction and user input for the quadratic equation coefficients.
print("Quadratic Equation Solver:")
a = int(input("Enter coefficient a (non-zero): "))  # Coefficient a must not be zero for a valid quadratic equation.
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))

# Calculating the discriminant to determine the nature of the roots.
d = b**2 - 4*a*c  # The discriminant formula: b^2 - 4ac
print("Discriminant (b^2 - 4ac):", d)  # Display the calculated discriminant.

# Conditional logic to determine the type of roots based on the discriminant.
if d > 0:
    # When discriminant is positive, the equation has two distinct real roots.
    root1 = (-b + math.sqrt(d)) / (2 * a)  # Using the quadratic formula to find the first root.
    root2 = (-b - math.sqrt(d)) / (2 * a)  # Using the quadratic formula to find the second root.
    print(f"Two distinct real roots: {root1} and {root2}")  # Output the roots.
elif d == 0:
    # When discriminant is zero, the equation has one real root (also known as a repeated root).
    root = -b / (2 * a)  # Simplified formula when discriminant is zero.
    print(f"One real root: {root}")  # Output the single root.
else:
    # When discriminant is negative, the equation has two complex roots.
    real_part = -b / (2 * a)  # Real part of the complex roots.
    imaginary_part = math.sqrt(-d) / (2 * a)  # Imaginary part of the complex roots, note sqrt of negative number.
    print(f"Complex roots: {real_part} + {imaginary_part}i and {real_part} - {imaginary_part}i")  # Output the complex roots.

