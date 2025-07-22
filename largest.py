# python program to find the largest among three numbers

# input from the user

a = float(input("enter the number:"))
b = float(input("enter the number:"))
c = float(input("enter the number:"))

if (a>=b) and (a>=c):
    print("the largest number is", a)
elif (b>=a) and (b>=c):
    print("the largest number is ",b)
else:
    print("the largest number is ",c)        