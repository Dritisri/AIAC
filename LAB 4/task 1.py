def is_valid_indian_mobile(number):
    """
    Validates if the given number is a valid Indian mobile number.
    Conditions:
    - Must be a string of exactly 10 digits.
    - Must start with 6, 7, 8, or 9.
    """
    return (
        isinstance(number, str) and
        len(number) == 10 and
        number.isdigit() and
        number[0] in {'6', '7', '8', '9'}
    )

# Example usage:
user_input = input("Enter a mobile number: ")
if is_valid_indian_mobile(user_input):
    print("Valid Indian mobile number.")
else:
    print("Invalid Indian mobile number.")