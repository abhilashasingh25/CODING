# python program to find LCM

def compute_lcm (x,y):
    # choose the greater number
    if x > y :
        greater = x
    else:
        greater =y
    while(True):
        if ((greater % x == 0)and (greater % y == 0)):
            lcm =greater
            break
        greater +=1
    return lcm

num1 = int (input("enter the number:"))
num2 = int (input("enter the number:"))
print("the lcm is ",compute_lcm(num1,num2))