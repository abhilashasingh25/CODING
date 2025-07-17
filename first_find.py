# write a function to find in which line of the file does the word "learning" occurs first.
# print -1 if the word not found

def check_for_line():
    word ="learning"
    data =True
    line_no= 1
    with open("practice.txt","r")as f:
        while data:
            data =f.readline()
            if(word in data):
                print(line_no)
                return
            line_no +=1

        return -1

print(check_for_line())        