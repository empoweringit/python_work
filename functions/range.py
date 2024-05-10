# Printing values from 1 to 4
for value in range(1, 5):
    print(value)

# Printing values from 1 to 5
for value in range(1, 6):
    print(value)

# Printing values from 0 to 5
for value in range(6):
    print(value)

# Creating a list of numbers from 1 to 5 and printing the list
numbers = list(range(1, 6))
print(numbers)  # Fixed indentation

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

squares = []
for value in range(1, 11):
    squares.append(value ** 2)

print(squares)

from random import randint

def main():
    # Demonstrating Basic Usage of range()
    print("Simple range from 0 to 9:", list(range(10)))
    print("Range from 50 to 55:", list(range(50, 56)))
    print("Range from 100 to 110, step by 2:", list(range(100, 111, 2)))

    # Real-World Example 1: Generating IDs for New Users
    def generate_user_ids(start_id, num_users):
        """Generates a specified number of user IDs starting from a given ID."""
        return list(range(start_id, start_id + num_users))

    user_ids = generate_user_ids(1001, 10)
    print("Generated User IDs:", user_ids)

    # Real-World Example 2: Creating Time Slots for Appointments
    def create_time_slots(start_hour, end_hour, duration_minutes):
        """Creates a list of time slots between start and end hours, spaced by duration."""
        return [f"{hour // 60}:{str(hour % 60).zfill(2)}" for hour in range(start_hour * 60, end_hour * 60, duration_minutes)]

    time_slots = create_time_slots(9, 17, 30)
    print("Time Slots:", time_slots)

    # Real-World Example 3: Simulating Sensor Data Readings
    def simulate_sensor_readings(num_readings):
        """Simulates sensor data readings over a period."""
        return [randint(100, 200) for _ in range(num_readings)]

    sensor_data = simulate_sensor_readings(20)
    print("Sensor Data Readings:", sensor_data)

if __name__ == "__main__":
    main()
