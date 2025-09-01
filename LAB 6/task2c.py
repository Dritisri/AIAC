def print_multiples_for(n):
    # use a for loop to print first 10 multiples of n
    for i in range(1, 11):
        print(n * i, end=' ')
    print()  # for newline

def print_multiples_while(n):
    # use a while loop to print first 10 multiples of n
    i = 1
    while i <= 10:
        print(n * i, end=' ')
        i += 1
    print()  # for newline

# Example usage to display output
print("Multiples of 5 using for loop:")
print_multiples_for(5)

print("Multiples of 7 using while loop:")
print_multiples_while(7)

# Explanation:
# The function print_multiples_for(n) uses a for loop to iterate from 1 to 10,
# printing n multiplied by the current index in each iteration.
# The function print_multiples_while(n) uses a while loop, starting from 1 and incrementing up to 10,
# printing n multiplied by the current value of the counter in each iteration.
# Both functions print the first 10 multiples of the given number n.
