# Program to demonstrate various string slicing techniques

# Original text for slicing
example_text = "Hello, World!"

# Using positive indexing
slice1 = example_text[7:12]  # Slices 'World'
print("Slice using positive indexing:", slice1)

# Using negative indexing
slice2 = example_text[-6:-1]  # Also slices 'World', using negative indexes
print("Slice using negative indexing:", slice2)

# Slicing with steps
slice3 = example_text[0:12:2]  # 'Hlo ol', every second character from index 0 to 11
print("Slice with steps:", slice3)

# Omitting start and stop indices
slice4 = example_text[:]  # 'Hello, World!', makes a full copy of the string
print("Full slice copy:", slice4)

# Only omitting the stop index
slice5 = example_text[7:]  # 'World!', from index 7 to the end
print("Slice omitting stop index:", slice5)

# Only omitting the start index
slice6 = example_text[:5]  # 'Hello', from the start to index 4
print("Slice omitting start index:", slice6)

# Reversing a string
slice7 = example_text[::-1]  # '!dlroW ,olleH', reverses the string
print("Reversed string:", slice7)

# Step with negative index (reverse every second character)
slice8 = example_text[::-2]  # '!lo ,olH', every second character in reverse order
print("Reversed string with step:", slice8)