# python program to concatenate two lists using iterable unpacking perator*

list_1 =[1,'a']
list_2 =range(2,6)

list_joined =[*list_1, *list_2]

print(list_joined)