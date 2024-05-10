# Python Program Demonstrating Practical Uses of List Comprehensions

# Basic Example: Squaring numbers
# Creates a list of squares for numbers 1 through 10 using list comprehension.
squares = [i * i for i in range(1, 11)]
print("Squares of numbers 1-10:", squares)
# Explanation: This line computes the square of each integer from 1 to 10.


# Real-World Example 1: Checking inventory levels
# Generates a list of low stock alerts for items with stock levels below a threshold.
inventory = ['pens', 'pencils', 'notebooks']
stock_levels = [24, 12, 33]
low_stock_alerts = [f"Alert: {item} has low stock: {stock} units" 
                    for item, stock in zip(inventory, stock_levels) if stock < 20]
print("Low stock alerts:", low_stock_alerts)
# Explanation: Filters and formats messages for items with stock below 20.

# Real-World Example 2: Tagging data rows for analysis
# Creates a list of data paired with indices for easier reference and manipulation.
data = ["data1", "data2", "data3"]
tagged_data = [(index, d) for index, d in enumerate(data)]
print("Tagged Data:", tagged_data)
# Explanation: Adds an index to each data item for tracking and reference.

# Real-World Example 3: Prioritizing tasks
# Generates a list of task descriptions with a priority tag.
tasks = ["email client", "write report", "meeting"]
prioritized_tasks = [f"Urgent task: {task}" if index == 0 else f"Task {index + 1}: {task}" 
                for index, task in enumerate(tasks)]
print("Prioritized Tasks:", prioritized_tasks)
# Explanation: Assigns a priority label to tasks, marking the first as urgent.

# Python Program Demonstrating Various List Comprehensions

# Example 1: Squaring Numbers
# Creates a list of squares for numbers 1 to 100 using list comprehension.
squares = [i**2 for i in range(1, 101)]
print("Squares of numbers 1 to 100:", squares)

# Example 2: Computing Remainders
# Generates the remainders of squares of numbers from 1 to 100 when divided by 11.
remainders = [x**2 % 11 for x in range(1, 101)]
print("Remainders of squares mod 11 from 1 to 100:", remainders)

# Example 3: Filtering Movie List
# Filters a list of movies to include only those released after the year 2000.
movies = [("The Matrix", 1999), ("Avatar", 2009), ("Inception", 2010)]
recent_movies = [title for (title, year) in movies if year > 2000]
print("Movies released after 2000:", recent_movies)

# Example 4: Cartesian Product of Odd and Even Numbers
# Generates a Cartesian product of odd and even numbers up to 10.
odds = [1, 3, 5, 7, 9]
evens = [2, 4, 6, 8, 10]
cartesian_product = [(odd, even) for odd in odds for even in evens]
print("Cartesian product of odd and even integers up to 10:", cartesian_product)

