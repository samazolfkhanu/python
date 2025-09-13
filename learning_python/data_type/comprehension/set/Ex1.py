set={1,2,3,4,5,6,6,6,"Sama","Sama"}
set.add(10)
for value in set:
    print(value)

print("_____________________")

 #You Cannot remove elements in set during iteration for the size of set must be constant during iteration
for index,value in enumerate(list(set)):
    if(index%2==0):
        set.discard(value)

for value in set:
    print(value)

print("_____________________")

set2={1,2,6,3,6,1,10,68}
print(set.union(set2))

print(set.intersection(set2))

print(set-set2)

print(set ^ set2)