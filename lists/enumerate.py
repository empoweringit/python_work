# Python List Comprehensions: Practical Examples

# Basic Example: Squaring numbers
# Creates a list of squares for numbers 1 through 10.
squares = [i * i for i in range(1, 11)]
print("Squares of numbers 1-10:", squares)
# Explanation: Multiplies each number 'i' by itself for numbers 1 to 10.

# Real-World Example 1: Calculating areas of square plots
# Calculates the area for plots with side lengths of 5, 10, 15, 20, and 25 meters.
side_lengths = [5, 10, 15, 20, 25]
areas = [length * length for length in side_lengths]
print("Areas of square plots (sq m):", areas)
# Explanation: Computes area by squaring each 'length' in the list of side lengths.

# Real-World Example 2: Converting temperatures from Celsius to Fahrenheit
# Converts a list of Celsius temperatures to Fahrenheit.
celsius_temps = [0, 10, 20, 30, 40]
fahrenheit_temps = [(c * 9/5) + 32 for c in celsius_temps]
print("Temperatures in Fahrenheit:", fahrenheit_temps)
# Explanation: Converts each Celsius 'c' to Fahrenheit using the formula (c * 9/5) + 32.

# Real-World Example 3: Filtering out negative numbers from financial transactions
# Filters a list to include only positive transactions from a list of mixed transactions.
transactions = [150, -100, 200, -50, 300]
positive_transactions = [t for t in transactions if t > 0]
print("Positive transactions:", positive_transactions)
# Explanation: Includes only those transactions 't' that are greater than zero.

