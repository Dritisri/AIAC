"""Safely access dictionary keys using .get() with a default value.

This script shows a Pythonic alternative to explicit membership checks by
using dict.get(key, default) to handle missing keys gracefully.

Expected output when 'Charlie' is missing:
    Not Found
"""

student_scores = {"Alice": 85, "Bob": 90}
print(student_scores.get("Charlie", "Not Found"))
