def assign_grade(score):
    if not isinstance(score, (int, float)):
        return "Invalid input: score must be a number."
    if score < 0 or score > 100:
        return "Invalid input: score must be between 0 and 100."

    if score >= 90:
        return 'Grade A'
    elif score >= 80:
        return 'Grade B'
    elif score >= 70:
        return 'Grade C'
    elif score >= 60:
        return 'Grade D'
    else:
        return 'Fail'
# test cases 1:
print(assign_grade(97)) #returns 'A'
# test cases 2:
print(assign_grade(85)) #returns 'B'
# test cases 3:
print(assign_grade(55)) #returns 'F'

