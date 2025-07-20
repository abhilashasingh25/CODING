# write a python program to calculate the area of a triangle

# take input from a user

a =float(input("enter the number:"))
b =float(input("enter the number:"))
c =float(input("enter the number:"))

# calculate the semi- perimeter
s =(a+b+c)/2

# calculate the area

area =(s*(s-a)*(s-b)*(s-c)**0.5)
print("the area of the triangle is ",area)