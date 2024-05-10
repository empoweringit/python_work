# Set up the variable with extra spaces.
favorite_language = ' python '

# Remove trailing spaces and print.
favorite_language = favorite_language.rstrip()
print(favorite_language)

# Remove leading spaces and print.
favorite_language = favorite_language.lstrip()
print(favorite_language)

# Remove spaces from both ends and print.
favorite_language = favorite_language.strip()
print(favorite_language)

# Program to demonstrate strip, lstrip, and rstrip functions
example_text = "   Hello, World!   "
print("Original text:", f"'{example_text}'")

# Using strip to remove spaces from both ends
stripped_text = example_text.strip()
print("Text after strip():", f"'{stripped_text}'")

# Using lstrip to remove spaces from the left end
left_stripped_text = example_text.lstrip()
print("Text after lstrip():", f"'{left_stripped_text}'")

# Using rstrip to remove spaces from the right end
right_stripped_text = example_text.rstrip()
print("Text after rstrip():", f"'{right_stripped_text}'")
