#ex1
s={1,2,3,4,5}
for value in s:
    print(value)
s.remove(4) #if 4 does not exit Error will occur for providing this use discard
s.add(10)
for value in s:
    print(value)