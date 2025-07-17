# create a new file "practice.txt" using python. Add the following data in it
""""
Hi everyone
we are lesrning File I/O
using Java
I like programming in Java
"""

with open("practice.txt","w")as f:
    f.write("Hi everyone\n we are learning File I/O")
    f.write("\nusing Java\n I like programming in Java")    