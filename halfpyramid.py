# python program to print half pyramid using *

row = int(input("enter number of rows:"))

for i in range (row):
    for j in range(i+1):
        print("*",end=" ")

    print()    