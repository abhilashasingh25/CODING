# python program to extract extention from the file name

# using splittext() method from os module

import os

file_details = os.path.splitext('/path/file.ext')

print(file_details)

print(file_details[1]) 