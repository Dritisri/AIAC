def calculate_power_bill(units):
    """
    Calculates the power bill based on the number of units consumed.
    The rates can be adjusted as per the local electricity board.

    Example slab rates:
    - First 100 units: $0.5 per unit
    - Next 100 units (101-200): $0.75 per unit
    - Next 200 units (201-400): $1.20 per unit
    - Above 400 units: $1.50 per unit

    Args:
        units (float): Number of units consumed.

    Returns:
        float: Total bill amount.
    """
    bill = 0.0
    if units <= 100:
        bill = units * 0.5
    elif units <= 200:
        bill = 100 * 0.5 + (units - 100) * 0.75
    elif units <= 400:
        bill = 100 * 0.5 + 100 * 0.75 + (units - 200) * 1.20
    else:
        bill = 100 * 0.5 + 100 * 0.75 + 200 * 1.20 + (units - 400) * 1.50
    return bill

if __name__ == "__main__":
    try:
        units = float(input("Enter the number of units consumed: "))
        if units < 0:
            print("Units consumed cannot be negative.")
        else:
            total_bill = calculate_power_bill(units)
            print(f"Total power bill for {units} units: ${total_bill:.2f}")
    except ValueError:
        print("Invalid input. Please enter a numeric value for units.")
