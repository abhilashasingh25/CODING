# write a program to check if a list contains a palindrome of elements 
input_string = input("enter the elements of the list,seperated by spaces:")
original_list = input_string.split()
print(original_list)
print(type(original_list))
copy_list = original_list.copy()
copy_list.reverse()
if(copy_list == original_list):
    print("pallindrome")
else:
    print("not pallindrome")