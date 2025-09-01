
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

# Example usage
ages = [5, 15, 35, 65, -3]
for a in ages:
    print(f"Age {a}: {classify_age_nested(a)}")

print("\n--- Step-by-step Explanation ---")
print("""
The function classify_age_nested(age) works as follows:
1. It first checks if the age is non-negative (age >= 0).
2. If so, it checks if age is less than or equal to 12. If true, returns "Child".
3. If not, it checks if age is less than or equal to 19. If true, returns "Teen".
4. If not, it checks if age is less than or equal to 59. If true, returns "Adult".
5. If none of the above, it returns "Senior" (age >= 60).
6. If the age is negative, it returns "Invalid age".
""")

# 2. Using multiple independent if statements
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

print("--- Multiple independent if statements ---")
for a in ages:
    print(f"Age {a}: {classify_age_multiple_if(a)}")

# 3. Using dictionary-based lookup (with ranges)
def classify_age_dict(age):
    if age < 0:
        return "Invalid age"
    age_groups = {
        range(0, 13): "Child",
        range(13, 20): "Teen",
        range(20, 60): "Adult",
        range(60, 200): "Senior"  # assuming max age 199
    }
    for age_range, group in age_groups.items():
        if age in age_range:
            return group
    return "Senior"  # fallback for ages >= 200

print("--- Dictionary-based lookup ---")
for a in ages:
    print(f"Age {a}: {classify_age_dict(a)}")

# 4. Using match-case (Python 3.10+)
def classify_age_match(age):
    if age < 0:
        return "Invalid age"
    match age:
        case n if 0 <= n <= 12:
            return "Child"
        case n if 13 <= n <= 19:
            return "Teen"
        case n if 20 <= n <= 59:
            return "Adult"
        case n if n >= 60:
            return "Senior"

print("--- match-case (Python 3.10+) ---")
for a in ages:
    print(f"Age {a}: {classify_age_match(a)}")

