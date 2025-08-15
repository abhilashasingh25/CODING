# python program to print inverted half pyramid using *

row = int(input("enter number of rows:"))

for i in range(row,0,-1):
    for j in range (0,i):
        print("*",end=" ")

    print()    