# Variable for name and display variations.
name = "John Underwood"
print(name.title())  # Title case.
print(name.upper())  # Uppercase.
print(name.lower())  # Lowercase.

# Variable for a famous quote.
famous_person = "Don't cry because it's over. Smile because it happened."
message = f"{famous_person}"  # Format message.
print(f"Dr Seuss Once Said, {message}")  # Print message.

# Manipulate string to remove spaces.
my_name = ' John Underwood '
my_name = my_name.rstrip()  # Remove trailing(right) spaces.
print(my_name)
my_name = my_name.lstrip()  # Remove leading(left) spaces.
print(my_name)
my_name = my_name.strip()  # Remove leading and trailing spaces.
print(my_name)

# Handle file name string.
filename = 'python_notes.txt'
filename = filename.removesuffix('.txt')  # Remove suffix.
print(filename)  
