import unittest
from Task1 import valid_email

class TestValidEmail(unittest.TestCase):
    def test_valid_email_simple(self):
        email = "user@example.com"
        result = valid_email(email)
        print(f"{email}: {result}")
        self.assertTrue(result)

    def test_valid_email_with_numbers(self):
        email = "user123@example.com"
        result = valid_email(email)
        print(f"{email}: {result}")
        self.assertTrue(result)

    def test_valid_email_with_dot(self):
        email = "first.last@example.co.uk"
        result = valid_email(email)
        print(f"{email}: {result}")
        self.assertTrue(result)

    def test_valid_email_with_underscore(self):
        email = "first_last@example.org"
        result = valid_email(email)
        print(f"{email}: {result}")
        self.assertTrue(result)

    def test_valid_email_with_plus(self):
        email = "user+tag@example.com"
        result = valid_email(email)
        print(f"{email}: {result}")
        self.assertTrue(result)

    def test_valid_email_with_hyphen(self):
        email = "user-name@example.com"
        result = valid_email(email)
        print(f"{email}: {result}")
        self.assertTrue(result)

    def test_valid_email_with_subdomain(self):
        email = "user@mail.example.com"
        result = valid_email(email)
        print(f"{email}: {result}")
        self.assertTrue(result)

    def test_valid_email_with_long_tld(self):
        email = "user@example.technology"
        result = valid_email(email)
        print(f"{email}: {result}")
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()