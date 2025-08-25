# python program to raising an exception if directory already exists

import os

try:
    os.makedirs("/dirA/dirB")

except FileExistsError:

    print("file alreay exists")    
    