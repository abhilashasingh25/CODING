# write a program to find the factorial of first n numbers

n =int(input("enter the number:"))
factorial=1
for i in range (1,n+1):
    factorial*=i
print("factorial=",factorial)    