def main():
    # Basic List Copying Demonstration
    def demonstrate_list_copying():
        my_foods = ['pizza', 'falafel', 'carrot cake']
        # Create a copy of the list using slicing
        friends_foods = my_foods[:]
        my_foods.append('cannoli')
        friends_foods.append('ice cream')

        print("My favorite foods are:")
        print(my_foods)
        print("\nMy friend's favorite foods are:")
        print(friends_foods)

    # Real-World Example 1: Managing Event Participants
    def manage_event_participants():
        base_participants = ['Alice', 'Bob', 'Charlie']
        event_a_participants = base_participants[:]
        event_b_participants = base_participants[:]

        event_a_participants.append('Dave')
        event_b_participants.remove('Charlie')

        print("\nEvent A participants:", event_a_participants)
        print("Event B participants:", event_b_participants)

    # Real-World Example 2: Customizing Marketing Materials
    def customize_marketing():
        base_messages = ['Buy now!', 'Sale ends soon!']
        west_region_messages = base_messages[:]
        east_region_messages = base_messages[:]

        west_region_messages.append('Free shipping in the West!')
        east_region_messages.append('East Coast special discount!')

        print("\nWest Region Messages:", west_region_messages)
        print("East Region Messages:", east_region_messages)

    # Real-World Example 3: Tracking Software Version Features
    def track_features():
        stable_features = ['login', 'search', 'checkout']
        beta_features = stable_features[:]

        beta_features.append('voice commands')

        print("\nStable Version Features:", stable_features)
        print("Beta Version Features:", beta_features)

    # Execute all functions
    demonstrate_list_copying()
    manage_event_participants()
    customize_marketing()
    track_features()

if __name__ == "__main__":
    main()
