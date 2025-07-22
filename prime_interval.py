# python progrma to print all prime numbers in an interval

lower = int(input("enter the number:"))
upper = int(input("enter the number:"))

print("prime number between ",lower," and", upper," are:")

for n in range (lower,upper+1):
    #  all the prime numbers are greater than 1
    if n > 1:
        for i in range(2,n):
            if (n% i) ==0:
                break
        else:
            print(n)

