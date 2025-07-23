# check armstrong number of n digits

num = input("enter the number:")

# calculate the lenght (num of digits)

order = len(num)

# Convert the input string to an INTEGER for math
num_int = int(num)

# initialize sum 
sum =0

# find the sum of the cube of each digit

temp = num_int
while temp>0:
    digit = temp % 10
    sum +=digit**order
    temp //= 10

# display the result

if num_int == sum:
    print(num,"is an armstrong number")

else:
    print(num,"is not an armstrong number")



