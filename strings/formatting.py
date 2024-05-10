# Program to demonstrate various string padding techniques

# Using zfill to pad a number with zeros on the left
example_number = "42"
zero_filled = example_number.zfill(5)
print("Original number:", example_number)
print("Zero filled number:", zero_filled)

# Using ljust to pad a string with spaces on the right to ensure it has a specified length
example_text = "apple"
left_justified = example_text.ljust(10)
print("\nOriginal text:", example_text)
print("Left justified with spaces:", f"'{left_justified}'")

# Using ljust with a custom fill character
left_justified_custom = example_text.ljust(10, '-')
print("Left justified with custom character:", f"'{left_justified_custom}'")

# Using rjust to pad a string with spaces on the left to ensure it has a specified length
right_justified = example_text.rjust(10)
print("\nRight justified with spaces:", f"'{right_justified}'")

# Using rjust with a custom fill character
right_justified_custom = example_text.rjust(10, '-')
print("Right justified with custom character:", f"'{right_justified_custom}'")

# Using center to center a string within a specified width with spaces
centered_text = example_text.center(10)
print("\nCentered with spaces:", f"'{centered_text}'")

# Using center with a custom fill character
centered_text_custom = example_text.center(10, '-')
print("Centered with custom character:", f"'{centered_text_custom}'")
