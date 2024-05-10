# Program to demonstrate the use of the replace function in Python strings

# Defining the original text
example_text = "Hello, World!"

# Using the replace method to substitute 'World' with 'there'
# The replace method searches for all instances of the first argument ('World') and replaces them with the second argument ('there')
replaced_text = example_text.replace("World", "there")
print("Original text:", example_text)
print("Text after replacement:", replaced_text)

# Demonstrating replacement with limited occurrences
# The third argument in the replace method specifies the maximum number of occurrences to replace
# This example replaces only the first occurrence of 'o' with '0'
limited_replace_text = example_text.replace('o', '0', 1)
print("Text after limited replacement (one occurrence):", limited_replace_text)

# Example with multiple replacements for training purposes
multi_replace_text = "Banana"
# Replace 'a' with 'o', demonstrating how all occurrences are replaced by default
multi_replace_text = multi_replace_text.replace('a', 'o')
print("Multiple replacements:", multi_replace_text)

# Replacing a substring that does not exist, to show it leaves the string unchanged
no_effect_replace_text = example_text.replace("Python", "Java")
print("Replacement with no effect (substring not found):", no_effect_replace_text)
