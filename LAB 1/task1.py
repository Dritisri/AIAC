
def is_valid_palindrome(s):
    # Remove spaces and convert to lowercase
    cleaned = ''.join(c.lower() for c in s if c != ' ')
    # Check if cleaned string is equal to its reverse
    return cleaned == cleaned[::-1]

# Example usage
input_str = input("Enter a string: ")
if is_valid_palindrome(input_str):
    print("Valid palindrome")
else:
    print("Not a palindrome")