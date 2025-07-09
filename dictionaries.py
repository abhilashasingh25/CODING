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
student ={
    "name" : "shradha",
    "score" : {
             "chem":98,
               "phy":34,
               "bio":67,
               "eng":45
              },
    "age": 34,
    "height": 34.67,
    "female":True        
}
# print(student)
# print(student["name"])
# print(student["score"]["bio"])
print(student.keys())
print(list(student.keys()))
print(len(list(student.keys())))
print(student.values())
print(list(student.values()))
print(student.items())
pairs =list(student.items())
print(pairs[3])
# print(student["name2"]) this will give an error due to which the code below this line will not be executed 
print(student.get("score"))
print(student.get("keys")) # this code is worng and gives no error but gives NONE after executing the code and the rest of the cods will be executed the same
student.update{"city":"gorakhpur"}
print(student)