# Example Python script demonstrating various conditional logic operations

# Example 1: Checking for Equality and Inequality with Strings
requested_topping = 'mushroom'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")  # Output: Hold the anchovies!
# This checks if the topping requested is not 'anchovies'. Since it's 'mushroom', the condition is true.

# Example 2: Nested Conditional Statements
answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")  # Output: That is not the correct answer. Please try again!
# This nested if statement checks if the answer is not 42, which is true here.

# Example 3: Checking Membership in a List
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)  # Outputs: True
print('pepperoni' in requested_toppings)  # Outputs: False
# These membership checks quickly determine if certain items are in the list of toppings.

# Example 4: Using `not in` to Check Non-Membership
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")  # Output: Marie, you can post a response if you wish.
# This checks if 'marie' is not in the list of banned users. Since she isn't, she's allowed to post a response.

# Combined, these examples show various ways to use conditional logic in Python to make decisions based on the values of variables.


requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("add pepperoni.")
if 'extra cheese' in requested_toppings:
    print("adding extra cheese.")

print("\Finished making your pizza!")