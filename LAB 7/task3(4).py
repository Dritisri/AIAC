with open("numbers.txt","r") as f:
    nums= f.readlines()
squares =[]
for num in nums:
    n=num.strip()
    if n.isdigit():
        squares.append(int(n)*int(n))
with open("squares.txt","w") as f2:
    for square in squares:
        f2.write(str(square) + "\n")
print("Squares written")
