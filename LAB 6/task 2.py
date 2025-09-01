def print_multiples_for(n):
    for i in range(1, 11):
        print(n * i)

def print_multiples_while(n):
    i = 1
    while i <= 10:
        print(n * i)
        i += 1

# Example usage:
print("Multiples using for loop:")
print_multiples_for(5)

print("\nMultiples using while loop:")
print_multiples_while(5)