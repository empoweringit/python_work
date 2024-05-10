# Program to demonstrate the use of the partition function in Python

# Defining a string to demonstrate partitioning
example_text = "Hello, World!"

# Using the partition method to split the string around ', '
# The partition method searches for the specified separator (', ') and splits the string into a tuple of three elements:
# 1. The part of the string before the separator
# 2. The separator itself (if found, otherwise an empty string)
# 3. The part of the string after the separator
before, separator, after = example_text.partition(", ")

# Printing the original text and the results of the partition
print("Original text:", example_text)
print("Before:", f"'{before}'", "Separator:", f"'{separator}'", "After:", f"'{after}'")

# Additional example to demonstrate partitioning when the separator is not found
# In this case, the original string is returned as the 'before' part, and both 'separator' and 'after' are empty strings
not_found_text = "Hello World"
before_nf, separator_nf, after_nf = not_found_text.partition(", ")
print("\nHandling case with no separator found:")
print("Original text:", not_found_text)
print("Before:", f"'{before_nf}'", "Separator:", f"'{separator_nf}'", "After:", f"'{after_nf}'")
