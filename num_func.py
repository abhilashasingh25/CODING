
#write a function to input a number by user and return a string "ODD" if the number is odd and return "EVEN" if the number is EVEN

n=int(input("enter a number:"))
def num (n):
    if (n%2 ==0):
        return "EVEN"
    else:
        return "ODD"
        
print(num(n))    