# Voting and Admission Cost Script

# Voting eligibility check for an 19-year-old
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

# Voting eligibility check for a 17-year-old
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, You are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

# Admission cost calculation based on age
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

# Consolidated admission price calculation with comprehensive age brackets
age = 12  # This variable is reset here for demonstration; typically, it would be input or retrieved from user data
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f"Your admission cost is ${price}.")

# Correction for the repeated age and price calculations
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
print(f"Your admission cost is ${price}.")
