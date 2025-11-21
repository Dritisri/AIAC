class ParcelStack:
    """
    Stack implementation to store parcel tracking IDs.
    It also keeps history of only the latest `history_limit` operations.
    """

    def __init__(self, history_limit=10):
        """
        Initialize an empty stack and an empty history list.

        :param history_limit: Maximum number of operations to remember.
        """
        self._items = []          # actual stack
        self._history = []        # stores text descriptions of operations
        self._history_limit = history_limit

    def _add_history(self, entry):
        """
        Internal helper to add an entry to the history.
        Ensures only the latest `history_limit` entries are kept.
        """
        self._history.append(entry)
        # If history is longer than limit, drop the oldest entry
        if len(self._history) > self._history_limit:
            self._history.pop(0)

    def push(self, parcel_id):
        """
        Push a new parcel ID onto the stack.
        """
        self._items.append(parcel_id)
        self._add_history(f"PUSH {parcel_id}")

    def pop(self):
        """
        Pop the top parcel from the stack.
        Returns the parcel ID or None if stack is empty.
        """
        if not self._items:
            self._add_history("POP (failed: empty)")
            return None
        value = self._items.pop()
        self._add_history(f"POP {value}")
        return value

    def peek(self):
        """
        Return the top parcel without removing it.
        """
        if not self._items:
            self._add_history("PEEK (failed: empty)")
            return None
        value = self._items[-1]
        self._add_history(f"PEEK {value}")
        return value

    def is_empty(self):
        """
        Check if the stack is empty.
        """
        empty = len(self._items) == 0
        self._add_history(f"ISEMPTY -> {empty}")
        return empty

    def size(self):
        """
        Return current size of the stack.
        """
        size = len(self._items)
        self._add_history(f"SIZE -> {size}")
        return size

    def get_history(self):
        """
        Return a copy of the operation history (oldest to newest).
        """
        return list(self._history)


# ---------- TEST CASES ----------
if __name__ == "__main__":
    s = ParcelStack()

    # Test 1: basic pushes
    s.push("P100")
    s.push("P101")
    s.push("P102")
    print("Stack after pushes:", s._items)

    # Test 2: peek and pop
    top = s.peek()
    popped = s.pop()
    print("Top element from peek:", top)
    print("Popped element:", popped)
    print("Stack after pop:", s._items)

    # Test 3: create more than 10 operations to see history limit
    for i in range(10):
        s.push(f"P20{i}")

    print("Number of history records:", len(s.get_history()))
    print("History (oldest to latest):")
    for record in s.get_history():
        print(record)
