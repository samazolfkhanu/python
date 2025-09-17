import json
from decimal import Decimal

#ex1
# l=[]
# dict={"name":"Sama","age":19}
# dict2={"name":"Sima","age":25}
# l.append(dict)
# l.append(dict2)
# with open("F:\Python\learning_python/file\json\json_file\ex1.json","w")as f:
#     json.dump(l,f,indent=4,ensure_ascii=False) #indent and ensure_ascii make output more beautiful and readable
#     print("Information Added To File Successfully!")
# l.clear()
# with open("F:\Python\learning_python/file\json\json_file\ex1.json","r") as file:
#     l=json.load(file)
# for d in l:
#     for key,value in d.items():
#         print(key,":",value)


#ex2
# dict={"c":1,"a":2,"b":3}
# with open("F:\Python\learning_python/file\json\json_file\ex2.json","w") as f:
#     json.dump(dict,f,sort_keys=True,indent=4) #sort_keys sort the key in dictionary
# dict.clear()
# with open("F:\Python\learning_python/file\json\json_file\ex2.json","r")as file:
#     dict=json.load(file)
# print("Sorted Keys: ")
# for k,v in dict.items():
#     print(k,":",v)


#ex3
# data={"age":25,"height":1.75,"score":100}
# with open("F:\Python\learning_python/file\json\json_file\ex3.json","w") as f:
#     json.dump(data,f)
# data.clear()
# with open("F:\Python\learning_python/file\json\json_file\ex3.json","r") as file:
#     data=json.load(file,parse_int=float,parse_float=Decimal) #parse_int converts all int in file to float while reading from file also parse-float converts all f;oat into decimal
# for k,v in data.items():
#     print(k,":",v)


#ex4
from Functions import A
#this method inverts all objects in list while reading from file to the object of employee class(Employee Class and Function relates to this part)
with open("F:\Python\learning_python/file\json\json_file\ex4.json","r") as file:
    data = json.load(file,object_hook=A)
for employee in data:
    print(employee)

