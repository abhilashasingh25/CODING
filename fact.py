# python program to find the factorial of a number using loop

n =7
factorial =1
# check if the number is negative ,positive or zero

if n<0:
    print("sorry,factorial does not exist for negative numbers")

elif n ==0:
    print("the factorial of 0 is 1")

else:
    for i in range(1,n+1):

        factorial = factorial*i

print("the factorial of ",n," is",factorial)

