# python program to solve quadratic equation

# import complex math module

import cmath

# take input number from the user

a = int(input("enter the number:"))
b = int(input("enter the number:"))
c = int(input("enter the number:"))

# calculate the discriminant

d = (b**2)-(4*a*c)

# find two solution

sol1 =(-b-cmath.sqrt(d))/(2*a)
sol2 =(-b+cmath.sqrt(d))/(2*a)

print("the solution are ",sol1,"and",sol2)