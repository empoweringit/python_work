"""
This module contains examples of using conditionals, loops, and user validation in Python.
"""

# Part 1: Greeting Users
def greet_users(usernames_list):
    """
    Function to greet users, providing a special greeting for the admin.
    """
    if usernames_list:
        for user in usernames_list:
            if user.lower() == 'admin':
                print("Hello admin, would you like to see a status report?")
            else:
                print(f"Hello {user}, thank you for logging in again.")
    else:
        print("We need to find some users!")

# List of usernames including 'admin'
usernames = ['admin', 'alice', 'bob', 'charlie', 'diana']
greet_users(usernames)

# Part 2: Handling an Empty User List
def check_empty_user_list(usernames_list):
    """
    Function to check if the user list is empty and print a corresponding message.
    """
    if not usernames_list:
        print("We need to find some users!")

# Empty the list and check again
usernames = []
check_empty_user_list(usernames)

# Part 3: Ensuring Unique Usernames
def ensure_unique_usernames(current_user_list, new_user_list):
    """
    Function to ensure that new usernames are unique compared to current usernames.
    """
    current_users_lower = [user.lower() for user in current_user_list]

    for new_user in new_user_list:
        if new_user.lower() in current_users_lower:
            print(f"Username '{new_user}' is already taken, please enter a new username.")
        else:
            print(f"Username '{new_user}' is available.")

# List of current and new users
current_users = ['alice', 'bob', 'charlie', 'diana', 'eve']
new_users = ['frank', 'Gina', 'ALICE', 'harry', 'bob']
ensure_unique_usernames(current_users, new_users)

# Part 4: Printing Ordinal Numbers
def print_ordinal_numbers(number_list):
    """
    Function to print numbers with their ordinal suffixes.
    """
    for num in number_list:
        if num == 1:
            print("1st")
        elif num == 2:
            print("2nd")
        elif num == 3:
            print("3rd")
        else:
            print(f"{num}th")

# List of numbers from 1 to 9
numbers = list(range(1, 10))
print_ordinal_numbers(numbers)

# Additional Functionality for Training Purposes

# Function to add users
def add_users(user_list, new_user_list):
    """
    Function to add new users to the user list.
    """
    user_list.extend(new_user_list)
    return user_list

# Adding new users and greeting them
usernames = add_users(usernames, ['john', 'jane'])
greet_users(usernames)

# Function to remove a user
def remove_user(user_list, user_to_remove):
    """
    Function to remove a user from the user list.
    """
    if user_to_remove in user_list:
        user_list.remove(user_to_remove)
    else:
        print(f"User {user_to_remove} not found.")
    return user_list

# Removing a user and checking the list
usernames = remove_user(usernames, 'john')
greet_users(usernames)

# Function to check if a user is in the list
def check_user(user_list, user_to_check):
    """
    Function to check if a user is in the user list.
    """
    if user_to_check in user_list:
        print(f"User {user_to_check} is in the list.")
    else:
        print(f"User {user_to_check} is not in the list.")

# Check for specific users
check_user(usernames, 'jane')
check_user(usernames, 'john')

# Detailed Docstrings for Better Understanding
"""
Functions:

1. greet_users(usernames_list):
- Greets each user in the list.
- Special greeting for 'admin'.

2. check_empty_user_list(usernames_list):
- Checks if the user list is empty.

3. ensure_unique_usernames(current_user_list, new_user_list):
- Ensures new usernames are unique.

4. print_ordinal_numbers(number_list):
- Prints numbers with their ordinal suffixes.

5. add_users(user_list, new_user_list):
- Adds new users to the user list.

6. remove_user(user_list, user_to_remove):
- Removes a user from the user list.

7. check_user(user_list, user_to_check):
- Checks if a user is in the user list.
"""
