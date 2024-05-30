"""
This module contains examples of using conditionals and loops in Python.
"""

# Example 1: Checking for Equality and Inequality with Strings
requested_topping = 'mushroom'
# Check if the requested topping is not 'anchovies'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")  # Expected output: "Hold the anchovies!"

# Example 2: Checking for an incorrect answer using a nested conditional
user_answer = 17
# Check if the provided answer is not equal to the expected answer (42)
if user_answer != 42:
    print("That is not the correct answer. Please try again!")  # Expected output:
    # "That is not the correct answer. Please try again!"

# Example 3: Using membership tests with lists
requested_toppings = ['mushrooms', 'onions', 'pineapple']
# Check if 'mushrooms' and 'pepperoni' are in the list of requested toppings
print('mushrooms' in requested_toppings)  # Outputs: True
print('pepperoni' in requested_toppings)  # Outputs: False

# Example 4: Using `not in` to check for non-membership
banned_users = ['andrew', 'carolina', 'david']
current_user = 'marie'
# Check if 'marie' is not in the list of banned users
if current_user not in banned_users:
    print(f"{current_user.title()}, you can post a response if you wish.")  # Expected output:
    # "Marie, you can post a response if you wish."

# Example 5: Iterating through a list and using conditional statements to modify behavior
requested_toppings = ['mushrooms', 'extra cheese']
# List of available toppings
available_toppings = ['mushrooms', 'pepperoni', 'extra cheese', 'onions']
# Iterate through each requested topping and perform an action if it's in the list
for topping in requested_toppings:
    if topping in available_toppings:
        print(f"Adding {topping}.")
    else:
        print(f"Sorry, we ran out of {topping}.")  # Inform if topping is not available
print("Finished making your pizza!")  # Confirm completion after all toppings are added

# Example 6: Multiple Conditions with Logical Operators
user_age = 25
if 18 <= user_age < 65:
    print("You are an adult.")  # Check if the person is between 18 and 65 years old
elif user_age < 18:
    print("You are a minor.")
else:
    print("You are a senior.")

# Use Case: Handling Out of Stock Items and Empty Topping List
requested_toppings = []
if requested_toppings:
    print("\nMaking your pizza with the following toppings:")
    for topping in requested_toppings:
        if topping in available_toppings:
            print(f"Adding {topping}.")
        else:
            print(f"Sorry, we ran out of {topping}.")  # Inform if topping is not available
    print("Finished making your pizza!")
else:
    print("Sorry, we don't have any requested toppings.")

# New Use Case: Checking Topping Availability
available_toppings = ['mushroom', 'olive', 'green pepper', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushroom', 'french fries', 'extra cheese']

print("\nChecking requested toppings:")
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")
