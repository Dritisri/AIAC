
def sum_to_n_for(n):
    """
    Calculates the sum of the first n natural numbers using a FOR loop.
    """
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Step-by-step analysis:
# 1. Initialize a variable 'total' to 0.
# 2. Iterate from 1 to n (inclusive) using a for loop.
# 3. In each iteration, add the current number 'i' to 'total'.
# 4. After the loop, return 'total' which contains the sum.

def sum_to_n_while(n):
    """
    Calculates the sum of the first n natural numbers using a WHILE loop.
    """
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total

# Explanation:
# 1. Initialize 'total' to 0 and 'i' to 1.
# 2. While 'i' is less than or equal to n, add 'i' to 'total' and increment 'i'.
# 3. Return 'total' after the loop ends.

def sum_to_n_recursive(n):
    """
    Calculates the sum of the first n natural numbers using recursion.
    """
    if n <= 0:
        return 0
    else:
        return n + sum_to_n_recursive(n - 1)

# Explanation:
# 1. Base case: if n <= 0, return 0.
# 2. Recursive case: return n plus the sum of numbers up to n-1.

def sum_to_n_formula(n):
    """
    Calculates the sum of the first n natural numbers using the direct formula.
    """
    return n * (n + 1) // 2

# Explanation:
# 1. Uses the mathematical formula for the sum of the first n natural numbers: n*(n+1)//2.
# 2. This approach is efficient and does not require loops or recursion.

# Example usage and demonstration:
if __name__ == "__main__":
    n = 10
    print("Sum to n using FOR loop:", sum_to_n_for(n))
    print("Sum to n using WHILE loop:", sum_to_n_while(n))
    print("Sum to n using Recursion:", sum_to_n_recursive(n))
    print("Sum to n using Formula:", sum_to_n_formula(n))

