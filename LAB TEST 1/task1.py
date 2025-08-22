def factorial_febo(n):
    # Calculate factorial
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i

    # Generate Fibonacci series up to n terms
    fibo_series = []
    a, b = 0, 1
    for _ in range(n):
        fibo_series.append(a)
        a, b = b, a + b

    return factorial, fibo_series

# Example usage:
num = int(input("Enter a number: "))
fact, fibo = factorial_febo(num)
print(f"Factorial of {num} is {fact}")
print(f"Fibonacci series up to {num} terms: {fibo}")