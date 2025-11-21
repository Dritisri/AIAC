import unittest
from Task2 import assign_grade

class TestAssignGrade(unittest.TestCase):
    def test_grade_A(self):
        for score in [ 97]:
            result = assign_grade(score)
            print(f"assign_grade({score}) = {result}")
            self.assertEqual(result, 'Grade A')

    def test_grade_B(self):
        for score in [89]:
            result = assign_grade(score)
            print(f"assign_grade({score}) = {result}")
            self.assertEqual(result, 'Grade B')

    def test_grade_C(self):
        for score in [ 75]:
            result = assign_grade(score)
            print(f"assign_grade({score}) = {result}")
            self.assertEqual(result, 'Grade C')

    def test_grade_D(self):
        for score in [66]:
            result = assign_grade(score)
            print(f"assign_grade({score}) = {result}")
            self.assertEqual(result, 'Grade D')

    def test_fail(self):
        for score in [55]:
            result = assign_grade(score)
            print(f"assign_grade({score}) = {result}")
            self.assertEqual(result, 'Fail')

    def test_invalid_negative(self):
        result = assign_grade(-5)
        print(f"assign_grade(-5) = {result}")
        self.assertEqual(result, "Invalid input: score must be between 0 and 100.")

    def test_invalid_above_100(self):
        result = assign_grade(105)
        print(f"assign_grade(105) = {result}")
        self.assertEqual(result, "Invalid input: score must be between 0 and 100.")

    def test_invalid_string(self):
        result = assign_grade("eighty")
        print(f"assign_grade('eighty') = {result}")
        self.assertEqual(result, "Invalid input: score must be a number.")

    def test_invalid_none(self):
        result = assign_grade(None)
        print(f"assign_grade(None) = {result}")
        self.assertEqual(result, "Invalid input: score must be a number.")

if __name__ == '__main__':
    unittest.main()