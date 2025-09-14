#ex1
List=[10,20,30]

for value in List:
    print(value*2)

#ex2
List2=[5,6,7]
for i in range(len(List2)):
    print(List2[i])

#ex3
"""
متد extend لیست رو درجا (in-place) تغییر میده.
ولی هیچ مقداری برنمی‌گردونه → یعنی return None می‌کنه.
پس وقتی میگی print(list1.extend(list2)) داری None رو چاپ می‌کنی.
"""
list1=[1,2,3]
list2=[4,5,6]
list1.extend(list2)
print(list1)

#ex4
List3=[1,2,2,3]
print(List3.count(2))

#ex5
List4=[1,2,3,4,5,6,3]
print(List4.index(3))

#ex6
List5=[4,3,6,2,9,1]
List5.sort()
print(List5)

#ex7
list6=[3,2,1]
list6.reverse()
print(list6)