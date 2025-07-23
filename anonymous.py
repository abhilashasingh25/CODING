# python program to display powers of 2 using anonymous function

# take input from user
term = int (input("how many terms?"))

# use anonymous function

result = list (map(lambda x:2**x ,range (term)))

print("the total term are :",term)

for i in range (term):
    print("2 raised to the power ",i," is",result[i])