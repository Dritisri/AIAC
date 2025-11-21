"""Compute squares of a list using a Pythonic list comprehension.

This module defines a helper function `square_all` and demonstrates refactoring
an explicit append loop into a list comprehension while preserving output.

Expected output:
    [1, 4, 9, 16, 25]
"""
def square_all(values):
    return [v ** 2 for v in values]
numbers = [1, 2, 3, 4, 5]
squares = square_all(numbers)
print(squares)