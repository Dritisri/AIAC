def sum_even_odd():
    """Read space-separated integers from stdin and return sums of even/odd.

    Prompts the user to enter integers separated by spaces. The input is
    validated so that any non-integer value results in a friendly error
    message and a `(None, None)` return value to indicate failure.

    Returns:
        tuple[int | None, int | None]:
            A pair `(sum_even, sum_odd)` when parsing succeeds; otherwise
            `(None, None)` if the input contains invalid (non-integer) data.
    """
    # Prompt for input as a single line of space-separated values
    user_input = input("Enter numbers separated by spaces: ")
    try:
        # Split by whitespace and convert each token to an integer
        numbers = [int(x) for x in user_input.split()]
    except ValueError:
        # At least one token was not an integer; inform the user and bail out
        print("Invalid input! Please enter only numbers.")
        return None, None
    # Initialize running totals for even and odd numbers
    sum_even = 0
    sum_odd = 0
    # Accumulate sums based on parity of each number
    for num in numbers:
        if num % 2 == 0:
            sum_even += num
        else:
            sum_odd += num
    # Return both computed totals as a tuple
    return sum_even, sum_odd
if __name__ == "__main__":
    # Execute only when run as a script, not when imported
    even_sum, odd_sum = sum_even_odd()
    if even_sum is not None and odd_sum is not None:
        print(f"Sum of even numbers: {even_sum}")
        print(f"Sum of odd numbers: {odd_sum}")
