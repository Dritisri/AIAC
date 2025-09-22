def calculate_percentage(value: float, percent: float) -> float:
    """
    Calculate the percentage of a given value.

    Args:
        value (float): The base value.
        percent (float): The percentage to calculate.

    Returns:
        float: The calculated percentage of the value.
    """
    return value * percent / 100

amount = 200
percentage = 15

# Calculate 15% of 200
result = calculate_percentage(amount, percentage)
print(result)