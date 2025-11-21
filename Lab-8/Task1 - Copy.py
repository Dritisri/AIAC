import re
def valid_email(email):
    # Check for exactly one @
    if email.count('@') != 1:
        return False
    # Check for allowed characters and structure
    pattern = r'^[A-Za-z0-9][A-Za-z0-9._%+-]*@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    if not re.match(pattern, email):
        return False
    # Should not start or end with special characters
    if not (email[0].isalnum() and email[-1].isalnum()):
        return False
    return True
if __name__ == "__main__":
    emails = [
        # Test case1
        "Deeksha123.@gmail.com", #returns true
        # Test case2
        ".deeksha123.@gmail.com" #returns false
    ]
    for e in emails:
        print(f"{e}: {valid_email(e)}")

