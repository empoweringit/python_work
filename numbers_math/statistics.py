def main():
    # Demonstrating basic list statistics with Python's built-in functions
    def basic_list_statistics(digits):
        """Display basic statistics of a list."""
        print("Digits:", digits)
        print("Minimum value:", min(digits))
        print("Maximum value:", max(digits))
        print("Sum of values:", sum(digits))

    # Analyzing financial transactions
    def financial_data_analysis(transactions):
        """Analyze financial transactions for min, max, and total."""
        print("\nTransactions:", transactions)
        print("Largest transaction:", max(transactions))
        print("Smallest transaction:", min(transactions))
        print("Total value of transactions:", sum(transactions))

    # Monitoring environmental temperatures
    def temperature_analysis(temperatures):
        """Analyze a list of temperatures."""
        print("\nTemperatures:", temperatures)
        print("Highest temperature:", max(temperatures))
        print("Lowest temperature:", min(temperatures))
        print("Total of all recorded temperatures:", sum(temperatures))

    # Evaluating class performance through test scores
    def class_performance(scores):
        """Evaluate class performance based on scores."""
        print("\nScores:", scores)
        print("Highest score:", max(scores))
        print("Lowest score:", min(scores))
        print("Sum of all scores:", sum(scores))

    # Basic usage of list statistics
    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    basic_list_statistics(digits)

    # Real-world example applications
    transactions = [200, -150, 400, -50, 1000]
    financial_data_analysis(transactions)

    temperatures = [22, 24, 19, 24, 30, 16, 25]
    temperature_analysis(temperatures)

    scores = [88, 92, 78, 90, 89, 84, 75]
    class_performance(scores)

if __name__ == "__main__":
    main()
