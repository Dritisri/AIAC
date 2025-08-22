class Student:
    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if self.marks >= 90:
            return 'A'
        elif self.marks >= 80:
            return 'B'
        elif self.marks >= 70:
            return 'C'
        elif self.marks >= 60:
            return 'D'
        else:
            return 'F'

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.rollno}")
        print(f"Marks: {self.marks}")
        print(f"Grade: {self.grade}")

if __name__ == "__main__":
    name = input("Enter student name: ")
    rollno = input("Enter roll number: ")
    marks = float(input("Enter marks: "))
    student = Student(name, rollno, marks)
    student.display_details()
