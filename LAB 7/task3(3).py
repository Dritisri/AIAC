data=open("input.txt").readlines()
output=open("output.txt","w")
for line in data:
    output.write(line.upper())
print("Processing done")