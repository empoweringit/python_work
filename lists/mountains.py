# Step 1: Create a list of mountains
mountains = ['Everest', 'K2', 'Kangchenjunga', 'Lhotse', 'Makalu']

# Step 2: Print the original list
print("Original list of mountains:", mountains)

# Step 3: Modify elements in the list
mountains[4] = 'Cho Oyu'  # Replace 'Makalu' with 'Cho Oyu'
print("Modified list of mountains:", mountains)

# Step 4: Add elements to the list
mountains.append('Makalu')  # Add 'Makalu' back to the list at the end
mountains.insert(0, 'Annapurna')  # Insert 'Annapurna' at the beginning
print("List after adding elements:", mountains)

# Step 5: Remove elements from the list
removed_mountain = mountains.pop()  # Remove the last item and store it
mountains.remove('Annapurna')  # Remove 'Annapurna' by value
print("List after removing elements:", mountains)
print("Removed mountain:", removed_mountain)

# Step 6: Sort and reverse the list
mountains.sort()  # Sort the list alphabetically
print("List sorted alphabetically:", mountains)
mountains.sort(reverse=True)  # Sort the list in reverse alphabetical order
print("List sorted in reverse alphabetical order:", mountains)
mountains.reverse()  # Reverse the current order of the list
print("List after reversing:", mountains)

# Step 7: Use list comprehensions to create a new list
high_mountains = [mountain for mountain in mountains if 'a' in mountain]
print("High mountains (contains letter 'a'):", high_mountains)

# Demonstrating other list methods
print("Number of mountains in the list:", len(mountains))  # Print the number of elements in the list
