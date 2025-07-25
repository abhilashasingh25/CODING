#  python program to print the fibonacci sequence

num = int (input("how many terms?"))

# first 2 terms

n1,n2= 0, 1
count =0
# check if the number of terms is valid
if num <= 0:
    print("please enter a positive integer")

# if there is only one term ,return n1    
elif num == 1:
    print("fabonacci sequence upto ",num)
    print(n1)

# generate fibonacci sequence

else:
    print("fibonacci sequence:")
    while count < num:
        print(n1)
        nth = n1 +n2
        # update values
        n1 =n2
        n2 =nth
        count +=1 