# List of names.
names = ['Dominique', 'Charlie', 'Greysen', 'Austin', 'Lazar', 'Chuck', 'Jeff', 'Patrick', 'Dre', 'Jade', 'Malik', 'Dean', 'Mom', 'Dad', 'Uncle Scott', 'Papa', 'Bramble Jam']

# Loop through each name and print a personalized greeting.
for name in names:
    # Format the greeting message using f-string.
    message = f"Hello {name}! It's great to see you."
    print(message)


# List of various modes of transportation.
transport_modes = ['car', 'bike', 'bus', 'train', 'airplane', 'boat', 'scooter', 'subway']

# Access the first mode of transportation and print it.
print("First mode of transportation:", transport_modes[0])

# Add a new mode of transportation to the list.
transport_modes.append('hoverboard')
print("Updated transport modes:", transport_modes)

# Slice the list to get the first three modes and print them.
first_three_modes = transport_modes[:3]
print("First three modes of transportation:", first_three_modes)

# Loop through each mode and print it.
print("All modes of transportation:")
for mode in transport_modes:
    print(mode)

# Print a personalized message for each mode of transportation.
print("Personalized messages for each transportation mode:")
for mode in transport_modes:
    print(f"I love traveling by {mode}!")

# Define a list of favorite transportation modes.
favorites = ['bike', 'boat']

# Check each mode and print if it is a favorite.
print("Favorite transportation modes:")
for mode in transport_modes:
    if mode in favorites:
        print(f"{mode} is one of my favorite modes of transportation!")

# Create a new list with only the favorite modes in uppercase.
favorite_upper = [mode.upper() for mode in transport_modes if mode in favorites]
print("Favorites in uppercase:", favorite_upper)
