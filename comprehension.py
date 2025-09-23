# python program to convert two lists into a dictinary

# using list comprehension

index =[1,2,3]

languages =['pyton','c','c++']

dictionary ={k:v for k,v in zip (index,languages)}

print(dictionary)