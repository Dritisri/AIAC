"""Lab 9 - Task 3

Simple interactive calculator that performs addition, subtraction, multiplication,
and division using NumPy operations. The user selects an operation from a menu,
enters two numbers, and the result is printed. Division by zero is handled
gracefully by displaying an error message.
"""

import numpy as np

def add():
    """Prompt for two numbers, add them with NumPy, and print the result."""
    # Read operands from the user
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    # Use NumPy's add for demonstration (equivalent to a + b for scalars)
    result = np.add(a, b)
    print(f"Result: {result}")

def subtract():
    """Prompt for two numbers, subtract them with NumPy, and print the result."""
    # Read operands from the user
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    # Use NumPy's subtract (equivalent to a - b for scalars)
    result = np.subtract(a, b)
    print(f"Result: {result}")

def multiply():
    """Prompt for two numbers, multiply with NumPy, and print the result."""
    # Read operands from the user
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    # Use NumPy's multiply (equivalent to a * b for scalars)
    result = np.multiply(a, b)
    print(f"Result: {result}")

def divide():
    """Prompt for two numbers, divide safely, and print the result.

    Guards against division by zero by printing an error and returning early.
    """
    # Read operands from the user
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    # Handle division by zero explicitly
    if b == 0:
        print("Error: Division by zero")
        return
    # Use NumPy's divide (equivalent to a / b for scalars)
    result = np.divide(a, b)
    print(f"Result: {result}")

if __name__ == "__main__":
    # Main interactive loop for the calculator
    while True:
        print("\nCalculator Menu:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add()
        elif choice == '2':
            subtract()
        elif choice == '3':
            multiply()
        elif choice == '4':
            divide()
        elif choice == '5':
            print("Exiting calculator...")
            break
        else:
            print("Invalid choice. Please try again.")

