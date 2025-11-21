class Student:
    def __init__(self, name: str, age: int, mark1: float, mark2: float, mark3: float) -> None:
        self.name = name
        self.age = age
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def print_details(self) -> None:
        print("Name:", self.name, "Age:", self.age)

    def calculate_total(self) -> float:
        return self.mark1 + self.mark2 + self.mark3

    def calculate_average(self) -> float:
        return self.calculate_total() / 3


if __name__ == "__main__":
    student = Student("Alice", 20, 85.0, 90.0, 88.0)
    student.print_details()
    print("Total:", student.calculate_total())
    print("Average:", student.calculate_average())

