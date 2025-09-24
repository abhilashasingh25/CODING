# python program to get line count of a file

# using a for loop

def file_len (fname):

    with open(fname)as f:
        for i,l in enumerate(f):
            pass

    return i+1

print (file_len ("my_file.txt"))    