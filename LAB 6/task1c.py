class Student:
    def __init__(self, name, age, grade):
        # initialize attributes here
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        # print student details
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

    def is_passed(self):
        # return True if grade >= 40
        return self.grade >= 40

# Example usage to display output
student1 = Student("Alice", 20, 85)
student2 = Student("Bob", 19, 35)

student1.display_info()
print("Passed:", student1.is_passed())

student2.display_info()
print("Passed:", student2.is_passed())
