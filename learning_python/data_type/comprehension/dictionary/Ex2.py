#ex1
dict={"name":"sama","major":"computer","age":19}
print(dict.get("major"))

print("____________________")

#ex2
dict["score"]=20
dict["age"]=21
print(dict)

print("____________________")

#ex3*
"""for deleting a pair in dictionary we have two way one of them is del dict[...] in this way if key
does not exit KeyError will ocurred for removing safely you can use dict.pop(key,default output)"""
dict={"name":"sama","adress":"Zanjan"}
dict.pop("adress")
print(dict)

print("____________________")

#ex4*
#reversing dictionary
dict={"name":"sama","adress":"Zanjan","City":"Zanjan"}
inv={}
for k,v in dict.items():
    inv.setdefault(v,[]).append(k)
print(inv)

print("____________________")

#ex5*
d1={1:2,3:4,5:6}
d2={1:4,10:12,3:[1,2,3]}
for k,v in d2.items():
    if k in d1:
        a=d1.get(k)
        if isinstance(a,(int,float)) and isinstance(v,(int,float)):
            d1[k]=v+a
        else:
            if not isinstance(a,list) :
                a=[a]
            if not isinstance(v,list) :
                v=[v]
            d1[k]=v+a
    else:
        d1[k]=v
print(d1)

print("____________________")

#ex6
keys=[1,2,3,4]
values=[5,6,7,8]
d={}
for index,key in enumerate(keys):
    d[key]=values[index]
print(d)

print("____________________")

#ex7*
d={"Sama":20,"Sima":19,"Tara":4,"Diba":15,"Shara":17}
dict=sorted(d.items(),key=lambda k:k[1],reverse=True)
print(dict)
