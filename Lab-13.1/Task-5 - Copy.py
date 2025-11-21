"""Search for an element using Pythonic containment instead of a manual loop.

This script replaces a nested/explicit search loop with the `in` keyword,
which is more readable and efficient for membership checks.

Expected output when searching for 30 in the list:
    Found
"""

items = [10, 20, 30, 40, 50]
found = 30 in items
print("Found" if found else "Not Found")
