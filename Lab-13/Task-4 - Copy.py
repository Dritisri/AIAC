"""Compute squares of numbers 1 through 10 using a loop and print them.

Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = []
# Use a for-loop to build the list of squares
for number in numbers:
    squares.append(number ** 2)
print(squares)