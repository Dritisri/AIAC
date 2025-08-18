def square(x):
    """
    Returns the square of a number.

    Args:
        x (int or float): The number to square.

    Returns:
        int or float: The square of x.
    """
    return x * x

def sum_of_squares(numbers):
    """
    Returns the sum of the squares of a list of numbers.

    Args:
        numbers (list of int or float): The numbers to square and sum.

    Returns:
        int or float: The sum of the squares of the numbers.
    """
    return sum(square(num) for num in numbers)
