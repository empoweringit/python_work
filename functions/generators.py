# Introduction to Generator Functions: Basic Example
def simple_counter(limit):
    """Generates numbers from 0 to limit."""
    num = 0
    while num < limit:
        yield num
        num += 1

print("Simple counter up to 5:")
for count in simple_counter(5):
    print(count)

# Real-World Example 1: Fibonacci Sequence Generator
def fibonacci(limit):
    """Generates the Fibonacci sequence up to a given limit."""
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

print("\nFibonacci Sequence up to 100:")
for fib in fibonacci(100):
    print(fib)

# Real-World Example 2: Reading Large Files
def read_large_file(file_name):
    """Lazily reads a large file line by line."""
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            for file_line in file:
                yield file_line.strip()
    except FileNotFoundError:
        print("File not found. Please check the file path.")

# Real-World Example 3: Streaming Data Processing
def process_data(input_stream):
    """Processes a data stream, doubling each data point."""
    for data_item in input_stream:
        yield data_item * 2

print("\nProcessed data stream (doubling values):")
stream_data = (x for x in range(10))  # Simulating streaming integers
for data in process_data(stream_data):
    print(data)

# Additional Example: Permutations of a Set
def permutations(items):
    """Yields all permutations of a given list of items."""
    if len(items) == 1:
        yield items
    else:
        for current_perm in permutations(items[1:]):
            for i in range(len(items)):
                yield current_perm[:i] + items[0:1] + current_perm[i:]

print("\nPermutations of ['apple', 'banana', 'cherry']:")
for perm in permutations(['apple', 'banana', 'cherry']):
    print(perm)

# Generator for the Top Ten Perfect Squares
def top_ten_squares():
    """Generates the first ten perfect squares."""
    n = 1
    while n <= 10:
        yield n * n
        n += 1

print("\nTop Ten Perfect Squares:")
for square in top_ten_squares():
    print(square)
