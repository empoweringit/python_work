# List of car brands with a typo in 'audi'.
cars = ['bmw', 'audi', 'toyota', 'subaru']

# Sorting the list in alphabetical order and printing.
cars.sort()
print("Sorted list:", cars)

# Re-initializing the list to correct the previous typo.
cars = ['bmw', 'audi', 'toyota', 'subaru']

# Sorting the list in reverse alphabetical order and printing.
cars.sort(reverse=True)
print("Sorted list in reverse order:", cars)

# Displaying the original list after sorting in reverse.
print("\nHere is the original list after sorting in reverse:")
print(cars)

# Showing the list sorted temporarily in alphabetical order.
print("\nHere is the sorted list in alphabetical order:")
print(sorted(cars))

# Showing the original list remains unchanged after using sorted().
print("\nHere is the original list again:")
print(cars)

# Reversing the list and showing before and after.
print("\nReversing the list:")
cars = ['bmw', 'audi', 'toyota', 'subaru']  # Re-initializing to correct the previous order.
print("Original list:", cars)
cars.reverse()
print("List after reversing:", cars)

# Displaying the length of the list.
print("\nThe length of the list is:", len(cars))
