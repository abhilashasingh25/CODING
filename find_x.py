# write a program to search for a number x in this tuple using loop
# (1,4,9,16,25,36,49,64,81,100,49)

nums =(1,4,9,16,25,36,49,64,81,100,49)
x=49
idx =0
for el in nums:
    if (el == x):
        print ("number found at index ", idx)
    idx +=1    
