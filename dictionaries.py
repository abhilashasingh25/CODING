# info ={
#     "ask":(1,"asd",65.4,True),
#     "ert":["23","34","563","53"],
#     "key" : "value",
#     "name" : "abhilasha",
#     "learing":"coding",
#     "age" : 32,
#     "is_adult": True,
#     "marks": 56.6 , 12:23,12.34:234,12.3:"anshu" ,True :123,
#     "[1,2,3,4]":"anshu"
# }
# # print(info)
# # print(type(info))
# # print(info["ert"])
# info["name"] = "anshu"
# print(info)
# info["surname"]= "singh"
# print(info)

# nested dictionary
# student ={
#     "name" : "shradha",
#     "score" : {
#              "chem":98,
#                "phy":34,
#                "bio":67,
#                "eng":45
#               },
#     "age": 34,
#     "height": 34.67,
#     "female":True        
# }
# print(student)
# print(student["name"])
# print(student["score"]["bio"])
# print(student.keys())
# print(list(student.keys()))
# print(len(list(student.keys())))
# print(student.values())
# print(list(student.values()))
# print(student.items())
# pairs =list(student.items())
# print(pairs[3])
# # print(student["name2"]) this will give an error due to which the code below this line will not be executed 
# print(student.get("score"))
# print(student.get("keys")) 
# # this code is worng and gives no error but gives NONE after
# # executing the code and the rest of the cods will be executed the same
# student.update({"city":"gorakhpur" ,"living":"yes"})
# print(student)

# sets
nums ={1,2,3,5,2,6,7,6,1,4}
print(nums)
print(type(nums))
null_set={}  #this will be considered as  empty dictionary 
print(null_set)
print(type(null_set))

set =set()   #this is considered as empty set
print(set)
print(type(set))

nums.add(9)
print(nums)
nums.remove(2)
print(nums)
nums.pop()
print(nums)

nums.clear()
print(nums)

set1 ={1,2,3,4,5,6,7}
set2={4.5,6,7,8,9,10,11}
print(set1.union(set2))
print(set1.intersection(set2))


