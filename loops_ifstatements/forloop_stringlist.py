# List of magicians with properly named variables in the loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:  # Changed iterator variable name to 'magician'
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!")

# Tuple of pizza brands with properly named variables in the loop
pizzas = ('primos', 'dominos', 'jets')  # Changed variable name to 'pizzas'
for pizza in pizzas:
    print(f"I like {pizza.title()} Pizza!")

print("I love Pizza so Much!")

# Tuple of animals with properly named variables in the loop
animals = ('dog', 'zebra', 'giraffe')  # Changed variable name to 'animals'
for animal in animals:
    print(f"A {animal.title()} would make a good pet.")

print("Any of these animals would make a great pet!")
