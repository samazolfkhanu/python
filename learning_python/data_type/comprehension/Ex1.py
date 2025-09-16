students=[
    ("Sama",101),
    ("Sima",102),
    ("Sara",103),
    ("Sama",102)
]
dict={}
for student in students:
    dict.setdefault(student[0],set()).add(student[1])
print(dict)

print("________________________")

#ex2
dict={"Sama":["Sky","Freedom"],"Bright":["Shiny","Smart"],"Clever":["Smart","Intelligent"]}
rec={}
for key,value in dict.items():
    for v in value:
        rec.setdefault(v, list()).append(key)
print(rec)

print("________________________")

#ex3
dict={"math":["Sama","Sima"],"Physic":["Sara","Sima"],"AP":["Sama"]}
rec={}
for key,value in dict.items():
    for v in value:
        rec.setdefault(v,set()).add(key)
dict2={key:value for key,value in rec.items() if len(value)>1}
print(dict2)

print("________________________")

#ex4
text="hello world python hello code"
words=text.split()
char={}
for word in words:
    for w in set(word):
        char[w]=char.get(w,0)+1
uniq_chars={k:v for k,v in char.items() if v==1}
print(uniq_chars)

print("________________________")

#ex5
list=[
    ("ali","sara"),
    ("ali","reza"),
    ("sara","mona"),
    ("sara","amir"),
    ("reza","amir")
]
friend={}
for t in list:
    friend.setdefault(t[0],set()).add(t[1])
    friend.setdefault(t[1],set()).add(t[0])

max=0
pair=None
for p in friend:
        for q in friend:
            if p<q:
                m=len(friend[p].intersection(friend[q]))
                if m>max:
                    max=m
                    pair=(p,q)
print(pair)

print("________________________")

#ex6
purchases = [
    ("ali", "book"),
    ("sara", "book"),
    ("ali", "pen"),
    ("mona", "book"),
    ("reza", "pen"),
    ("sara", "laptop"),
]
dict={}
for purchase in purchases:
    if purchase[1] not in dict:
        dict[purchase[1]]=[0,set()]
    dict[purchase[1]][0]+=1
    dict[purchase[1]][1].add(purchase[0])
final={k:tuple(v) for k,v in dict.items() }
print(final)


