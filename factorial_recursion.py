# python program to find the factorial of number using recursion

def recur_factorial(n):
    if n == 1:
        return n 
    else:
        return n*recur_factorial(n-1)
    
# take input from user  

num = int(input("enter the number:"))

# check if the number is negative

if num < 0:
    print("sorry,factorial does not exist for negative number")

elif num == 0:
    print("the factorial of 0 is 1")

else:
    print("the factorial of ",num," is ",recur_factorial(num))
            
