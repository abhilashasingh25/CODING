#  this function adds two numbers
def add(x,y):
    return x+y
# this function substracts two numbers
def substract(x,y):
    return x-y
# this function multiply two numbers
def multiply(x,y):
    return x*y
# this function devide two numbers
def devide(x,y):
    return x/y
print("select option")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Devide")

while True:
    # take input from the user
    choice = input("enter choice(1/2/3/4):")
    # check if choice is one of the four options
    if choice in ('1','2','3','4'):
        try:
            num1 = float(input("enter the first number:"))
            num2 = float(input("enter the second number:"))

        except ValueError:
            print("invalid input. Please enter a number.")
            continue
        if choice == '1':
            print(num1,"+",num2,"=",add(num1,num2))

        elif choice =='2':
            print(num1,"-",num2,"=",substract(num1,num2))

        elif choice =='3':
            print(num1,"*",num2,"=",multiply(num1,num2))

        elif choice =='4':
            print(num1,"/",num2,"=",devide(num1,num2))

        # check if user wants another calculation
        # break the while loop if the answer is no
        next_calc = input("let's do next calculation?(yes/no):")
        if next_calc == "no":
            break
    else:
        print("invalid input")                    
