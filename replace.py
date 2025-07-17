# write a function that replaces all occurances of "Java" with "python" in practice.txt

with open ("practice.txt","r")as f:
    data = f.read()
new_data =data.replace("java","python")
print(new_data)

with open("practice.txt","w")as f:
    f.write(new_data)