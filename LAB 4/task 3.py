def extract_student_info(student):
    first_name = student.get("personal", {}).get("first_name", "")
    last_name = student.get("personal", {}).get("last_name", "")
    branch = student.get("academic", {}).get("branch", "")
    sgpa = student.get("academic", {}).get("sgpa", "")
    full_name = f"{first_name} {last_name}".strip()
    return f"Full Name: {full_name}, Branch: {branch}, SGPA: {sgpa}"

# Example usage:
student1 = {
    "personal": {"first_name": "Amit", "last_name": "Sharma"},
    "academic": {"branch": "CSE", "sgpa": 8.7}
}
student2 = {
    "personal": {"first_name": "Riya", "last_name": "Verma"},
    "academic": {"branch": "ECE", "sgpa": 9.2}
}

print(extract_student_info(student1))
print(extract_student_info(student2))