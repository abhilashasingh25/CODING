# phthon program to convertdecimal to binary using recursion

# fuction to print binary using recursion

def converttobinary(n):
    if n > 1:
        converttobinary(n // 2)
    print(n % 2 , end = '')

# decimalnumber
dec =34

converttobinary(dec)
print()      