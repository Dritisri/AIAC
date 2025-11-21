"""
Q2: Custom Stack to track last 10 operations
"""

class ParcelStack:
    """
    A custom implementation of a Stack for storing parcel tracking history.
    Tracks only the last 10 operations.
    """

    def __init__(self, history_limit=10):
        self.stack = []                # Actual stack storage
        self.history = []              # Stores last N operations
        self.history_limit = history_limit

    def _add_history(self, record):
        """Internal helper: adds new record and keeps only last 10 entries."""
        self.history.append(record)
        if len(self.history) > self.history_limit:
            self.history.pop(0)

    def push(self, item):
        """Push an item onto the stack."""
        self.stack.append(item)
        self._add_history(f"PUSH {item}")

    def pop(self):
        """Pop item from stack; if empty, return None."""
        if not self.stack:
            self._add_history("POP FAILED")
            return None
        value = self.stack.pop()
        self._add_history(f"POP {value}")
        return value

    def peek(self):
        """Returns top item without removing it."""
        if not self.stack:
            self._add_history("PEEK FAILED")
            return None
        value = self.stack[-1]
        self._add_history(f"PEEK {value}")
        return value

    def get_history(self):
        """Returns last operations."""
        return list(self.history)


# ------------------------------
# UNIT TESTS FOR Q2
# ------------------------------

import unittest

class TestParcelStack(unittest.TestCase):

    def test_push_operation(self):
        """Stack should store pushed items."""
        s = ParcelStack()
        s.push("P100")
        self.assertEqual(s.stack[-1], "P100")

    def test_pop_operation(self):
        """Pop should return the last pushed item."""
        s = ParcelStack()
        s.push("A1")
        result = s.pop()
        self.assertEqual(result, "A1")

    def test_history_limit(self):
        """History should only keep last 10 operations."""
        s = ParcelStack()
        for i in range(15):
            s.push(f"P{i}")
        self.assertEqual(len(s.get_history()), 10)  # Only 10 latest operations


if __name__ == "__main__":
    unittest.main()
