def grade(score):
    """
    Assign a letter grade based on the numeric score.

    Args:
        score (int or float): The student's score.

    Returns:
        str: The letter grade corresponding to the score.
    """
    # Check the score against grade boundaries
    if score >= 90:
        return "A"  # Excellent
    elif score >= 80:
        return "B"  # Very Good
    elif score >= 70:
        return "C"  # Good
    elif score >= 60:
        return "D"  # Satisfactory
    else:
        return "F"  # Fail

if __name__ == "__main__":
    # List of student scores to grade
    scores = [95, 82, 76, 65, 54]

    # Iterate through each score and print the corresponding grade
    for s in scores:
        print(f"Score: {s} => Grade: {grade(s)}")