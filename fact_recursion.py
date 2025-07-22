# python program to find the factorial of a number using recursion and take input from user

def factorial(x):
    # this is a recursive function to find the factorial of an integer

    if x ==1 or x == 0:
        return 1
    else:
        # recursive call to the function
        return(x *factorial(x-1))

# take input from user

n = int(input("enter the user number:"))

# call the factorial function
result = factorial(n)

print("the factorial of ",n," is",result)