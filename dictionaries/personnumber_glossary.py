"""
This program performs the following tasks:
1. Stores and prints information about a person using a dictionary.
2. Stores and prints people's favorite numbers using a dictionary.
3. Creates a glossary of programming terms and prints them with their meanings.
"""

# Task 1: Store Information About a Person
def person_info():
    person = {
        'first_name': 'John',
        'last_name': 'Doe',
        'age': 30,
        'city': 'New York'
    }

    print("Person Information:")
    print(f"First name: {person['first_name']}")
    print(f"Last name: {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")
    print("\n")

# Task 2: Store People's Favorite Numbers
def favorite_numbers_info():
    favorite_numbers = {
        'alice': 5,
        'bob': 12,
        'charlie': 7,
        'diana': 9,
        'eve': 3
    }

    print("Favorite Numbers:")
    for name, number in favorite_numbers.items():
        print(f"{name.title()}'s favorite number is {number}.")
    print("\n")

# Task 3: Glossary of Programming Words
def programming_glossary():
    glossary = {
        'variable': 'A reserved memory location to store values.',
        'function': 'A block of code which only runs when it is called.',
        'loop': 'A sequence of instructions that is continually repeated until a certain condition is reached.',
        'dictionary': 'A collection of key-value pairs.',
        'list': 'A collection of ordered items that can be of different types.'
    }

    print("Programming Glossary:")
    for word, meaning in glossary.items():
        print(f"\n{word.title()}:\n{meaning}")

# Execute all functions
if __name__ == "__main__":
    person_info()
    favorite_numbers_info()
    programming_glossary()
