# python program to print inverted half pyramid using numbers

row =int(input("enter numbers of rows:"))

for i in range (row,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")

    print()    