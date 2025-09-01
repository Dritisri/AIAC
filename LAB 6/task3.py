# 1. Using nested if-elif-else conditionals

def classify_age_nested(age):
    if age >= 0:
        if age <= 12:
            return "Child"
        elif age <= 19:
            return "Teen"
        elif age <= 59:
            return "Adult"
        else:
            return "Senior"
    else:
        return "Invalid age"

# 2. Step-by-step explanation:
# - First, check if the age is non-negative (age >= 0).
# - If age is between 0 and 12 (inclusive), return "Child".
# - If age is between 13 and 19 (inclusive), return "Teen".
# - If age is between 20 and 59 (inclusive), return "Adult".
# - If age is 60 or above, return "Senior".
# - If age is negative, return "Invalid age".

# 3. Other approaches:

# a) Multiple independent if statements
def classify_age_multiple_if(age):
    if age < 0:
        return "Invalid age"
    if age <= 12:
        return "Child"
    if age <= 19:
        return "Teen"
    if age <= 59:
        return "Adult"
    return "Senior"

# b) Dictionary-based lookup (using ranges as keys is not possible, so use a function)
def classify_age_dict(age):
    age_groups = {
        "Child": range(0, 13),
        "Teen": range(13, 20),
        "Adult": range(20, 60),
        "Senior": range(60, 200)  # assuming max age 199
    }
    if age < 0:
        return "Invalid age"
    for group, ages in age_groups.items():
        if age in ages:
            return group
    return "Senior"  # for ages >= 200

# c) match-case (Python 3.10+)
def classify_age_match(age):
    if age < 0:
        return "Invalid age"
    match age:
        case _ if age <= 12:
            return "Child"
        case _ if age <= 19:
            return "Teen"
        case _ if age <= 59:
            return "Adult"
        case _:
            return "Senior"

# Example usage:
if __name__ == "__main__":
    test_ages = [-1, 5, 15, 30, 65]
    for age in test_ages:
        print(f"Age {age}: Nested: {classify_age_nested(age)}, Multiple If: {classify_age_multiple_if(age)}, Dict: {classify_age_dict(age)}, Match: {classify_age_match(age)}")