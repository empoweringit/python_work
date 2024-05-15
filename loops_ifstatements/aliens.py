# Alien Color Game Simulation

# Part 1: Alien Colors #1
# This part checks if the alien's color is 'green' and awards points accordingly.

# Version 1: Pass version (alien color is green)
# Initialize the alien color to 'green'
alien_color_pass = 'green'
# Check if the alien's color is 'green'
if alien_color_pass == 'green':
    # Output the message for earning 5 points because the condition is met
    print("You just earned 5 points!")

# Version 2: Fail version (alien color is not green)
# Initialize the alien color to 'red' to simulate a failing condition
alien_color_fail = 'red'
# There is no output because the color is not 'green', hence no if block is executed.

# Part 2: If-Else Chain
# This part extends the game by using an if-else structure to award different points depending on the alien's color.

# Version 1: If block execution (alien color is green)
# Set the alien color to 'green'
alien_color_if = 'green'
# Check if the alien's color is 'green'
if alien_color_if == 'green':
    # Since the condition is true, output the message for earning 5 points
    print("You earned 5 points for shooting the alien")
else:
    # This part does not execute because the if condition is true
    print("You earned 10 points for shooting the alien")

# Version 2: Else block execution (alien color is not green)
# Set the alien color to 'yellow'
alien_color_else = 'yellow'
# Check if the alien's color is 'green'
if alien_color_else == 'green':
    # This part does not execute because the condition is false
    print("You earned 5 points for shooting the alien")
else:
    # Since the if condition is false, this else part executes
    print("You earned 10 points for shooting the alien")

# Part 3: If-Elif-Else Chain
# This part involves multiple alien colors and assigns points based on the specific color.

# Set the alien color to 'green' to test the first condition
alien_color_green = 'green'
# Check the alien's color among 'green', 'yellow', or other
if alien_color_green == 'green':
    # The condition is met for green
    print("You just earned 5 points")
elif alien_color_green == 'yellow':
    # Not executed because the color is not yellow
    print("You just earned 10 points")
else:
    # Not executed because the color is neither yellow nor red
    print("You just earned 15 points")

# Set the alien color to 'yellow' to test the second condition
alien_color_yellow = 'yellow'
# Check the alien's color among 'green', 'yellow', or other
if alien_color_yellow == 'green':
    # Not executed because the color is not green
    print("You just earned 5 points")
elif alien_color_yellow == 'yellow':
    # The condition is met for yellow
    print("You just earned 10 points")
else:
    # Not executed because the color is neither green nor red
    print("You just earned 15 points")

# Set the alien color to 'red' to test the else condition
alien_color_red = 'red'
# Check the alien's color among 'green', 'yellow', or other
if alien_color_red == 'green':
    # Not executed because the color is not green
    print("You just earned 5 points")
elif alien_color_red == 'yellow':
    # Not executed because the color is not yellow
    print("You just earned 10 points")
else:
    # The else condition is met because the color is red
    print("You just earned 15 points")
