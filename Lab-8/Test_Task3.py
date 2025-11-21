import unittest
from Task3 import is_sentence_palindrome

class TestIsSentencePalindrome(unittest.TestCase):
    def test_simple_palindrome(self):
        self.assertTrue(is_sentence_palindrome("madam"))
        print("test_simple_palindrome")

    def test_sentence_palindrome(self):
        self.assertTrue(is_sentence_palindrome("A man a plan a canal Panama"))
        print("test_sentence_palindrome")

    def test_sentence_with_punctuation(self):
        self.assertTrue(is_sentence_palindrome("Was it a car or a cat I saw?"))
        print("test_sentence_with_punctuation")

    def test_sentence_with_mixed_case(self):
        self.assertTrue(is_sentence_palindrome("No lemon, no melon"))
        print("test_sentence_with_mixed_case")

    def test_not_palindrome(self):
        self.assertFalse(is_sentence_palindrome("This is not a palindrome"))
        print("test_not_palindrome")

    def test_empty_string(self):
        self.assertTrue(is_sentence_palindrome(""))
        print("test_empty_string")

    def test_single_character(self):
        self.assertTrue(is_sentence_palindrome("x"))
        print("test_single_character")

if __name__ == '__main__':
    unittest.main()