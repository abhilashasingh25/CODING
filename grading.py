""" write a program to count the number of students with "A" grade in the
 following tuple and store the values in a list and sort them from "A" to "D" """


grade = ("C","A","D","C","A","A","B","D","C","A","B","C","D")
print(grade.count("A"))
list = list(grade)
print(list)
list.sort()
print(list)