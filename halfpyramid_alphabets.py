# python program to print half pyramid using alphabets

row = int(input("enter number of rows:"))

ascii_value= 65

for i in range (row):
    for j in range(i+1):
        alphabet = chr(ascii_value)
        print(alphabet,end =" ")

    ascii_value +=1
    print()    