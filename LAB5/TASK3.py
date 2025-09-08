def fibonacci(n):
    """
    Calculate the nth Fibonacci number using recursion.

    Args:
        n (int): The position in the Fibonacci sequence (0-indexed).

    Returns:
        int: The nth Fibonacci number.
    """
    # Base case: The 0th Fibonacci number is 0
    if n == 0:
        return 0
    # Base case: The 1st Fibonacci number is 1
    elif n == 1:
        return 1
    else:
        # Recursive case: Sum of the two preceding numbers
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage:
print(fibonacci(5))  # Output: 5