# python program to find the sum of natural numbers using recursive function

def recur_sum(n):
    if n <= 1:
        return n 
    else:
        return n +recur_sum(n-1)
    
# take input from user 
num = int(input("enter the number:"))

if num < 0:
    print("enter a positive number")

else:
    print("the sum is",recur_sum(num))    