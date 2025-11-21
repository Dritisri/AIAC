"""Build a sentence from words using a Pythonic join operation.

This module demonstrates refactoring a string-building loop with += into a
single " ".join(...) call for clarity and efficiency.

Expected output:
    AI helps in refactoring code
"""

def build_sentence(words):
    return " ".join(words)

words = ["AI", "helps", "in", "refactoring", "code"]
sentence = build_sentence(words)
print(sentence)
