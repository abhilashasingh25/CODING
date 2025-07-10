"""write a program to enter marks of 3 subjects from the user and store them inba dictionary .
start with an empty dictionary and add one by one .
use subject name as a key and marks as values
"""
subjects ={}
subjects.update( {"english" : 98 ,})
subjects.update({"computer":89})
subjects.update({"hindi":99})
print(subjects)

# or
marks ={}
x =int(input("enter the phy marks:"))
marks.update({"phy":x})
x =int(input("enter chem marks:"))
marks.update({"chem":x})
x =int(input("enter english marks:"))
marks.update({"eng":x})
print(marks)