# Initial dictionary creation for alien_0 with color and points
alien_0 = {'color': 'green', 'points': 5}

# Print the values associated with the keys 'color' and 'points'
print(alien_0['color'])   # Expected output: green
print(alien_0['points'])  # Expected output: 5

# Accessing the points value and printing a formatted string with the points
new_points = alien_0['points']
print(f"You just earned {new_points} points!")  # Expected output: You just earned 5 points!

# Adding new key-value pairs for the alien's position
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)  # Expected output: {'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}

# Resetting alien_0 dictionary to empty
alien_0 = {}

# Re-adding keys 'color' and 'points' to the dictionary
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)  # Expected output: {'color': 'green', 'points': 5}

# Changing the alien's color and printing the updates
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")  # Expected output: The alien is green.
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")  # Expected output: The alien is now yellow.

# Initializing alien_0 with position and speed attributes
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original Position: {alien_0['x_position']}")  # Expected output: Original Position: 0

# Move the alien to the right based on its speed
# Determine the increment based on the alien's speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien
    x_increment = 3

# Update the alien's x_position by adding the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f'New Position: {alien_0["x_position"]}')  # Expected output: New Position: 2

# Deleting a key-value pair from the dictionary
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)  # Expected output: {'color': 'green', 'points': 5}

# Delete the key 'points'
del alien_0['points']
print(alien_0)  # Expected output: {'color': 'green'}

# Using the get method to handle missing keys
alien_0 = {'color': 'green', 'speed': 'slow'}

# Use get method to safely access a key that might not exist
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)  # Expected output: No point value assigned.


