"""Select arithmetic operations via a dictionary-based dispatch.

This script replaces an if-elif chain with a mapping from operation names to
callables, making it easy to add new operations while preserving behavior.

Expected output for operation "multiply" and inputs 5, 3:
    15
"""

operation = "multiply"
a, b = 5, 3

operations = {
    "add": lambda x, y: x + y,
    "subtract": lambda x, y: x - y,
    "multiply": lambda x, y: x * y,
}

func = operations.get(operation)
result = func(a, b) if func else None

print(result)