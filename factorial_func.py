# write a function to find the factorial of n.(n is the parameter)

def cal_func(n):
    fact = 1
    for i in range (1,n+1):
        fact*=i
    print(fact)
cal_func(5)
cal_func(8)    