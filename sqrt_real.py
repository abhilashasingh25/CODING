# write a program to find the square root for real or complex numbers

# import the complex math module 

import cmath

num = eval (input("enter a number:"))

num_sqrt = cmath.sqrt (num)

print("the square root of {0} is{1:0.3f}+{2:0.3f}j".format(num,num_sqrt.real,num_sqrt.imag))