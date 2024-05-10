# Python Program Demonstrating the Use of the sorted() Function

# Basic Example: Sorting a list of numbers
# Sorts a list of integers in ascending order.
numbers = [14, 3, 17, 7, 9, 1, 6]
sorted_numbers = sorted(numbers)
print("Sorted numbers (ascending):", sorted_numbers)
# Explanation: The sorted() function organizes the numbers in ascending order.

# Real-World Example 1: Sorting strings
# Sorts a list of names alphabetically.
names = ["Alice", "Bob", "Charlie", "Dave"]
sorted_names = sorted(names)
print("Sorted names:", sorted_names)
# Explanation: Alphabetically sorts the list of names using default order (A to Z).

# Real-World Example 2: Sorting by string length
# Sorts the same list of names by the length of the name.
sorted_by_length = sorted(names, key=len)
print("Names sorted by length:", sorted_by_length)
# Explanation: Sorts names based on their length, from shortest to longest, using the 'key' parameter.

# Real-World Example 3: Sorting with custom criteria
# Sorts a list of dictionaries representing products by their 'price' attribute in descending order.
products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Phone", "price": 700},
    {"name": "Camera", "price": 500}
]
sorted_by_price_desc = sorted(products, key=lambda x: x['price'], reverse=True)
print("Products sorted by price (descending):", sorted_by_price_desc)
# Explanation: Uses a lambda function as the key to sort products by price in descending order.

