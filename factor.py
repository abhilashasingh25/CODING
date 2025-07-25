# python program to find the factors of a number

# this function computes the factor of the argument passed

def print_factors(x):
    print("the factors of ",x,"are:")
    for i in range(1,x+1):
        if x % i == 0:
            print (i)

num = int(input("enter the number:"))
print_factors(num)
