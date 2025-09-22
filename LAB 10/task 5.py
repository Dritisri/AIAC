def calculate_squares(start: int, end: int) -> list:
    """
    Calculate the squares of numbers in a given range.

    Args:
        start (int): The starting number (inclusive).
        end (int): The ending number (exclusive).

    Returns:
        list: A list containing the squares of the numbers in the range.
    """
    return [n ** 2 for n in range(start, end)]

if __name__ == "__main__":
    # Define the range of numbers
    start_num = 1
    end_num = 1000000

    # Calculate squares using the function
    squares = calculate_squares(start_num, end_num)

    # Print the total number of squares calculated
    print(f"Total numbers squared: {len(squares)}")

    # Optionally, print the first 5 and last 5 squares to verify the results
    print("First 5 squares:", squares[:5])
    print("Last 5 squares:", squares[-5:])