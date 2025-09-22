def welcome_student(name: str) -> None:
    """
    Print a personalized welcome message for a student.

    Args:
        name (str): The name of the student.
    """
    print(f"Welcome, {name}!")

def welcome_all_students(student_list):
    """
    Welcome each student in the provided list.

    Args:
        student_list (list): List of student names.
    """
    for student in student_list:
        welcome_student(student)

if __name__ == "__main__":
    # List of student names
    students = ["Alice", "Bob", "Charlie", "David", "Eva"]

    # Welcome each student using modular functions
    welcome_all_students(students)