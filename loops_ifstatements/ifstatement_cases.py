# List of car brands for demonstration
cars = ['audi', 'bmw', 'subaru', 'toyota']

# Iterate through each car in the list
for car in cars:
    # Check if the current car is 'bmw'
    if car == 'bmw':
        print(car.upper())  # Outputs 'BMW' - car is 'bmw', so this is an uppercase transformation
    else:
        print(car.title())  # Outputs the car name with the first letter capitalized, as it's not 'bmw'

# Testing string comparison and assignment in Python
car = 'bmw'
print(f"Is the car 'bmw'? {car == 'bmw'}")  # True - because car is exactly 'bmw'

car = 'audi'
print(f"Is the car still 'bmw'? {car == 'bmw'}")  # False - car has been reassigned to 'audi'

car = 'Audi'
print(f"Is 'Audi' equal to 'audi'? {car == 'audi'}")  # False - Python is case-sensitive

car = 'Audi'
print(f"Does 'Audi'.lower() equal 'audi'? {car.lower() == 'audi'}")  # True - 'Audi' converted to lowercase is 'audi'

# Testing numerical comparisons and logical operators
age = 18
print(f"Is age exactly 18? {age == 18}")  # True - age is initially set to 18
age = 19
print(f"Is age less than 21? {age < 21}")  # True - age is now 19, which is less than 21
print(f"Is age less than or equal to 21? {age <= 21}")  # True - age is still less than 21
print(f"Is age greater than 21? {age > 21}")  # False - age is less than 21
print(f"Is age greater than or equal to 21? {age >= 21}")  # False - age is less than 21

age_0 = 22
age_1 = 18
print(f"Are both ages 22 and 18 greater than or equal to 21? {age_0 >= 21 and age_1 >= 21}")  # False - age_1 is 18, not >= 21

age_1 = 22
print(f"Are both ages 22 now greater than or equal to 21? {age_0 >= 21 and age_1 >= 21}")  # True - both are now 22

age_0 = 22
age_1 = 18
print(f"Is at least one age greater than or equal to 21? {age_0 >= 21 or age_1 >= 21}")  # True - age_0 is 22, so at least one condition is true

age_0 = 18
print(f"Is at least one age greater than or equal to 21 now? {age_0 >= 21 or age_1 >= 21}")  # False - neither age is >= 21

# Testing boolean variables with logical operators
game_active = True
can_edit = False
print(f"Is the game active and can edit? {game_active and can_edit}")  # False - can_edit is False
print(f"Is the game active or can edit? {game_active or can_edit}")   # True - game_active is True

# This structured approach clarifies the logical checks and outcomes, making it ideal for educational purposes or debugging.

