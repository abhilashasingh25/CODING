# python program to remove the items that are duplicated in two lists

list_1 =[1,2,3,1,4,2,5]
list_2=[7,8,9,1,2]

print(list(set(list_1)^set(list_2)))