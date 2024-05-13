# Empty Tuple Example
empty_tuple = ()
print("Empty Tuple:", empty_tuple)

# Single Element Tuple
single_element_tuple = (3,)
print("Single Element Tuple:", single_element_tuple)

# Mixed Data Types Tuple
mixed_tuple = (1, 'hello', 3.14, None)
print("Mixed Data Types Tuple:", mixed_tuple)

# Nested Tuples
nested_tuple = (1, (2, 3), [4, 5])
print("Nested Tuple:", nested_tuple)

# Accessing Elements of a Tuple
a_tuple = ('a', 'b', 'c', 'd')
print("Access Element 1:", a_tuple[1])

# Slicing Tuples
print("Sliced Tuple:", a_tuple[1:3])

# Unpacking Tuples
x, y, z, w = a_tuple
print("Unpacked Values:", x, y, z, w)

# Real World Example 1: Using Tuples as Keys in Dictionaries
# Tuples are ideal as keys in dictionaries because of their immutability
coordinates_info = {(35.6895, 139.6917): "Tokyo", (40.7128, -74.0060): "New York"}
print("Dictionary with Tuple Keys:", coordinates_info)

# Real World Example 2: Returning Multiple Values from Functions
def get_dimensions():
    # Returning width, height, depth as a tuple
    return 1920, 1080, 100

dimensions = get_dimensions()
print("Function Returning Multiple Values:", dimensions)

# Real World Example 3: Data Grouping
# Tuples are great for grouping related data together.
employee_record = ("John Doe", 30, "Software Engineer")
print("Employee Record:", employee_record)

# This script provides a basic to advanced introduction to Python tuples,
# showcasing how to create, access, and use them, along with real-world applications.
