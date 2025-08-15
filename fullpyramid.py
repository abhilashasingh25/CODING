# python program to print full pyramid using *

row = int(input("enter number of rows:"))



for i in range (row):

    space  =" " * (row-i-1)



    star = "*" * (2*i+1)
    print(space +star)          