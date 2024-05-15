# Example 1: Checking for Equality and Inequality with Strings
requested_topping = 'mushroom'
# Checks if the requested topping is not 'anchovies'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")  # Expected output: "Hold the anchovies!"

# Example 2: Checking for an incorrect answer using a nested conditional
answer = 17
# This checks if the provided answer is not equal to the expected answer (42)
if answer != 42:
    print("That is not the correct answer. Please try again!")  # Expected output: "That is not the correct answer. Please try again!"

# Example 3: Using membership tests with lists
requested_toppings = ['mushrooms', 'onions', 'pineapple']
# Check if 'mushrooms' and 'pepperoni' are in the list of requested toppings
print('mushrooms' in requested_toppings)  # Outputs: True
print('pepperoni' in requested_toppings)  # Outputs: False

# Example 4: Using `not in` to check for non-membership
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
# Checks if 'marie' is not in the list of banned users
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")  # Expected output: "Marie, you can post a response if you wish."

# Example 5: Iterating through a list and using conditional statements to modify behavior
requested_toppings = ['mushrooms', 'extra cheese']
# Iterate through each requested topping and perform an action if it's in the list
for topping in requested_toppings:
    print(f"Adding {topping}.")
print("Finished making your pizza!")  # Confirm completion after all toppings are added

# Example 6: Multiple Conditions with Logical Operators
age = 25
if age >= 18 and age < 65:
    print("You are an adult.")  # This checks if the person is between 18 and 65 years old
elif age < 18:
    print("You are a minor.")
else:
    print("You are a senior.")

