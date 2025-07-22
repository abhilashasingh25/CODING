# python program to check leap year

# get the input from user 
year = int(input("enter the number:"))

# devided by 100 means century year(ending with 00)
# century year devided by 400 is leap year

if (year % 400 == 0) and (year % 100 ==0):
    print(year,"is a leap year")

#not divided by 100 means not a century year
# year divided by 4 is a leap year

elif(year % 4 == 0)  and (year % 100 != 0):
    print(year,"is a leap year")

# if not devided by both400(century year) and 4(not century year)
# year is not leap year    

else:
    print(year,"is not a leap year") 