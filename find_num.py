# search for a number x in this tuple using loop:
# (1,4,9,16,25,36,49,64,81,100),4924
x =int(input("enter the number:"))
i=1
while i<=10:
    m=i*i
    if(m==x):
        print("found at index" ,i)
    i+=1 
      