# python program to count the number of each vowel using a listand a dictionary comprehension

# .using dictionary and list comprehenssion

str ="hello, my name is abhilasha singh."

# make it suitable for caseless comprehensions

str = str.casefold()

# count the vowels

count ={x:sum([1 for char in str if char == x]) for x in 'aeiou'}

print (count)