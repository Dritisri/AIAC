# 1. Using a FOR loop
def sum_to_n_for(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Step-by-step analysis:
# - Initialize total to 0.
# - Loop from 1 to n (inclusive).
# - Add each number i to total.
# - After the loop, return total.

# 2. Using a WHILE loop
def sum_to_n_while(n):
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total

# 3. Using Recursion
def sum_to_n_recursive(n):
    if n <= 0:
        return 0
    else:
        return n + sum_to_n_recursive(n - 1)

# 4. Using the direct mathematical formula
def sum_to_n_formula(n):
    return n * (n + 1) // 2

# Example usage and demonstration
if __name__ == "__main__":
    n = 5
    print("Sum to n using FOR loop:", sum_to_n_for(n))
    print("Sum to n using WHILE loop:", sum_to_n_while(n))
    print("Sum to n using Recursion:", sum_to_n_recursive(n))
    print("Sum to n using Formula:", sum_to_n_formula(n))

"""
Explanations:

1. FOR loop:
   - Iterates from 1 to n, adding each value to a running total.

2. WHILE loop:
   - Uses a counter variable, adds it to total, and increments until it exceeds n.

3. Recursion:
   - The function calls itself with n-1 until n is 0, summing up all values.

4. Formula:
   - Uses the mathematical formula for the sum of the first n natural numbers: n*(n+1)//2.
"""