list=[1,2,3,4,"Sama",True]
print(list[1])

print("______________________")

list.append(7)
#Iteratio on List
for value in list:
    print(value)
print("______________________")

list.extend([0,10,45])
list.remove(2)
#Iteration on List
for i in range(len(list)):
    print(list[i])
    i+=1

print("_______________________")

list.insert(0,"hello")
#Iteration on List
for index,value in enumerate(list):
    print(index,":",value)
