# Initial list of motorcycles.
motorcycles = ['honda', 'yamaha', 'suzuki']
print("Initial list:", motorcycles)

# Changing the first element of the list from 'honda' to 'ducati'.
motorcycles[0] = 'ducati'
print("After replacing 'honda' with 'ducati':", motorcycles)

# Adding 'honda' back to the end of the list.
motorcycles.append('honda')
print("After adding 'honda' back to the list:", motorcycles)

# Clearing the list and re-adding motorcycles.
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print("Rebuilt motorcycles list:", motorcycles)

# Insert 'ducati' at the beginning of the list.
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print("After inserting 'ducati' at the beginning:", motorcycles)

# Removing the first element using the del statement.
del motorcycles[0]
print("After deleting the first element:", motorcycles)

# Removing the last item from the list and saving it to a variable.
popped_motorcycle = motorcycles.pop()
print("After popping the last element:", motorcycles)
print("Popped motorcycle:", popped_motorcycle)

# Using pop to retrieve and report the last owned motorcycle.
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

# Using pop with an index to retrieve and report the first owned motorcycle.
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

# Removing an item by value where 'ducati' is specified directly.
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati')
print("After removing 'ducati' by value:", motorcycles)

# Removing an item by value stored in a variable and including a message.
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print("After removing a too expensive bike:", motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
