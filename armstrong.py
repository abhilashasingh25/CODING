# python program to check armstrong number

# take input from the user

n = int (input("enter the number:"))

# initialize sum
sum =0

# find thesum of the cube of each digit

temp =n
while temp> 0:
    digit = temp % 10
    sum +=digit **3
    temp //=10

if n == sum:
    print (n ,"is an armstrong number")

else:
    print (n,"is not an armstrong number")        