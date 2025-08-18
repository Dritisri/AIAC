def factorial(n):
    """
    Compute the factorial of a non-negative integer n using recursion.

    Parameters:
    n (int): A non-negative integer whose factorial is to be computed.

    Returns:
    int: The factorial of n.

    Raises:
    ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1
    return n * factorial(n - 1)

num = int(input("Enter a non-negative integer to compute its factorial: "))
try:
    print(f"Factorial of {num} is {factorial(num)}")
except ValueError as e:
    print(e)


