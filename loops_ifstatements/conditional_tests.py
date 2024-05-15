# Example of conditional tests with predictions and explanations

# Test 1
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')  # This will print True because car is indeed 'subaru'

# Test 2
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')  # This will print False because car is not 'audi'

# Test 3
color = 'blue'
print("\nIs color == 'blue'? I predict True.")
print(color == 'blue')  # This will print True because color is 'blue'

# Test 4
print("\nIs color == 'green'? I predict False.")
print(color == 'green')  # This will print False because color is not 'green'

# Test 5
number = 25
print("\nIs number > 20? I predict True.")
print(number > 20)  # This will print True because 25 is greater than 20

# Test 6
print("\nIs number < 20? I predict False.")
print(number < 20)  # This will print False because 25 is not less than 20

# Test 7
animal = 'dog'
print("\nIs animal == 'dog'? I predict True.")
print(animal == 'dog')  # This will print True because animal is 'dog'

# Test 8
print("\nIs animal == 'cat'? I predict False.")
print(animal == 'cat')  # This will print False because animal is not 'cat'

# Test 9
is_student = True
print("\nIs is_student? I predict True.")
print(is_student)  # This will print True because is_student is True

# Test 10
print("\nIs not is_student? I predict False.")
print(not is_student)  # This will print False because is_student is not False

# Additional True and False conditions
temperature = 30
print("\nIs temperature <= 30? I predict True.")
print(temperature <= 30)  # True, because temperature is 30, which is equal to 30

print("\nIs temperature > 30? I predict False.")
print(temperature > 30)  # False, because temperature is not greater than 30

# These tests showcase various types of comparisons: equality, inequality, greater than, and less than.
# Understanding each result helps in grasping how Python evaluates different conditions.

# Python script for demonstrating a variety of conditional tests

# 1) Test for equality and inequality with strings
print("1) Equality and Inequality with Strings")
favorite_food = 'pizza'
print("Is favorite_food == 'pizza'? I predict True.")
print(favorite_food == 'pizza')  # True

print("Is favorite_food != 'burger'? I predict True.")
print(favorite_food != 'burger')  # True

print("Is favorite_food == 'burger'? I predict False.")
print(favorite_food == 'burger')  # False

# 2) Test using the lower() method
print("\n2) Testing with the lower() method")
car = 'Tesla'
print("Is car.lower() == 'tesla'? I predict True.")
print(car.lower() == 'tesla')  # True

print("Is car.lower() == 'audi'? I predict False.")
print(car.lower() == 'audi')  # False

# 3) Numerical tests involving equality and inequality, greater than and less than,
# greater than or equal to, and less than or equal to
print("\n3) Numerical Tests")
age = 30
print("Is age == 30? I predict True.")
print(age == 30)  # True

print("Is age != 25? I predict True.")
print(age != 25)  # True

print("Is age > 25? I predict True.")
print(age > 25)  # True

print("Is age < 40? I predict True.")
print(age < 40)  # True

print("Is age >= 31? I predict False.")
print(age >= 31)  # False

print("Is age <= 29? I predict False.")
print(age <= 29)  # False

# 4) Tests using the 'and' keyword and the 'or' keyword
print("\n4) Logical Operator Tests with 'and' & 'or'")
budget = 100
item_cost = 75
print("Is budget >= item_cost and item_cost > 50? I predict True.")
print(budget >= item_cost and item_cost > 50)  # True

print("Is budget > 100 and item_cost <= 75? I predict False.")
print(budget > 100 and item_cost <= 75)  # False

print("Is budget > 50 or item_cost > 100? I predict True.")
print(budget > 50 or item_cost > 100)  # True

print("Is budget < 75 or item_cost > 100? I predict False.")
print(budget < 75 or item_cost > 100)  # False

# 5) Test whether an item is in a list
print("\n5) Membership Tests in a List")
fruits = ['apple', 'banana', 'cherry']
print("Is 'apple' in fruits? I predict True.")
print('apple' in fruits)  # True

print("Is 'mango' in fruits? I predict False.")
print('mango' in fruits)  # False

# 6) Test whether an item is not in a list
print("\n6) Non-Membership Tests in a List")
print("Is 'pear' not in fruits? I predict True.")
print('pear' not in fruits)  # True

print("Is 'banana' not in fruits? I predict False.")
print('banana' not in fruits)  # False

# This script not only runs these tests but also prints out the expected outcomes,
# helping beginners to verify their understanding of Python's conditional logic.
