
def calculate_electricity_bill(units, tax_rate=0.10):
    """
    Calculates the electricity bill with tiered rates and tax.
    Returns a breakdown of the costs.

    Args:
        units (float): Number of units consumed.
        tax_rate (float): Tax rate as a decimal (e.g., 0.10 for 10%).

    Returns:
        dict: Breakdown of the bill with keys:
            - 'energy_charge'
            - 'tax'
            - 'total'
    Raises:
        ValueError: If units is negative or not a number.
    """
    # Input validation
    if not isinstance(units, (int, float)):
        raise ValueError("Units consumed must be a numeric value.")
    if units < 0:
        raise ValueError("Units consumed cannot be negative.")

    # Tiered rates
    energy_charge = 0.0
    if units <= 100:
        energy_charge = units * 0.5
    elif units <= 200:
        energy_charge = 100 * 0.5 + (units - 100) * 0.75
    elif units <= 400:
        energy_charge = 100 * 0.5 + 100 * 0.75 + (units - 200) * 1.20
    else:
        energy_charge = 100 * 0.5 + 100 * 0.75 + 200 * 1.20 + (units - 400) * 1.50

    tax = energy_charge * tax_rate
    total = energy_charge + tax

    return {
        'energy_charge': round(energy_charge, 2),
        'tax': round(tax, 2),
        'total': round(total, 2)
    }

if __name__ == "__main__":
    try:
        user_input = input("Enter the number of units consumed: ")
        units = float(user_input)
        breakdown = calculate_electricity_bill(units)
        print("\nElectricity Bill Breakdown:")
        print(f"  Energy Charge : ${breakdown['energy_charge']:.2f}")
        print(f"  Tax (10%)     : ${breakdown['tax']:.2f}")
        print(f"  Total Bill    : ${breakdown['total']:.2f}")
    except ValueError as ve:
        print(f"Invalid input: {ve}")
