# python program to sort words in alphabetical order

# take input from the user

str = input("enter a string:")
# breakdown the string into a list if words

words =[word.lower()for word in str.split()]

# sort the list
words.sort()

# display the sorted words

print("The sorted words are:")

for word in words:
    print(word)