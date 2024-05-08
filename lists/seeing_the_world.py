# Step 1: Define the list of places
places = ['Italy', 'Greece', 'France', 'Nepal', 'Brazil']  # Nepal and Brazil represent beautiful countries in their respective regions

# Step 2: Print the original list
print("Original list:", places)

# Step 3: Print the list sorted alphabetically without modifying the original
print("Sorted list (alphabetically):", sorted(places))

# Step 4: Show that the original list is unchanged
print("Original list after sorted():", places)

# Step 5: Print the list sorted in reverse alphabetical order without modifying the original
print("Sorted list (reverse alphabetically):", sorted(places, reverse=True))

# Step 6: Reverse the order of the list and print it
places.reverse()
print("List after reverse():", places)

# Step 7: Reverse the order of the list again to show it's back to original
places.reverse()
print("List after second reverse():", places)

# Step 8: Sort the list alphabetically and show it has changed
places.sort()
print("List after sort() alphabetically:", places)

# Step 9: Sort the list in reverse alphabetical order and show it has changed
places.sort(reverse=True)
print("List after sort() in reverse alphabetical order:", places)
