# python program to count the number of each vowels using dictionary

# string of vowels

vowels='aeiou'

str ="hello, my name is abhilasha singh"

# make it suitable for caseless comparisons

str = str.casefold()

# make a dictionary with each vowel a key and a value 0

count ={}.fromkeys(vowels,0)

# count the vowels

for char in count :
    count[char] +=1

print(count)    