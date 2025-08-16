# python program to invert full pyramid of *

row = int (input("enter number of rows:"))

for i in range(row,1,-1):
    for space in range(0,row-i):
        print(" ",end=" ")

    for j in range(i,2 *i-1):
        print("*",end=" ")

    for j in range (1,i-1):
        print("*",end=" ")

    print()            