# Original and Modified Dimensions Example
dimensions = (200, 50)

print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

# Modifying the dimensions tuple
dimensions = (400, 100)

print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

# Real-World Example 1: Image Resizing
image_sizes = [(800, 600), (1024, 768), (1280, 720)]
resized_sizes = (400, 300)

print("\nResizing images:")
for original_size in image_sizes:
    print(f"Original: {original_size}, Resized: {resized_sizes}")

# Real-World Example 2: Coordinate Transformation
original_coordinates = [(10.0, 20.0), (30.5, 60.5), (50.0, 40.0)]
offset = (5.5, 3.5)

print("\nAdjusted coordinates:")
for (x, y) in original_coordinates:
    new_coordinates = (x + offset[0], y + offset[1])
    print(f"Original: {(x, y)}, Adjusted: {new_coordinates}")

# Real-World Example 3: Batch Processing Data
data_batches = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

print("\nProcessing data batches:")
for batch in data_batches:
    processed = tuple(x * 2 for x in batch)
    print(f"Original: {batch}, Processed: {processed}")

# All code blocks are structured to demonstrate the efficient use of tuples in various contexts,
# emphasizing their immutability and practicality for fixed-size and unchangeable sequences of elements.

        # Initial menu in the buffet-style restaurant
menu = ("chicken", "beef", "salad", "soup", "rice")

# Printing the initial menu using a for loop
print("Original Menu:")
for item in menu:
    print(item)

# The restaurant decides to change 'soup' to 'pasta' and 'rice' to 'mashed potatoes'
# Since tuples are immutable, we cannot change them directly, we need to create a new tuple
menu = ("chicken", "beef", "salad", "pasta", "mashed potatoes")

# Printing the updated menu using a for loop
print("\nUpdated Menu:")
for item in menu:
    print(item)
