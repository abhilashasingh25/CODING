# write a program to find the sum of the first n natural numbers using while loops

n =int(input("enter the number:"))
i = int(input("enter the number:"))
sum =0
while i <= n :
    sum +=i
    i+=1

print("total sum=",sum)


# or

# n=int(input("enter the number:"))
# sum =0
# for i in range (1,n+1):
#     sum+=i
# print("total sum:",sum)    