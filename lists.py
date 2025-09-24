# python program to get line count of a file 

# using list comprehension

num_of_lines =sum(1 for l in open ('my_file.txt'))

print (num_of_lines)