# write a function to print the elements if a list in a single line (list is the parameter)

num=[1 , 2, 3, 4, 5, 6, 7]
heroes=["thor","iron man","captain america","shaktimaan"]

def print_len(list):
    print(len(list))

def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(heroes )
print()
print_list(num)
print()        