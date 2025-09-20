# python program to catch multiple exception in one line -multiple exceptin as a parentesized tuple

string = input()

try:
    num = int(input())
    print(string+num)
except(TypeError,ValueError) as e:
    print(e)    