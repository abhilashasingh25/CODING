# python program to print half pyramid using a number

row = int (input ("enter numberof rows:"))

for i in range (row):
    for j in range(i+1):
        print(j+1,end=" ")

    print()    