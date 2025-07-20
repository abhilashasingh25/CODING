# write a python program to find the area of a triangle when the sides are given

a =5
b =6
c =7

# calculate the semi-perimeter

s=(a+b+c)/2

# calculaye the area

area = (s*(s-a)*(s-b)*(s-c))**0.5

print("the area of the triangle is ",area)