# python program to find HCF or GCD USING LOOP

# define function 
def compute_hcf(x,y):

# choose the smaller number

    if x > y:
        smaller =y
    else:
        smaller = x
    for i in range (1,smaller+1):
        if ((x % i == 0) and (y % i == 0)):
         hcf =i
    return hcf

num1 = int (input("enter the number:"))
num2 = int (input("enter the number:"))
print ("the hcf is ",compute_hcf (num1,num2))    
             