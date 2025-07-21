# python program to swap two variables using a temporary variable with input fron user

# to take input from user

x = int(input("enter the number:"))
y = int(input("enter the number:"))

# create a temporary variable and swap the values

temp =x
x= y
y= temp

print("the value of x after swapping: ",x)
print("the value of y after swapping: ",y)