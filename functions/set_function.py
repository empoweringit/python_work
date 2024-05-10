# Comprehensive Python Program Demonstrating Set Functions

# Basic Example: Fundamental Set Operations
# Creating and manipulating a set of numbers
numbers_set = {1, 2, 3, 4, 5}
numbers_set.add(6)  # Adding an element
numbers_set.discard(3)  # Removing an element
exists = 4 in numbers_set  # Membership test
print("Updated Set:", numbers_set)
print("Does 4 exist in the set?:", exists)

# Real-World Example 1: Removing Duplicates from a List
# Utilizing sets to remove duplicates from a list of names
names_list = ["Alice", "Bob", "Alice", "Charlie", "Bob"]
unique_names = set(names_list)
print("Unique names:", unique_names)

# Real-World Example 2: Intersection of Two Groups
# Using set intersection to find common elements between two groups
group_a = {"apple", "banana", "cherry"}
group_b = {"banana", "fig", "apple"}
common_fruits = group_a.intersection(group_b)
print("Common fruits between two groups:", common_fruits)

# Real-World Example 3: Symmetric Difference in Surveys
# Finding unique responses in surveys using symmetric difference
survey_a = {"yes", "no", "maybe", "no opinion"}
survey_b = {"maybe", "no", "not sure"}
unique_responses = survey_a.symmetric_difference(survey_b)
print("Unique responses in both surveys:", unique_responses)

