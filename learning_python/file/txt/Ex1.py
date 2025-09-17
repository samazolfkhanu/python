from Ex1_fun import write_in_file ,read_from_file,write_file,read_file,w,r,reverse,read

# #ex1
#
# count=int(input("Enter Number of Members: "))
# name_list=[]
# for i in range(count):
#     name_list.append(input("Enter Name: "))
# write_in_file(name_list)
# print(read_from_file("F:/Python/learning_python/file/txt/files/ex1.txt"))
#
# print("______________________________")

# #ex2
#
# txt=input("Enter Text : ")
# write_file(txt,"F:\Python\learning_python/file/txt/files\ex2.txt")
# line=read_file("F:\Python\learning_python/file/txt/files\ex2.txt")
# print(len(line.split(" ")))

# #ex3
# dictionary={"Name1":"Sama","Name2":"Sima","Name3":"Sky"}
# w(dictionary,"F:\Python\learning_python/file/txt/files\ex3.txt")
# print(r("F:\Python\learning_python/file/txt/files\ex3.txt"))

#ex4
reverse("F:\Python\learning_python/file/txt/files\ex4.txt")
print(read("F:\Python\learning_python/file/txt/files\ex4.txt"))