# List of bicycle brands.
bicycles = ['trek', 'cannondale', 'redline', 'specialized']

# Printing the entire list of bicycles.
print("List of bicycles:", bicycles)

# Accessing and printing the first item in the list (index 0).
print("First bicycle:", bicycles[0])

# Printing the first bicycle's name in title case.
print("First bicycle title cased:", bicycles[0].title())

# Accessing and printing the second item in the list (index 1).
print("Second bicycle:", bicycles[1])

# Accessing and printing the fourth item in the list (index 3).
print("Fourth bicycle:", bicycles[3])

# Accessing and printing the last item using negative indexing.
print("Last bicycle using negative index:", bicycles[-1])

# Accessing and printing the third last item using negative indexing.
print("Third last bicycle using negative index:", bicycles[-3])

# Constructing and printing a message about the first bicycle.
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)
