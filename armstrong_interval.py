# python program to find armstrong number in an interval

lower =int(input("enter the number:"))
upper =int(input("enter the nmber:"))

for num in range(lower,upper+1):
    # order of number
    order = len (str(num))
    # initialize sum
    sum =0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum +=digit **order
        temp //= 10
    if num ==sum:
        print(num)
            