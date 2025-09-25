# python program to calculate the power of a number 
# calculate the power of a number using a for loop

base = 3
exponent =4
result = 1

for exponent in range (exponent,0,-1):
    result *=base

print("answer=" +str(result))