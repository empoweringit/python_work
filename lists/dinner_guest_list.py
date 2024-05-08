# Method 1: Managing the Guest List with Invitations

# Step 1: Creating the initial guest list
guests = ['Albert Einstein', 'Marie Curie', 'Isaac Newton']

# Print individual invitations and initial count
print("Initially inviting {} people to the dinner party:".format(len(guests)))
for guest in guests:
    print(f"Dear {guest}, you are cordially invited to a dinner party at my residence.")

# Step 2: Modifying the guest list
# Isaac Newton can't make it, replace him with Nikola Tesla
guests[2] = 'Nikola Tesla'

# Update and print new invitations
print("\nUnfortunately, Isaac Newton can't make it to the dinner.")
for guest in guests:
    print(f"Dear {guest}, you are still invited to the dinner party.")

# A bigger table is available
print("\nGreat news! A bigger table is available, so more guests can join.")
guests.insert(0, 'Ada Lovelace')
guests.insert(2, 'Charles Darwin')
guests.append('Stephen Hawking')

# Print new set of invitations with updated count
print(f"\nNow inviting {len(guests)} people to the dinner party:")
for guest in guests:
    print(f"Dear {guest}, you are cordially invited to a dinner party at my residence.")

# Shrinking the guest list due to table size constraint
print("\nUnfortunately, the bigger table won't arrive on time, and we can only have 2 guests.")
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Dear {removed_guest}, we are very sorry but there's no longer space at the dinner party.")

# Final invitations with updated count
print(f"\nNow only {len(guests)} people can still attend:")
for guest in guests:
    print(f"Dear {guest}, you are still invited to the dinner party.")

# Clearing the list and confirming it is empty
guests.clear()
print(f"\nThe guest list is now empty: {guests}")





# Method 2 --> advanced
# Step 1: Creating the initial guest list
guests = ['Albert Einstein', 'Marie Curie', 'Isaac Newton']
for guest in guests:
    print(f"Dear {guest}, you are cordially invited to a dinner party at my residence.")

# Step 2: Modifying the guest list
# Assume that Isaac Newton can't make it; replace him with Nikola Tesla
guests[2] = 'Nikola Tesla'
print("\nUnfortunately, Isaac Newton can't make it to the dinner.")
for guest in guests:
    print(f"Dear {guest}, you are cordially invited to a dinner party at my residence.")

# Step 3: Expanding the guest list
# A bigger table is now available
print("\nGreat news! A bigger table is available, so more guests can join.")
guests.insert(0, 'Ada Lovelace')  # Adds a new guest at the beginning
guests.insert(len(guests) // 2, 'Charles Darwin')  # Adds a new guest in the middle
guests.append('Stephen Hawking')  # Adds a new guest at the end
for guest in guests:
    print(f"Dear {guest}, you are cordially invited to a dinner party at my residence.")

# Step 4: Shrinking the guest list
# We only have space for 2 guests now
print("\nUnfortunately, the bigger table won't arrive on time, and we can only have 2 guests.")
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Dear {removed_guest}, we are very sorry but there's no longer space at the dinner party.")

# Inform the remaining guests that they are still invited
for guest in guests:
    print(f"Dear {guest}, you are still invited to the dinner party.")

# Finally, clear the list
del guests[:]
print("\nThe guest list is now empty:", guests)
