#ex1
def write_in_file(lst):
    with open("F:/Python/learning_python/file/txt/files/ex1.txt","w") as f:
        for x in lst:
            f.write(x+" ")
def read_from_file(path):
    name_list = []
    with open(path, "r") as f:
        line=f.readline()
        name_list=line.split(" ")
    return name_list

#ex2
def write_file(txt,path):
    with open(path,"w") as f:
        f.write(txt)
def read_file(path):
    with open(path,"r") as f:
        line=f.read()
    return line

#ex3
def w(dictionary,path):
    with open(path,"w")as f:
        for k,v in dictionary.items():
            f.write(k+":"+v+"\n")
def r(path):
    dictionary={}
    with open(path,"r") as f:
        for l in f:
            line =l.strip().split(":")
            dictionary[line[0]] = line[1]
    return dictionary

#ex4
def reverse(path):
    with open(path,"r") as f:
        line=f.readlines()
    with open(path,"w") as f:
        for l in line:
            f.write(l.strip()[::-1])
def read(path):
    with open(path,"r") as f:
        for l in f:
            return l
