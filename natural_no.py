# python progtam to find the sum of natural numbers

num = int(input("enter the number:"))

if num<0:
    print("enter the positive number")

else:
    sum = 0
    # use whileloop to iterate until Zero    
    while(num > 0):
        sum += num
        num -=1
    print("the sum is",sum)
         