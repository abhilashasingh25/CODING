# search if the word "learning" exists in the file or not

word ="learning"

with open("practice.txt","r") as f:
    data = f.read()

    if (data.find(word) != -1):
        print("found")
    else:
        print("not found")  

# write a function to search if the word "learning" exists in the file or not

def check_for_word():
    word = "xlearning"
    with open("practice.txt","r") as f:
        data = f.read()
        if (data.find(word) != -1):
            print("found")
        else:
            print("not found")

check_for_word()                 
 