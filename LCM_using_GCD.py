# python program to compute LCM using GCD

# THIS function compute GCD

def compute_gcd(x,y):
    while (y):
        x,y = y, x% y
    return x
# this function compute LCM 

def compute_lcm(x,y):
    lcm = (x*y) // compute_gcd(x,y)
    return lcm

num1 = int (input("enter the number:"))
num2 = int(input("enter the number:"))
print("the lcm is ",compute_lcm(num1,num2))
 