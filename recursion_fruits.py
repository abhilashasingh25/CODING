# write a recursive function to print all elements in a list 
# hint: use list and index as parameters

def print_list (list , index=0):
    if (index == len(list)):
        return
    print(list[index])
    print_list(list,index+1)

fruits=["mango","litchi","apple","banana"]

print_list(fruits)