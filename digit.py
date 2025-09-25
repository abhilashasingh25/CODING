# python program to count the number od digits present in a number

# count number of digits in an integer using while loop

num = 3452

count =0

while num!=0:
    num//=10
    count+=1

print("number of digits:" +str(count))