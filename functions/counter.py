from collections import Counter

# Function to count character frequencies in a string
def character_frequency(text):
    """Returns the frequency of each character in the given string."""
    # Counter tallies occurrences of each character automatically.
    return Counter(text)

# Function to update inventory with new items using Counter
def update_inventory(current_inventory, additions):
    """Updates the inventory count given a list of new items."""
    # Update method adds counts from 'additions' to 'current_inventory'.
    current_inventory.update(additions)
    return current_inventory

# Function to analyze word frequency in a given text
def word_frequency(text):
    """Returns the frequency of each word in the given text."""
    # Text is split into words, and Counter tallies each word's occurrences.
    words = text.split()
    return Counter(words)

# Function to count votes in a voting system
def count_votes(vote_list):
    """Counts votes for each candidate and returns the results."""
    # Counter tallies votes for each candidate from 'vote_list'.
    return Counter(vote_list)

# Main block to demonstrate the functions
if __name__ == "__main__":
    # Using the character frequency function
    sample_text = "hello world"
    frequency = character_frequency(sample_text)
    print("Character Frequencies:", frequency)

    # Using the inventory management function
    initial_inventory = Counter(['apple', 'orange', 'banana'])
    new_stock = ['apple', 'apple', 'banana', 'orange', 'pear']
    updated_inventory = update_inventory(initial_inventory, new_stock)
    print("Updated Inventory:", updated_inventory)

    # Using the word frequency function
    sample_phrase = "the quick brown fox jumps over the lazy dog the dog slept"
    word_freq = word_frequency(sample_phrase)
    print("Word Frequencies:", word_freq)

    # Using the vote counting function
    votes = ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob', 'Bob']
    vote_counts = count_votes(votes)
    print("Vote Counts:", vote_counts)
