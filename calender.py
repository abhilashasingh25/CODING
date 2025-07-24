# python program to display calender

import calendar

# take month and year input from the user

yy= int(input("enter year:"))
mm = int(input("enter month:"))

# display calender

print(calendar.month(yy,mm))
